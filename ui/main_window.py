import customtkinter as ctk
import tkinter.messagebox as messagebox
from ui.pdf_viewer import PDFViewer
from ui.mp3_player import MP3Player
from ui.mp4_player import MP4Player


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("GEM")
        self.geometry("900x620")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.sidebar = ctk.CTkFrame(self, width=200)
        self.sidebar.pack(side="left", fill="y")

        self.content = ctk.CTkFrame(self)
        self.content.pack(side="right", fill="both", expand=True)

        self.current_view = None

        self.btn_pdf = ctk.CTkButton(self.sidebar, text="PDF Viewer", command=lambda: self._switch_view(PDFViewer))
        self.btn_pdf.pack(pady=10, padx=10, fill="x")

        self.btn_mp3 = ctk.CTkButton(self.sidebar, text="MP3 Player", command=lambda: self._switch_view(MP3Player))
        self.btn_mp3.pack(pady=10, padx=10, fill="x")

        self.btn_mp4 = ctk.CTkButton(self.sidebar, text="MP4 Player", command=lambda: self._switch_view(MP4Player))
        self.btn_mp4.pack(pady=10, padx=10, fill="x")

        self._switch_view(PDFViewer)

    def on_close(self):
        if messagebox.askyesno("Quitter", "Voulez-vous vraiment quitter GEM ?"):
            self.destroy()

    def _switch_view(self, view_class):
        if self.current_view is not None:
            self.current_view.destroy()

        self.current_view = view_class(self.content)
        self.current_view.pack(fill="both", expand=True)
