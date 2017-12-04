======================================================
Python package for Kaggle Spooky Author identification
======================================================


Implemented: just a tfidf with a Linear Regression. simple but efficient!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


This repository is a minimal example of how to share packaged code for collaborative reuse.

structure of the directory:
.
├── MANIFEST.in
├── README.rst
├── setup.py
└── spooky
    ├── __init__.py
    ├── config.ini
    ├── data
    │   ├── test.zip
    │   └── train.zip
    ├── loader.py
    ├── output
    │   └── simple_submission.csv
    ├── preprocess.py
    ├── spooky.py
    └── trainer.py

3 directories, 12 files


*************************
Collaborative guidelines:
*************************

**we don't need to be able to understand all the code, but easily use the function !!**

- write code following `packaging guidelines <https://python-packaging.readthedocs.io>`_

- write documented and commented codes
- write reusable codes:


To use this package, just add the command line:

pip install /path/to/spooky

python spooky.py

-max_features           command-line option "max_features"


