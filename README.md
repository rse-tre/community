# Research Software Engineers Trusted Research Environment Working Group (RSETREWG)

[![Build](https://github.com/manics/rse-tre/actions/workflows/build.yml/badge.svg)](https://github.com/manics/rse-tre/actions/workflows/build.yml)
[![Documentation Status](https://readthedocs.org/projects/rse-tre-community/badge/?version=latest)](https://rse-tre-community.readthedocs.io/en/latest/?badge=latest)

https://rse-tre-community.readthedocs.io/

# :wave: Welcome to the RSE TRE WG repo!

This repo is for Research Software Engineers (RSEs), researchers, Trusted Research Environment (TRE) users, developers and enthusiasts to collaborate on and communicate about open-source TRE infrastructure.

Our [Code of Conduct]() applies to all interactions within this space. We value the participation of every member of the community and want to ensure that everybody has an enjoyable and fulfilling experience. 

We want this space to be community-driven, and not have any one voice direct conversation. Please use it as a free-form place to share thoughts and ideas, work together on resolving problems, and discuss where the community should be focusing our efforts!

# :family: Community and Support

- Visit [our readthedocs site](https://rse-tre-community.readthedocs.io/en/latest/index.html#) to see latest developments with the community
- Join the `rse-tre-wg` Slack channel in the [RSE Slack Workspace](https://docs.google.com/forms/d/e/1FAIpQLSdqs-_QNwQFzCIUEafah91E5E00lGUEnTPC4jjYbGUqPjONwA/viewform)
- Look through our [issues on GitHub](https://github.com/rse-tre/community/issues) to see what we're working on, and create a new issue if you have something to add!

# :handshake: Contributing

We welcome contributions from anyone who is interested in this community.
There are lots of ways to contribute, not just writing docs!

See our [Code of Conduct](CODE_OF_CONDUCT.md) and our [Contributor Guide](CONTRIBUTING.md) to learn more about how we work together as a community and how you can contribute.

# :link: Useful links
* [Our readthedocs site](https://rse-tre-community.readthedocs.io/en/latest/index.html#)
* [The report from our latest meeting](https://rse-tre-community.readthedocs.io/en/latest/events/wg_workshops/rsecon22/index.html)

## :computer: Building the docs

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

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-13-orange.svg?style=flat-square)](#contributors)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
