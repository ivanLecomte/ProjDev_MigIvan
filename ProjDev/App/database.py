import mysql.connector
from datetime import datetime

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",       # Modifier selon vos paramètres
        user="root",            # Modifier selon vos paramètres
        password="Pa$$w0rd",    # Modifier selon vos paramètres
        database="ProjPy"
    )

# Fonction pour ajouter une commande
def add_order(client_info_id, deliveries_id, packages_id, date, price_total, nb_product, tracking_order):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Convertir la date en format approprié pour MySQL
    date = date.strftime('%Y-%m-%d %H:%M:%S')  # Format datetime
    
    cursor.execute("""INSERT INTO orders (client_info_id, deliveries_id, Packages_id, date, price_total, nb_product, tracking_order)
                      VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                   (client_info_id, deliveries_id, packages_id, date, price_total, nb_product, tracking_order))
    
    connection.commit()
    order_id = cursor.lastrowid  # Obtenez l'ID de la commande ajoutée
    cursor.close()
    connection.close()
    
    return order_id  # Retournez l'ID de la commande

# Fonction pour ajouter un client
def add_client(firstname, lastname, country, city, cp, street, street_nb):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    add_client_query = """
    INSERT INTO customers (firstname, lastname, country, city, cp, street, street_nb)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    data = (firstname, lastname, country, city, cp, street, street_nb)
    cursor.execute(add_client_query, data)
    connection.commit()
    
    client_id = cursor.lastrowid
    
    cursor.close()
    connection.close()
    return client_id

# Fonction pour récupérer les commandes
def get_orders():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Jointure entre les tables orders, deliveries et deliveries_status
    cursor.execute("""
        SELECT o.*, ds.statut_type AS delivery_status
        FROM orders o
        JOIN deliveries d ON o.deliveries_id = d.id
        JOIN deliveries_status ds ON d.delivery_status_id = ds.id
    """)  # Récupérer toutes les commandes avec leur statut de livraison
    orders = cursor.fetchall()

    cursor.close()
    connection.close()
    return orders




# Fonction pour récupérer la liste des produits
def get_products():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT id, name, description, price FROM product")
    products = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return products
