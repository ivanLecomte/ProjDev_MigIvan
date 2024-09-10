import tkinter as tk
import market, database
from tkinter import PhotoImage

def open_market():
    market.market_window()

# Fonction pour ouvrir la fenêtre de réglages
def open_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("Réglages")
    settings_window.geometry("200x200")
    tk.Label(settings_window, text="Réglages").pack(pady=20)

# Fonction pour ajouter une commande temporaire
def add_order():
    package_listbox.insert(tk.END, "Nouvelle Commande - En préparation")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Suivi de Colis")
root.configure(bg="#ffffff") #Couleur principal

# Dimensions de la fenêtre
window_width = 650
window_height = 700

# Obtenir la taille de l'écran et calculer la position pour centrer la fenêtre
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# Appliquer la taille et centrer la fenêtre
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Charger l'image (logo)
# Assurez-vous que l'image logo.png se trouve dans le même dossier ou précisez le chemin complet
logo_image = PhotoImage(file="img\FatEx2.png")

# Ajouter un label pour afficher l'image (centrée en haut) 
logo_label = tk.Label(root, image=logo_image, bg="#ffffff")#Couleur logo
logo_label.grid(row=0, column=0, pady=10)

# Configuration de la grille pour structurer la fenêtre
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

# Bouton de réglages (roue dentée)
settings_button = tk.Button(root, text="⚙", command=lambda: open_settings())
settings_button.grid(row=0, column=0, sticky="ne", padx=10, pady=10)

# Zone centrale - Liste des colis
package_listbox = tk.Listbox(root, height=15, width=50, background="#f7ba6f")#Couleur liste
package_listbox.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

# Ajouter un scrollbar à la liste
scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=1, column=0, sticky="nse", padx=(0, 10), pady=10)
package_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=package_listbox.yview)

# Bouton "+" pour ajouter une commande                                                  #Couleur bouton +      #Couleur + du bouton
add_button = tk.Button(root, text="+", font=("Arial", 15), width=6, height=3, background="#f7ba6f", foreground="#000000", command=lambda: open_market())
add_button.grid(row=2, column=0, pady=10)

# Lancer la boucle principale
root.mainloop()
