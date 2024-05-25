import tkinter as tk
from tkinter import messagebox
from downloader.download import baixar_videos

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text= "Digite as URLs dos vídeos (separadas vírgula): ")
        self.label.pack()

        self.url_entry = tk.Label(self, text="Escolha a qualidade do vídeo:")
        self.quality_label.pack()

        self.quality_var = tk.StringVar(value='highest')
        self.quality_highest = tk.Radiobutton(self, text = "Alta", variable=self.quality_var, value= "highest")
        self.quality_highest.pack()
        self.quality_low = tk.Radiobutton(self, text = "Baixa", variable=self.quality_var, value= "low")
        self.quality_low.pack()

        self.download_button = tk.Button(self, text= "Baixar Vídeos", command=self.start_download)
        self.download_button.pack()

    def start_download(self):
        urls = self.url_entry.get().split(',')
        quality = self.quality_var.get()
        try:
            baixar_videos([url.strip() for url in urls], quality = quality)
            messagebox.showinfo("Sucesso", "Download concluído")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def run_app():
    root = tk.Tk()
    root.title = "NewTube"
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    run_app()            