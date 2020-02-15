# datamegh
[![Build Status](https://travis-ci.org/leapfrogtechnology/datamegh.svg?branch=master)](https://travis-ci.org/leapfrogtechnology/datamegh)  

Datamegh - Engineered for the cloud.

## Development

#### Setting up the codebase

1. Clone the repository.

```bash
$ git clone git@github.com:leapfrogtechnology/datamegh.git
$ cd datamegh
```

2. Setup a virtualenv.

```bash
$ make venv
```

3. Activate the virtualenv.

```bash
$ source .venv/bin/activate
$ make setup
```

#### Running tests

```bash
$ make test
```

Note: This ensures all the dependencies are complete since tests are run in an isolated container.

## Contributing

Feel free to send pull requests.

## License

Licensed under [The MIT License](LICENSE).
