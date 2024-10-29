import tkinter as tk
import market, database
from tkinter import PhotoImage

def open_market():
    market.market_window()

# Function to open the settings window
def open_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")
    settings_window.geometry("200x200")
    tk.Label(settings_window, text="Settings").pack(pady=20)

# Function to load orders from the database
# Function to load orders from the database
def load_orders():
    orders = database.get_orders()
    package_listbox.delete(0, tk.END)  # Effacer l'ancienne liste

    for order in orders:
        package_listbox.insert(tk.END, f"Order {order['id']} - Status: {order['delivery_status']}")


# Create the main window
root = tk.Tk()
root.title("Package Tracking")
root.configure(bg="#ffffff")  # Main color

# Window dimensions
window_width = 650
window_height = 700

# Get screen size and calculate position to center the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# Apply size and center the window
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Load image (logo)
logo_image = PhotoImage(file="img/fraudex.png")

# Add a label to display the image (centered at the top)
logo_label = tk.Label(root, image=logo_image, bg="#ffffff")
logo_label.grid(row=0, column=0, pady=10)

# Grid configuration to structure the window
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

# Settings button (gear icon)
settings_button = tk.Button(root, text="⚙", command=open_settings)
settings_button.grid(row=0, column=0, sticky="ne", padx=10, pady=10)

# Central area - List of orders
package_listbox = tk.Listbox(root, height=15, width=50, background="#f7ba6f")
package_listbox.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

# Add a scrollbar to the list
scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=1, column=0, sticky="nse", padx=(0, 10), pady=10)
package_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=package_listbox.yview)

# "+" button to add an order
add_button = tk.Button(root, text="+", font=("Arial", 15), width=6, height=3,
                       background="#f7ba6f", foreground="#000000", command=open_market)
add_button.grid(row=2, column=0, pady=10)

# Load orders on startup
load_orders()

# Refresh the list of orders periodically (every 5 seconds)
def refresh_orders():
    load_orders()
    root.after(5000, refresh_orders)

refresh_orders()

# Start the main loop
root.mainloop()
