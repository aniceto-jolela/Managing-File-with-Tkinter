from pathlib import PurePath, PureWindowsPath
import os

p = PurePath('/etc')
q = p / 'init.d' / 'apache2'
print(q)
print(os.fspath(p))
p1 = PureWindowsPath('c:/Program Files')
print(str(p1))
print(bytes(p))