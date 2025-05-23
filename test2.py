import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Loginvenster
def show_login_window():
    login_window = tk.Tk()
    login_window.title("Login - MySQL")

    tk.Label(login_window, text="MySQL Gebruikersnaam:").grid(row=0, column=0, padx=10, pady=10)
    username_entry = tk.Entry(login_window)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(login_window, text="MySQL Wachtwoord:").grid(row=1, column=0, padx=10, pady=10)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    def login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        # Probeer verbinding met database
        try:
            test_conn = mysql.connector.connect(
                host='localhost',
                user=username,
                password=password,
                database='logsdb'
            )
            test_conn.close()
            login_window.destroy()
            show_main_window(username, password)
        except mysql.connector.Error as err:
            messagebox.showerror("Verbindingsfout", f"Kan geen verbinding maken met MySQL:\n{err}")

    tk.Button(login_window, text="Inloggen", command=login).grid(row=2, column=0, columnspan=2, pady=10)
    login_window.mainloop()

# Hoofdvenster na succesvolle login
def show_main_window(username, password):
    def execute_action(action):
        name = name_var.get().strip()
        email = email_var.get().strip()

        if not name or not email:
            messagebox.showerror("Fout", "Naam en e-mailadres zijn verplicht.")
            return

        try:
            conn = mysql.connector.connect(
                host='localhost',
                user=username,
                password=password,
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
            if cursor.rowcount == 0:
                messagebox.showwarning("Geen resultaat", "Geen records bijgewerkt of verwijderd.")
            else:
                messagebox.showinfo("Succes", f"{action.upper()} uitgevoerd voor {name} ({email})")

        except mysql.connector.Error as err:
            messagebox.showerror("Databasefout", f"Fout bij verbinding of query: {err}")
        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

    main_window = tk.Tk()
    main_window.title("Gebruikersactie Menu")

    tk.Label(main_window, text="Naam:").grid(row=0, column=0, padx=10, pady=5)
    name_var = tk.StringVar()
    tk.Entry(main_window, textvariable=name_var).grid(row=0, column=1, columnspan=2, padx=10, pady=5)

    tk.Label(main_window, text="E-mail:").grid(row=1, column=0, padx=10, pady=5)
    email_var = tk.StringVar()
    tk.Entry(main_window, textvariable=email_var).grid(row=1, column=1, columnspan=2, padx=10, pady=5)

    tk.Button(main_window, text="Insert", command=lambda: execute_action('insert')).grid(row=2, column=0, pady=10)
    tk.Button(main_window, text="Update", command=lambda: execute_action('update')).grid(row=2, column=1, pady=10)
    tk.Button(main_window, text="Delete", command=lambda: execute_action('delete')).grid(row=2, column=2, pady=10)

    main_window.mainloop()

# Start de applicatie
show_login_window()
