import customtkinter as ctk
from tkinter import filedialog


class PDFViewer(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.label = ctk.CTkLabel(self, text="PDF Viewer", font=ctk.CTkFont(size=24, weight="bold"))
        self.label.pack(pady=30)

        self.open_btn = ctk.CTkButton(self, text="Ouvrir un PDF", command=self.open_pdf)
        self.open_btn.pack(pady=10)

        self.file_label = ctk.CTkLabel(self, text="Aucun fichier sélectionné.")
        self.file_label.pack(pady=10)

    def open_pdf(self):
        path = filedialog.askopenfilename(title="Sélectionner un fichier PDF", filetypes=[("Fichiers PDF", "*.pdf")])
        if path:
            self.file_label.configure(text=f"Fichier sélectionné : {path}")
        else:
            self.file_label.configure(text="Aucun fichier sélectionné.")
