import os


def test_help_command():
    exit_status = os.system('page-loader -h')
    assert exit_status == 0


def read_file(path):
    with open(path, 'r') as file:
        return file.read()
