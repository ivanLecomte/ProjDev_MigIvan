import tkinter as tk

# Créer la fenêtre principale
root = tk.Tk()
root.title("Suivi de Colis")

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

# Configuration de la grille pour structurer la fenêtre
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

# Bouton de réglages (roue dentée)
settings_button = tk.Button(root, text="⚙", command=lambda: open_settings())
settings_button.grid(row=0, column=0, sticky="ne", padx=10, pady=10)

# Zone centrale - Liste des colis
package_listbox = tk.Listbox(root, height=15, width=50)
package_listbox.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

# Ajouter un scrollbar à la liste
scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=1, column=0, sticky="nse", padx=(0, 10), pady=10)
package_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=package_listbox.yview)

# Bouton "+" pour ajouter une commande
add_button = tk.Button(root, text="+", font=("Arial", 15), width=6, height= 3, background="black", foreground= "yellow", command=lambda: add_order())
add_button.grid(row=2, column=0, pady=10)

# Fonction pour ouvrir la fenêtre de réglages
def open_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("Réglages")
    settings_window.geometry("200x200")
    tk.Label(settings_window, text="Réglages").pack(pady=20)

# Fonction pour ajouter une commande temporaire
def add_order():
    package_listbox.insert(tk.END, "Nouvelle Commande - En préparation")

# Lancer la boucle principale
root.mainloop()
