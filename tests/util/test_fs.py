''' Tests for the fs util. '''

from mock import patch, mock_open
from datamegh.util import fs


@patch('os.path.exists')
def test_exists(result):
    ''' Test fs.exists() works. '''
    filename = 'somefile'
    fs.exists(filename)
    result.assert_called_with(filename)


def test_read():
    ''' Test fs.read() works. '''
    filename = 'somefile'
    data = 'somedata'

    with patch('builtins.open', mock_open(read_data=data)) as mock_file:
        assert fs.read(filename) == data
        mock_file.assert_called_with(filename, 'r')


def test_write():
    ''' Test fs.write() works. '''
    filename = 'somefile'
    data = 'somedata'
    m = mock_open()

    with patch('builtins.open', m) as mock_file:
        fs.write(filename, data)
        mock_file.assert_called_with(filename, 'w')
        m().write.assert_called_with(data)
