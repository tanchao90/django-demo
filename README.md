# django-demo
A django demo.


## Development Environment
- macOS Sierra 10.12.6
- [Python](https://www.python.org/) 3.6.2
- [Django](https://djangoproject.com) 1.11.4


## Development Progress
#### 2017.08.05
- Build the dev env.
- Learn `Writing your first Django app, part 1` in Getting started.
- Create `polls` apps.


## Reference
- [Django documentation](https://docs.djangoproject.com/en/1.11/)
- [Tutorials: Getting started](https://docs.djangoproject.com/en/1.11/intro/)


## Problem
- `pyenv install 3.6.2`
    - `xcode-select --install`
    - [zipimport.ZipImportError: can't decompress data; zlib not available](https://github.com/pyenv/pyenv/issues/454)
- `pip install Django`
    - `pip install --default-timeout=100 Django`
    - [pip._vendor.requests.packages.urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host='pypi.python.org', port=443): Read timed out.](https://stackoverflow.com/questions/43298872/how-to-solve-pip-readtimeouterror-httpsconnectionpoolhost-pypi-python-org-p)


