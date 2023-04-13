# env_color_logger

[![Latest Release](https://img.shields.io/github/v/release/ofersadan85/env_color_logger)](https://github.com/ofersadan85/env_color_logger/releases/latest)
[![env_color_logger on pypi](https://img.shields.io/pypi/v/env_color_logger)](https://pypi.org/project/env_color_logger/)
[![MIT License](https://img.shields.io/github/license/ofersadan85/env_color_logger)](LICENSE)
[![Python package tests](https://github.com/ofersadan85/env_color_logger/actions/workflows/tests.yml/badge.svg)](https://github.com/ofersadan85/env_color_logger/actions/workflows/tests.yml)

A simple logger that prints colored messages to the console and uses environment variables to control the basic setup.

See [example.env](example.env) for a list of environment variables that can be used to control the logger.

## Install

[![env_color_logger on pypi](https://img.shields.io/pypi/v/env_color_logger)](https://pypi.org/project/env_color_logger/)
![wheel](https://img.shields.io/pypi/wheel/env_color_logger)

```bash
pip install --upgrade env_color_logger
```

## Usage

The usage in Python is very basic. Just import the logger and use it as you would use the standard `logging` module. The logger will automatically use the environment variables to configure itself. This is done to aid in development of apps that are run in isolated environments, such as Docker containers.

```python
from env_color_logger import EnvLogger

logger = EnvLogger(__name__)
logger.info("Hello World!")
```

## Requirements

![Python Versions](https://img.shields.io/pypi/pyversions/env_color_logger)

Tested with & designed for python 3.10, see [requirements.txt](requirements.txt) for additional dependencies

## Contributing

For bugs / feature requests please submit [issues](https://github.com/ofersadan85/env_color_logger/issues)

[![Open Issues](https://img.shields.io/github/issues-raw/ofersadan85/env_color_logger)](https://github.com/ofersadan85/env_color_logger/issues)
[![Closed Issues](https://img.shields.io/github/issues-closed-raw/ofersadan85/env_color_logger)](https://github.com/ofersadan85/env_color_logger/issues)

If you would like to contribute to this project, you are welcome
to [submit a pull request](https://github.com/ofersadan85/env_color_logger/pulls)

[![Open Pull Requests](https://img.shields.io/github/issues-pr-raw/ofersadan85/env_color_logger)](https://github.com/ofersadan85/env_color_logger/pulls)
[![Closed Pull Requests](https://img.shields.io/github/issues-pr-closed-raw/ofersadan85/env_color_logger)](https://github.com/ofersadan85/env_color_logger/pulls)

## Warranty / Liability / Official support

This project is being developed independently, we provide the
package "as-is" without any implied warranty or liability, usage is your own responsibility

## Additional info

Just because I like badges

![Code Size](https://img.shields.io/github/languages/code-size/ofersadan85/env_color_logger)
![Pypi downloads per month](https://img.shields.io/pypi/dm/env_color_logger?label=pypi%20downloads)
![Pypi downloads per week](https://img.shields.io/pypi/dw/env_color_logger?label=pypi%20downloads)
![Pypi downloads per day](https://img.shields.io/pypi/dd/env_color_logger?label=pypi%20downloads)
