# datamegh
[![Travis (.org)](https://img.shields.io/travis/leapfrogtechnology/datamegh?style=flat-square&branch=master)](https://travis-ci.org/leapfrogtechnology/datamegh)  

Datamegh - A Cloud-native framework for Data Engineering projects.

If you're unfamiliar with what cloud-native means? Read it [here](https://github.com/cncf/toc/blob/master/DEFINITION.md).

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
Make sure to run following commands:
```bash
$ make format
$ make check
$ make test
```

## License

Licensed under [The MIT License](LICENSE).
