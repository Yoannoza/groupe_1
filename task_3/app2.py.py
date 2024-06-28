import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import threading
from diffusers import StableDiffusionPipeline
import torch

# Charger le modèle
try:
    mon_modele = "CompVis/stable-diffusion-v1-4"
    generateur = StableDiffusionPipeline.from_pretrained(mon_modele)
    generateur = generateur.to("cuda" if torch.cuda.is_available() else "cpu")
except Exception as e:
    print(f"Erreur lors du chargement du modèle : {e}")
    exit()

# Fonction pour générer l'image
def generer_img():
    # Récupérer la description de la zone de texte
    prompt = text_taper.get("1.0", tk.END).strip()
    
    if not prompt:
        label_resultat.config(text="Veuillez entrer une description.")
        return
    
    # Activer le spinner
    spinner.grid(row=2, column=0, columnspan=2)
    label_resultat.config(text="Génération de l'image en cours...")

    # Fonction de génération d'image
    def generer():
        try:
            # Générer l'image
            image = generateur(prompt).images[0]
            image.save("image_generer.png")
            
            # Charger et afficher l'image
            img = Image.open("image_generer.png")
            img = img.resize((256, 256), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)
            
            # Mettre à jour l'interface graphique
            def mise_a_jour_gui():
                spinner.grid_remove()
                image_label.config(image=img_tk)
                image_label.image = img_tk
                label_resultat.config(text=f"Image générée pour : '{prompt}'")
            
            debut.after(0, mise_a_jour_gui)
        except Exception as e:
            debut.after(0, lambda: label_resultat.config(text=f"Erreur : {str(e)}"))
            spinner.grid_remove()
    
    # Exécuter la génération d'image
    threading.Thread(target=generer).start()

# Configuration de l'application principale
debut = tk.Tk()
debut.title("Générateur d'images avec Hugging Face")
debut.geometry("500x500")

# Zone de texte pour la description
text_taper = tk.Text(debut, height=4, width=40)
text_taper.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Bouton pour générer l'image
bouton_generer = tk.Button(debut, text="Générer", command=generer_img)
bouton_generer.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Indicateur de chargement (spinner)
spinner = ttk.Progressbar(debut, mode="indeterminate")

# Zone d'affichage pour l'image générée
image_label = tk.Label(debut)
image_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Label pour afficher des messages
label_resultat = tk.Label(debut, text="", wraplength=300)
label_resultat.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Lancer l'application
debut.mainloop()
