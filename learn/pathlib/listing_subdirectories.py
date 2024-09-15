from pathlib import Path

p = Path('.')
subdir = [x for x in p.iterdir() if x.is_dir()]
file = [x for x in p.iterdir() if x.is_file()]
print(f'Totally: {len(subdir) + len(file)}\nSubdir=>{subdir} \nFile=> {file}')
#
print(list(p.glob('**/*.py')))
