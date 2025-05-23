import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Gebruikersconfiguratie
app_users = {
    'root': 'Welcome01',
    'user': 'Welcome01'
}

# Acties
def execute_action(action):
    selected_user = user_var.get()
    name = name_var.get().strip()
    email = email_var.get().strip()

    if selected_user not in app_users:
        messagebox.showerror("Fout", "Ongeldige gebruiker.")
        return

    if not name or not email:
        messagebox.showerror("Fout", "Naam en e-mailadres zijn verplicht.")
        return

    try:
        conn = mysql.connector.connect(
            host='localhost',
            user=selected_user,
            password=app_users[selected_user],
            database='logsdb'
        )
        cursor = conn.cursor()

        if action == 'insert':
            cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        elif action == 'update':
            cursor.execute("UPDATE users SET name = %s WHERE email = %s", (name, email))
        elif action == 'delete':
            cursor.execute("DELETE FROM users WHERE email = %s", (email,))

        conn.commit()
        messagebox.showinfo("Succes", f"{action.upper()} uitgevoerd voor {name} ({email})")

    except mysql.connector.Error as err:
        messagebox.showerror("Databasefout", f"Fout bij verbinding of query: {err}")
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass

# GUI setup
root = tk.Tk()
root.title("Gebruikersactie Menu")

tk.Label(root, text="Kies een gebruiker:").grid(row=0, column=0, padx=10, pady=10)
user_var = tk.StringVar()
user_dropdown = ttk.Combobox(root, textvariable=user_var, values=list(app_users.keys()), state='readonly')
user_dropdown.grid(row=0, column=1)

tk.Label(root, text="Naam:").grid(row=1, column=0, padx=10, pady=5)
name_var = tk.StringVar()
tk.Entry(root, textvariable=name_var).grid(row=1, column=1, columnspan=2, padx=10, pady=5)

tk.Label(root, text="E-mail:").grid(row=2, column=0, padx=10, pady=5)
email_var = tk.StringVar()
tk.Entry(root, textvariable=email_var).grid(row=2, column=1, columnspan=2, padx=10, pady=5)

tk.Button(root, text="Insert", command=lambda: execute_action('insert')).grid(row=3, column=0, pady=10)
tk.Button(root, text="Update", command=lambda: execute_action('update')).grid(row=3, column=1, pady=10)
tk.Button(root, text="Delete", command=lambda: execute_action('delete')).grid(row=3, column=2, pady=10)

root.mainloop()
