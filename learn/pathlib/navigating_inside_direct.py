from pathlib import Path

p = Path('/etc')
q = p / 'init.d' / 'whoopsie'
print(q)
print(q.resolve())
print(q.exists())
print(q.is_dir())
with q.open() as f:
    print(f.readline())

