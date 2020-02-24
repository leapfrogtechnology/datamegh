SHELL :=/bin/bash
CWD := $(PWD)
TMP_PATH := $(CWD)/.tmp
VENV_PATH := $(CWD)/.venv
TRAVIS_BRANCH := master

last_tag := $(shell git tag --sort=-creatordate | head -n 1)
new_tag := $(shell semver bump patch "${last_tag}")
timestamp := $(date -u +%Y%m%d%H%M%S)
# The new version is tagged as pre-release for master. Once we are good to go for production, remove the -prerelease suffix
new_version := $(shell if [ "${TRAVIS_BRANCH}" = "master" ]; then echo "${new_tag}-prerelease"; else echo "${new_tag}-${TRAVIS_BRANCH}.${timestamp}"; fi)

clean:
	@rm -rf $(TMP_PATH) __pycache__ .pytest_cache
	@find . -name '*.pyc' -delete

venv:
	@virtualenv -p python3 $(VENV_PATH)

setup:
	@pip install -U -e .[dev]
	@pre-commit install

venv_test:
	@pytest -vvv

build:
	@docker build --no-cache --target=test -t datamegh:test .
	@docker build --no-cache --target=main -t datamegh .

test:
	@docker build --target=test -t datamegh:test .
	@docker run datamegh:test

.PHONY: all test clean

tag:
	@echo "Bump version :- $(last_tag) -> $(new_version)"
	@sed -i "s/version.*=.*/version = '$(new_version)'/" datamegh/__init__.py && \
		git add datamegh/__init__.py && \
		git commit -m "Update $(last_tag) to $(new_version)" -m "[skip ci]" && \
		git remote add origin-pusher https://${GITHUB_OAUTH_TOKEN}@github.com/leapfrogtechnology/datamegh.git || true && \
		git push origin-pusher ${TRAVIS_BRANCH} --tags

