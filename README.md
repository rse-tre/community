# Research Software Engineers Trusted Research Environment

[![Build](https://github.com/manics/rse-tre/actions/workflows/build.yml/badge.svg)](https://github.com/manics/rse-tre/actions/workflows/build.yml)
[![Documentation Status](https://readthedocs.org/projects/rse-tre-community/badge/?version=latest)](https://rse-tre-community.readthedocs.io/en/latest/?badge=latest)

https://rse-tre-community.readthedocs.io/

## Overview

This repository is published using [Read the Docs](https://rse-tre-community.readthedocs.io/).
The documentation is built with Sphinx, and written in [Markdown with the MyST Parser](https://myst-parser.readthedocs.io/).

To build this repository locally, create a Python environment and install the requirements:

```sh
cd docs
pip install -r requirements.txt
```

Then build the documentation:

```sh
make html
```

[pre-commit](https://pre-commit.com/) is used to check the documentation for common issues, and to auto-format all content.

To run pre-commit locally:

```sh
pre-commit run --all-files
```
