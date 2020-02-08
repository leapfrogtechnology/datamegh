# STAGE: base
# -----------
# The base image (intermediate).
FROM laudio/pyodbc:1.0.32 AS base

WORKDIR /source

COPY ["setup.py", "README.md", "./"]
COPY ["datamegh", "./datamegh"]

RUN pip install .

# STAGE: main
# -----------
# The main image that is published.
FROM base AS main

# STAGE: test
# -----------
# Image used for running tests.
FROM base AS test
RUN pip install .[dev]

COPY ["tests", "./"]

CMD pytest -vvv
