import send2trash
from pathlib import Path

cwd = Path.cwd()
subfolder = 'tmp'

test_file = cwd / subfolder / 'test1.txt'

file = open(test_file, 'a')
file.write('Testing file writing')
file.close()
send2trash.send2trash(test_file)