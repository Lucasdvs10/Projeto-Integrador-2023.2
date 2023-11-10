import tkinter as tk
import os
import tkinter.font as tkFont
import customtkinter as ctk

ctk.set_default_color_theme('green')
ctk.set_appearance_mode('dark')
root = ctk.CTk()
root.title('Criar módulo')
root.geometry('300x200')
root.resizable(False, False)
term14 = ctk.CTkFont(family='Terminal', size=14)
term20 = ctk.CTkFont(family='Terminal', size=20)

def create_module_window():
    a = tk.StringVar()
    l = ctk.CTkLabel(root, textvariable='Digite o nome do módulo: ', font=term14, text='Digite o nome do módulo: ')
    l.place(anchor=tk.CENTER, relx=0.5, rely=0.3)
    e = ctk.CTkEntry(root, textvariable=a, font=term20, width=150)
    e.place(anchor=tk.CENTER, relx=0.5, rely=0.5)
    b = ctk.CTkButton(root, text='Criar', command=lambda: create_module(a.get()), font=term14)
    b.place(anchor=tk.CENTER, relx=0.5, rely=0.7)
    root.mainloop()

def create_module(module_name):
    if module_name != '':
        if not os.path.exists('src/modules/' + module_name):
            os.mkdir('src/modules/' + module_name)
        os.mkdir('src/modules/' + module_name + '/app')
        if not os.path.exists('tests/modules/' + module_name):
            os.mkdir('tests/modules/' + module_name)
        os.mkdir('tests/modules/' + module_name + '/app')
        with open('src/modules/' + module_name + '/__init__.py', 'w+') as f:
            f.write('')
        with open('src/modules/' + module_name + '/app/__init__.py', 'w+') as f:
            f.write('')
        with open('tests/modules/' + module_name + '/__init__.py', 'w+') as f:
            f.write('')
        with open('tests/modules/' + module_name + '/app/__init__.py', 'w+') as f:
            f.write('')
        for file in ['usecase', 'viewmodel', 'controller', 'presenter']:
            with open('src/modules/' + module_name + '/app/' + module_name + '_' + file + '.py', 'w+') as f:
                f.write('')
            with open('tests/modules/' + module_name + '/app/test_' + module_name + '_' + file + '.py', 'w+') as f:
                f.write('')
        root.destroy()
        popup_success(module_name)
    else:
        popup_error()
    
    
def popup_error():
    popup = tk.Tk()
    popup.title('Erro')
    popup.geometry('300x100')
    tk.Label(popup, text='O nome do módulo não pode ser vazio').pack()
    tk.Button(popup, text='Ok', command=popup.destroy).pack()
    popup.mainloop()

def popup_success(module_name):
    popup = ctk.CTk()
    popup.title('Sucesso')
    popup.geometry('300x100')
    l = ctk.CTkLabel(popup, text=f'Módulo {module_name} criado com sucesso!', font=ctk.CTkFont(family='Terminal', size=10))
    l.place(anchor=tk.CENTER, relx=0.5, rely=0.3)
    b = ctk.CTkButton(popup, text='Ok', command=popup.destroy, font=term14)
    b.place(anchor=tk.CENTER, relx=0.5, rely=0.7)
    popup.mainloop()

if __name__ == '__main__':
    create_module_window()