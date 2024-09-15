import os

#/home/aniceto/PycharmProjects/AI/3
os.chdir('/home/aniceto/PycharmProjects/AI/Teste')
print(f'Dir actually: {os.getcwd()}')

default = input('Which name do you want to use for files?')
for cont, arq in enumerate(os.listdir()):
    if os.path.isfile(arq):
        name_file, ext_file = os.path.splitext(arq)
        name_file = default + ' - ' + str(cont)

        new_file = f'{name_file}{ext_file}'
        os.rename(arq, new_file)

print(f'\nChange files')

# Path with file -> n = os.path.split(file_path)
# Only path -> n = [0]
# Only file with extension -> n = [1]

# Path with extension -> os.path.splitext(file_path)
# Only path -> n = [0]
# Only station -> n = [1]
