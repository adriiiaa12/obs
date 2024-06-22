import tkinter as tk
from tkinter import filedialog, messagebox

class AcademyApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('400x250')
        
        try:
            self.root.iconbitmap('assets/logo_2.ico')
        except Exception as e:
            print(f"Error setting icon: {e}")
            
        self.root.title("Añadir Cuerpo")

        self.file_path = ""

        self.frame1 = tk.Frame(root)
        self.frame1.pack(padx=10, pady=10)

        self.label = tk.Label(self.frame1, text="Selecciona el archivo HTML")
        self.label.pack()

        self.select_file_btn = tk.Button(self.frame1, text="Seleccionar Archivo", command=self.select_file)
        self.select_file_btn.pack()

    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("HTML files", "*.html")])
        if self.file_path:
            self.frame1.pack_forget()
            self.open_academy_entry()

    def open_academy_entry(self):
        self.frame2 = tk.Frame(self.root)
        self.frame2.pack(padx=10, pady=10)

        tk.Label(self.frame2, text="Título").grid(row=0, column=0, padx=5, pady=5)
        self.title_entry = tk.Entry(self.frame2)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame2, text="SubTítulo").grid(row=1, column=0, padx=5, pady=5)
        self.subtitle_entry = tk.Entry(self.frame2)
        self.subtitle_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame2, text="Descripción").grid(row=2, column=0, padx=5, pady=5)
        self.description_entry = tk.Entry(self.frame2)
        self.description_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.frame2, text="Nombre Icono").grid(row=3, column=0, padx=5, pady=5)
        self.icon_entry = tk.Entry(self.frame2)
        self.icon_entry.grid(row=3, column=1, padx=5, pady=5)

        self.save_btn = tk.Button(self.frame2, text="Guardar Cuerpo", command=self.save_academy)
        self.save_btn.grid(row=4, columnspan=2, pady=10)

    def save_academy(self):
        title = self.title_entry.get()
        subtitle = self.subtitle_entry.get()
        description = self.description_entry.get()
        icon = self.icon_entry.get()

        if not title or not subtitle or not description or not icon:
            messagebox.showerror("Error", "Debes rellenar todos los huecos.")
            return

        academy_item = f"""
                <div class="cuerpo card">
                    <div class="name">
                        <img src="../assets/{icon}">
                        <h3>{title}</h3>
                    </div>
                    <div class="description">
                        <h4>{subtitle}</h4>
                        <p>{description}</p>
                    </div>
                </div>
        """

        self.append_academy_to_file(academy_item)

    def append_academy_to_file(self, academy_item):
        try:
            content = None
            try:
                with open(self.file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
            except UnicodeDecodeError:
                with open(self.file_path, 'r', encoding='latin-1') as file:
                    content = file.read()

            insertion_point = content.find("<!-- NUEVO CUERPO -->")
            if insertion_point == -1:
                messagebox.showerror("Error", "No se encontró '<!-- NUEVO CUERPO -->'")
                return

            content_before = content[:insertion_point]
            content_after = content[insertion_point:]

            updated_content = content_before + academy_item + content_after

            with open(self.file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)

            messagebox.showinfo("Éxito", "Cuerpo agregado correctamente")
            self.root.quit()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el nuevo cuerpo: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AcademyApp(root)
    root.mainloop()