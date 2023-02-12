import re, os, sys, math, time
import slob
import wget

# file containing cleaned DADS index
INDEX_FILE = 'index.html'
print('Reading from index file "{}"'.format(INDEX_FILE))

OUT_FILE = 'dads.slob'
print('Writing to "{}"'.format(OUT_FILE))

# if getting ratelimited
SLEEP_TIME = 0

if OUT_FILE in os.listdir():
    print(f'File {OUT_FILE} already in directory.')
    choice = input('Overwrite? [y/N] ')
    if choice == 'y':
        os.remove(OUT_FILE)
    else:
        print('Aborting.')
        sys.exit(0)

with open(INDEX_FILE, 'r') as f:
    entries = f.readlines()

# remove trailing newlines
entries = [e.strip() for e in entries]

nonpointer_regex = re.compile(r'<a href="(.*)">(.*)</a>')
pointer_regex = re.compile(r'(.*): see <a href="(.*)">(.*)</a>')

# create a dictionary of all the entries in the DADS index
HTML_TEXT = 'text/html; charset=utf-8'

DADS_HTML_PREFIX = 'http://xlinux.nist.gov/dads/'
dads_entries = {}

print('Generating file...')
processed_entries = 0

with slob.create(OUT_FILE) as w:
    time.sleep(SLEEP_TIME)
    is_pointer = lambda entry : not entry.startswith('<a href')
    # build up dictionary iteratively
    for entry in entries:
        if not is_pointer(entry):
            # parse out link and name
            try:
                link, name = nonpointer_regex.match(entry).groups()
            except:
                print('nonpointer regex failed on {}'.format(repr(entry)))
                continue
            # download link
            full_link = DADS_HTML_PREFIX + link
            filename = wget.download(full_link, bar=None)
            # get page data
            with open(filename, 'r') as f:
                contents = f.read()
            # create entry
            html_link = link[len('HTML/'):]
            w.add(contents.encode('utf-8'), name, html_link, content_type=HTML_TEXT)
            # clean up
            os.remove(filename)
        else:
            try:
                alias, _, name = pointer_regex.match(entry).groups()
            except:
                print('pointer regex failed on {}'.format(repr(entry)))
                continue
            # create alias
            w.add_alias(alias, name)
        processed_entries += 1
        processed_frac = math.floor(50 * processed_entries/len(entries))
        print('[' + '=' * (processed_frac-1) + '>' +
              ' ' * (50 - processed_frac) + ']', end='\r')

print('[' + '=' * 51 + ']')