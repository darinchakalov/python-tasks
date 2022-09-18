from pathlib import Path
import os

current_folder = Path('C:/Users/volat/Desktop/Python/Training')
cwd = Path.cwd()

subfolder = Path('tmp')

print(str(cwd))
print(str(cwd / subfolder))

current_file = (current_folder / subfolder / 'test1.txt')
print(current_file.suffix.upper())