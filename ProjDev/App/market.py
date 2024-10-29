import tkinter as tk
from tkinter import ttk
import database  # Importez votre module de base de données
from datetime import datetime

# Fonction pour ajouter une commande
def ajouter_au_panier(firstname, lastname, country, city, cp, street, street_nb):
    # Ajout du client à la base de données et récupération de son ID
    client_info_id = database.add_client(firstname, lastname, country, city, cp, street, street_nb)
    
    deliveries_id = 1   # Supposons une livraison avec l'ID 1
    packages_id = 1     # Supposons un package avec l'ID 1
    price_total = 10.00  # Prix total par défaut (vous pouvez l'ajuster selon vos besoins)
    nb_product = 1      # Quantité du produit
    tracking_order = f"TRACK-{client_info_id}-{deliveries_id}-{packages_id}" 
    
    date = datetime.now()
    order_id = database.add_order(
        client_info_id, deliveries_id, packages_id, date, price_total, nb_product, tracking_order
    )
    print(f"Commande ajoutée avec le tracking {tracking_order} et ID {order_id}")

# Créer la fenêtre secondaire, de livraison
def order_window():
    fenetre_livraison = tk.Toplevel()
    fenetre_livraison.title("Informations de livraison - commande")
    fenetre_livraison.geometry("400x500")  # Dimensions ajustées pour une meilleure visibilité

    # Ajoutez des informations de base pour la livraison
    ttk.Label(fenetre_livraison, text="Informations de livraison", font=("Arial", 14, "bold")).grid(row=0, column=0, pady=10, padx=20)

    # Champs de saisie pour les informations de livraison
    labels = ["Prénom:", "Nom:", "Pays:", "Ville:", "Code Postal:", "Rue:", "Numéro de rue:"]
    entries = []

    for i, label in enumerate(labels):
        ttk.Label(fenetre_livraison, text=label).grid(row=i + 1, column=0, sticky="w", padx=10, pady=5)
        entry = ttk.Entry(fenetre_livraison, width=30)
        entry.grid(row=i + 1, column=1, padx=10, pady=5)  # Placer l'entrée à côté de l'étiquette
        entries.append(entry)

    # Fonction pour confirmer la commande
    def confirm_order():
        # Récupérer les données des champs
        firstname = entries[0].get()
        lastname = entries[1].get()
        country = entries[2].get()
        city = entries[3].get()
        cp = entries[4].get()
        street = entries[5].get()
        street_nb = entries[6].get()

        # Appeler la fonction pour ajouter la commande
        ajouter_au_panier(firstname, lastname, country, city, cp, street, street_nb)
        fenetre_livraison.destroy()  # Fermer la fenêtre après la confirmation

    # Ajout du bouton de confirmation
    ttk.Button(fenetre_livraison, text="Confirmer", command=confirm_order).grid(row=len(labels) + 1, column=0, pady=20)  # Bouton pour confirmer

# Créer la fenêtre principale
def market_window():
    fenetre = tk.Toplevel()
    fenetre.title("Site de Produits - KariMarket")

    # Créer un cadre pour contenir les informations sur les commandes
    cadre_commande = ttk.Frame(fenetre, padding="10")
    cadre_commande.grid(row=0, column=0)

    commandes = [
        {'tracking_order': 'PS5 Pro', 'client_info_id': 1, 'price_total': 299},
        {'tracking_order': 'iPhone 17 Pro Max S Plus XS', 'client_info_id': 1, 'price_total': 999},
    ]
    
    for i, commande in enumerate(commandes):
        cadre = ttk.Frame(cadre_commande, borderwidth=2, relief="groove", padding="10")
        cadre.grid(row=i, column=0, padx=10, pady=10)
    
        tracking_label = ttk.Label(cadre, text=f"Produit: {commande['tracking_order']}", font=("Arial", 14, "bold"))
        tracking_label.pack(anchor="w")
    
        price_label = ttk.Label(cadre, text=f"Total: {commande['price_total']} .-", font=("Arial", 12, "bold"))
        price_label.pack(anchor="w")
    
        bouton_ajouter = ttk.Button(cadre, text="Commander", command=order_window)
        bouton_ajouter.pack(anchor="e", pady=(10, 0))
