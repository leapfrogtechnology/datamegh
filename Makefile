SHELL :=/bin/bash
CWD := $(PWD)
TMP_PATH := $(CWD)/.tmp
VENV_PATH := $(CWD)/.venv

clean:
	@rm -rf $(TMP_PATH) __pycache__ .pytest_cache
	@find . -name '*.pyc' -delete

venv:
	@virtualenv -p python3 $(VENV_PATH)

venv_setup:
	@pip install -U -e .[dev]

venv_test:
	@pytest -vvv

test:
	@docker build --target=test -t datamegh:test .
	@docker run datamegh:test

.PHONY: all test clean
