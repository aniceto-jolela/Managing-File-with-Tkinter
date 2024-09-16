from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os


def open_file_dialog():
    global file_path
    file_path = filedialog.askopenfilename(
        title='Select a file',
        filetypes=[('Text files', '*.txt *.mp4 *.mp3'), ('All files', '*.*')]
    )
    os.chdir(os.path.split(file_path)[0])
    if file_path:
        messagebox.showinfo('Selected', f'File path:\n{file_path}')
        lb_path_v.set(file_path)
        et_default['state'] = 'enable'
        btn['state'] = 'enable'
        all_listbox()


def all_listbox():
    if lb_path_v.get():
        if int(rd_state.get()) == 1:
            ls.delete(0, END)
            path_dir = os.path.split(file_path)[0]
            for count, file in enumerate(os.listdir(path_dir)):
                ls.insert(count, file)
        else:
            ls.delete(0, END)
            ls.insert(0, os.path.basename(file_path))
    else:
        messagebox.showerror('Error', 'Empty list!')


def clear_entry():
    messagebox.showinfo('Success', 'Successful file rename!')
    name.set('')
    lb_path_v.set('')
    ls.delete(0, END)
    et_default['state'] = 'disable'
    btn['state'] = 'disable'


def file_rename():
    if name.get().strip():
        path_dir = os.path.split(file_path)[0]
        old_file = os.path.split(file_path)[1]
        ext = os.path.splitext(file_path)[1]
        if int(rd_state.get()) == 1:
            for count, file in enumerate(os.listdir(path_dir)):
                if os.path.isfile(file):
                    ext_file = os.path.splitext(file)[1]
                    name_file = name.get() + ' - ' + str(count)
                    new_file_such = f'{name_file}{ext_file}'
                    os.rename(file, new_file_such)
            clear_entry()
        else:
            new_file = f'{name.get()}{ext}'
            os.rename(old_file, new_file)
            clear_entry()
    else:
        messagebox.showwarning('Empty', 'Entry empty')


root = Tk()
root.title('File rename')
frame = ttk.Frame(root)
name = StringVar()
lb_path_v = StringVar()
rd_state = StringVar(value='0')
lb_path = ttk.Label(frame, text='path...', foreground='green')
btn_path = ttk.Button(frame, text='open', command=open_file_dialog)
ls = Listbox(frame, yscrollcommand='vertical', activestyle='dotbox')
rb_1 = ttk.Radiobutton(frame, text='Only', variable=rd_state, value='0', command=all_listbox)
rb_2 = ttk.Radiobutton(frame, text='All', variable=rd_state, value='1', command=all_listbox)

lb_default = ttk.Label(frame, text='What name do you want to use for file(s)?')
et_default = ttk.Entry(frame, textvariable=name, state='disable')
btn = ttk.Button(frame, text='Rename', state='disable', command=file_rename)


if __name__ == '__main__':
    frame.grid(padx=20, pady=20, column=50, row=20)
    lb_path.grid(column=2, row=0)
    btn_path.grid(column=3, row=0)
    rb_2.grid(column=1, row=1)
    rb_1.grid(row=1)
    ls.grid(pady=10, column=3, row=1)

    lb_path['textvariable'] = lb_path_v
    lb_default.grid(pady=10, column=2, row=2)
    et_default.grid(pady=10, column=2, row=3)
    btn.grid(column=2, row=4)
    root.mainloop()