SHELL :=/bin/bash
CWD := $(PWD)
TMP_PATH := $(CWD)/.tmp
VENV_PATH := $(CWD)/.venv

last_tag := $(shell git tag --sort=-creatordate | head -n 1)
new_tag := $(shell semver bump patch "${last_tag}")
timestamp := $(date -u +%Y%m%d%H%M%S)
# The new version is tagged as pre-release for master. Once we are good to go for production, remove the -prerelease suffix
new_version := $(shell if [ "${TRAVIS_BRANCH}" = "master" ]; then echo "${new_tag}-alpha.${timestamp}"; else echo "${new_tag}-${TRAVIS_BRANCH}.${timestamp}"; fi)
COLOR=\x1b[36m
NO_COLOR=\x1b[m]

.PHONY: clean
## Clean the pycache folder and pyc files.
clean:
	@rm -rf $(TMP_PATH) __pycache__ .pytest_cache
	@find . -name '*.pyc' -delete

.PHONY: venv
## Create virtual environment for python.
venv:
	@virtualenv -p python3 $(VENV_PATH)

.PHONY: setup
## Setup the application by installing the packages.
setup:
	@pip install -U -e .[dev]
	@npm install

.PHONY: venv_test
## Test for virtual environment.
venv_test:
	@pytest -vvv

.PHONY: build
## Build the docker container.
build:
	@docker build --no-cache --target=test -t datamegh:test .
	@docker build --no-cache --target=main -t datamegh .

.PHONY: test
## Test application in docker container.
test:
	@docker build --target=test -t datamegh:test .
	@docker run datamegh:test

.PHONY: all test clean

## Update Tag and push to github 
tag:
	echo "Bump version :- $(last_tag) -> $(new_version)"
	git config --global user.name "leapfrog-bot"
	git config --global user.email "devops@lftechnology.com"
	git remote add origin-pusher https://${GITHUB_OAUTH_TOKEN}@github.com/leapfrogtechnology/datamegh.git
	sed -i'' "s/version.*=.*/version = '$(new_version)'/" datamegh/__init__.py
	git add datamegh/__init__.py
	git commit -m "Update $(last_tag) to $(new_version)" -m "[skip ci]"
	git push origin-pusher ${TRAVIS_BRANCH}
	git tag $(new_version)

	
.PHONY: format
## Format the code.
format:
	@black .

.PHONY: check
## Check the code.
check:
	@black --check --diff .
	@npm run typecheck

.DEFAULT_GOAL := help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: help
## Show this help message
help:
	@echo -e "Usage:\n\tmake <command>\n"
	@echo "$$(tput bold)Available commands:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
