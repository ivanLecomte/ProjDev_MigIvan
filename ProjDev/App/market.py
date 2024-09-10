import tkinter as tk
from tkinter import ttk

# Fonction pour ajouter un produit au panier
def ajouter_au_panier(produit):
    print(f"{produit} ajouté au panier")


# Créer la fenêtre principale
def market_window():
    fenetre = tk.Tk()
    fenetre.title("Site de Produits - Digitech")
    # Créer un cadre pour contenir les produits
    cadre_produits = ttk.Frame(fenetre, padding="10")
    cadre_produits.grid(row=0, column=0)

    # Exemple de produits
    produits = [
        {"nom": "Produit 1", "description": "Description du produit 1", "prix": "207567€"},
        {"nom": "Produit 2", "description": "Description du produit 2", "prix": "3535456€"},
        {"nom": "Produit 3", "description": "Description du produit 3", "prix": "69€"},
    ]

    # Ajouter les produits au cadre
    for i, produit in enumerate(produits):
        cadre = ttk.Frame(cadre_produits, borderwidth=2, relief="groove", padding="10")
        cadre.grid(row=i // 2, column=i % 2, padx=10, pady=10)

        nom_label = ttk.Label(cadre, text=produit["nom"], font=("Arial", 14, "bold"))
        nom_label.pack(anchor="w")

        desc_label = ttk.Label(cadre, text=produit["description"], wraplength=200)
        desc_label.pack(anchor="w", pady=(5, 10))

        prix_label = ttk.Label(cadre, text=produit["prix"], font=("Arial", 12, "bold"))
        prix_label.pack(anchor="w")

        bouton_ajouter = ttk.Button(cadre, text="Ajouter au panier", command=lambda p=produit["nom"]: ajouter_au_panier(p))
        bouton_ajouter.pack(anchor="e", pady=(10, 0))

    # Lancer la boucle principale de l'interface
    fenetre.mainloop()