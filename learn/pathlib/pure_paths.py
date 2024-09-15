from pathlib import Path, PurePath, PureWindowsPath

print(PurePath())
show = PurePath('foo', 'some/path', 'bar')
print(show)
show2 = PurePath(Path('foo'), Path('bar'))
print(show2)
#
print(PurePath('/etc', '/usr', 'lib64'))
print(PureWindowsPath('c:/Windows', '/Program Files'))
print(PurePath('foo/../bar'))
