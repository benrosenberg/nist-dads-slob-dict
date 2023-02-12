# NIST Dictionary of Algorithms and Data Structures (DADS) SLOB file

This repository hosts a `*.slob` ("sorted list of blobs") file for use with [Aard2](https://github.com/itkach/aard2-android). For other dictionaries see [the dictionary page on the SLOB repo](https://github.com/itkach/slob/wiki/Dictionaries). For more information on the SLOB format see the [SLOB repo](https://github.com/itkach/slob).

The file in question is an amateur attempt at creating a dictionary for the NIST Dictionary of Algorithms and Data Structures (DADS). There is no image support right now. The [downloader script](https://github.com/benrosenberg/nist-dads-slob-dict/blob/main/stageIndex.py) is a work in progress and assumes a sanitized index in `index.html` (one entry per line of the form seen in the [repo's `index.html` file](https://github.com/benrosenberg/nist-dads-slob-dict/blob/main/index.html)) and is not for general use.

## Requirements

If you *do* want to use the downloader script (not recommended), you will need the `slob` and `wget` Python packages installed. See the [SLOB repo readme](https://github.com/itkach/slob) for information on how to install the `slob` Python package.
