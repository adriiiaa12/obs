import tkinter as tk
from tkinter import filedialog, messagebox
import json

class NewsApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('400x300')
        
        try:
            self.root.iconbitmap('assets/logo_2.ico')
        except Exception as e:
            print(f"Error setting icon: {e}")
            
        self.root.title("Añadir Noticias")

        self.file_path = ""

        self.frame1 = tk.Frame(root)
        self.frame1.pack(padx=10, pady=10)

        self.label = tk.Label(self.frame1, text="Seleciona el archivo de noticias")
        self.label.pack()

        self.select_file_btn = tk.Button(self.frame1, text="Seleccionar Archivo", command=self.select_file)
        self.select_file_btn.pack()

    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("JavaScript files", "*.js")])
        if self.file_path:
            self.frame1.pack_forget()
            self.open_news_entry()

    def open_news_entry(self):
        self.frame2 = tk.Frame(self.root)
        self.frame2.pack(padx=10, pady=10)

        tk.Label(self.frame2, text="Título").grid(row=0, column=0, padx=5, pady=5)
        self.title_entry = tk.Entry(self.frame2)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame2, text="Descripción").grid(row=1, column=0, padx=5, pady=5)
        self.description_entry = tk.Entry(self.frame2)
        self.description_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame2, text="Fecha").grid(row=2, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(self.frame2)
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.frame2, text="Nombre de la Foto").grid(row=3, column=0, padx=5, pady=5)
        self.photo_entry = tk.Entry(self.frame2)
        self.photo_entry.grid(row=3, column=1, padx=5, pady=5)

        self.save_btn = tk.Button(self.frame2, text="Guardar Noticia", command=self.save_news)
        self.save_btn.grid(row=4, columnspan=2, pady=10)

    def save_news(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        date = self.date_entry.get()
        photo = self.photo_entry.get()

        if not title or not description or not date or not photo:
            messagebox.showerror("Error", "Debes rellenar todos los huecos.")
            return

        news_item = {
            "title": title,
            "description": description,
            "date": date,
            "imagePath": f"images/{photo}"
        }

        self.append_news_to_file(news_item)

    def append_news_to_file(self, news_item):
        try:
            content = None
            try:
                with open(self.file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
            except UnicodeDecodeError:
                with open(self.file_path, 'r', encoding='latin-1') as file:
                    content = file.read()
                    
            insertion_point = content.find("// NOTICIAS")

            insertion_point += len("// NOTICIAS")
            
            content_before = content[:insertion_point]
            content_after = content[insertion_point:]

            new_news_js = f"""\n        {{
                title: '{news_item["title"]}',
                description: '{news_item["description"]}',
                date: '{news_item["date"]}',
                imagePath: '{news_item["imagePath"]}'
            }},\n"""

            updated_content = content_before + new_news_js + content_after

            with open(self.file_path, 'w') as file:
                file.write(updated_content)

            messagebox.showinfo("Éxito", "Noticia agregada correctamente")
            self.root.quit()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar la noticia: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NewsApp(root)
    root.mainloop()