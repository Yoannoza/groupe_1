import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from transformers import pipeline
import torch

#disponibilité du cpu ou cdu pour l'accélération matérielle
pilote = "cpu" if torch.cpu.is_available() else "cdu"

#création de la fenêtre tkinter
debut = tk.Tk()
debut.title("Générateur d'images")
debut.geometry("600x400")

#zone de texte de saisie
zone_de_texte = tk.Label(debut, text="Entrez la description:")
zone_de_texte.pack(pady=10)

description_text = tk.Text(debut, height=5, width=50)
description_text.pack(pady=5)
