from pathlib import PurePath, PureWindowsPath, PurePosixPath

p = PurePath('/usr/bin/python3')
p1 = PureWindowsPath('c:/Progran Files/PSF')
print(p.parts)
print(p1.parts)
print(PureWindowsPath('c:/Program Files/').drive)
print(PureWindowsPath('c:/Program Files/').root)
print(PurePosixPath('////etc'))