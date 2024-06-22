import tkinter as tk
import subprocess
from tkinter import font

def run_news_script():
    subprocess.Popen(['python', 'news.py'])

def run_academies_script():
    subprocess.Popen(['python', 'academies.py'])

def run_bodies_script():
    subprocess.Popen(['python', 'bodies.py'])

def run_main():
    root = tk.Tk()
    root.geometry('400x250')
    try:
        root.iconbitmap('assets/logo_2.ico')
    except Exception as e:
        print(f"Error setting icon: {e}")
    root.title('Añadir Información - Ejército De Honor')
    
    main_label = tk.Label(root, text='¿QUÉ QUIERES AÑADIR A LA WEB?', font=('Helvetica', 16, 'bold'))
    main_label.pack(pady=20)
    
    button_width = 20
    
    button1 = tk.Button(root, text='Añadir Noticia', bg='lightblue', font=('Helvetica', 12), width=button_width, command=run_news_script)
    button1.pack(pady=5)
    
    button2 = tk.Button(root, text='Añadir Academia', bg='lightgreen', font=('Helvetica', 12), width=button_width, command=run_academies_script)
    button2.pack(pady=5)
    
    button3 = tk.Button(root, text='Añadir Cuerpo', bg='lightcoral', font=('Helvetica', 12), width=button_width, command=run_bodies_script)
    button3.pack(pady=5)
    
    root.mainloop()
    
if __name__ == '__main__':
    run_main()