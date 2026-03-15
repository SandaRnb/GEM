import customtkinter as ctk
from tkinter import filedialog


class MP4Player(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.label = ctk.CTkLabel(self, text="MP4 Player", font=ctk.CTkFont(size=24, weight="bold"))
        self.label.pack(pady=30)

        self.open_btn = ctk.CTkButton(self, text="Ouvrir un MP4", command=self.open_mp4)
        self.open_btn.pack(pady=10)

        self.status_label = ctk.CTkLabel(self, text="Aucun fichier sélectionné.")
        self.status_label.pack(pady=10)

        self.play_btn = ctk.CTkButton(self, text="Play (placeholder)", command=self.play)
        self.play_btn.pack(pady=5)

    def open_mp4(self):
        path = filedialog.askopenfilename(title="Sélectionner un fichier MP4", filetypes=[("Fichiers MP4", "*.mp4")])
        if path:
            self.status_label.configure(text=f"Fichier sélectionné : {path}")
            self.current_file = path
        else:
            self.status_label.configure(text="Aucun fichier sélectionné.")
            self.current_file = None

    def play(self):
        if hasattr(self, 'current_file') and self.current_file:
            self.status_label.configure(text=f"Lecture : {self.current_file} (simulée)")
        else:
            self.status_label.configure(text="Pas de fichier à lire.")
