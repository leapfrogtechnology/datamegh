SHELL :=/bin/bash
CWD := $(PWD)
TMP_PATH := $(CWD)/.tmp
VENV_PATH := $(CWD)/.venv

clean:
	@rm -rf $(TMP_PATH) __pycache__ .pytest_cache
	@find . -name '*.pyc' -delete

venv:
	@virtualenv -p python3 $(VENV_PATH)

setup:
	@pip install -U -e .[dev]

test:
	@pytest

.PHONY: all test clean
