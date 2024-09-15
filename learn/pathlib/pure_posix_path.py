from pathlib import PurePosixPath, PureWindowsPath

print(PurePosixPath('/etc/hosts'))
print(PureWindowsPath('c:/', 'Users', 'Ximénez'))
print(PureWindowsPath('//server/share/file'))
print(PurePosixPath('foo') == PurePosixPath('FOO'))
print(PureWindowsPath('FOO') == PureWindowsPath('foo'))
print(PureWindowsPath('C:') < PureWindowsPath('d:'))
print(PureWindowsPath('foo') == PurePosixPath('foo'))
