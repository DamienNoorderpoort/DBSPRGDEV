import tkinter as tk
from tkinter import messagebox
import mysql.connector
import re

# Loginvenster
def show_login_window():
    login_window = tk.Tk()
    login_window.title("Login - MySQL")
    login_window.configure(bg='lightgrey')

    tk.Label(login_window, text="Gebruikersnaam:").grid(row=0, column=0, padx=10, pady=10)
    username_entry = tk.Entry(login_window)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(login_window, text="Wachtwoord:").grid(row=1, column=0, padx=10, pady=10)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    def login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        try:
            test_conn = mysql.connector.connect(
                host='localhost',
                user=username,
                password=password,
                database='logsdb'
            )
            test_conn.close()
            login_window.destroy()
            show_table_selection(username, password)
        except mysql.connector.Error as err:
            messagebox.showerror("Verbindingsfout - Let op Hoofdletters!", f"Kan geen verbinding maken met MySQL:\n{err}")

    login_window.bind('<Return>', lambda event: login())
    tk.Button(login_window, text="Inloggen", command=login).grid(row=2, column=0, columnspan=2, pady=10)
    login_window.mainloop()

# Keuze tussen 'users' en 'admin'
def show_table_selection(username, password):
    selection_window = tk.Tk()
    selection_window.title("Selecteer Tabel")
    selection_window.configure(bg='lightgrey')

    tk.Label(selection_window, text="Kies een tabel om te beheren:", bg='lightgrey', font=('Arial', 10)).pack(pady=20)

    tk.Button(selection_window, text="Users beheren", width=20,
              command=lambda: [selection_window.destroy(), show_main_window(username, password, 'users')]).pack(pady=10)

    tk.Button(selection_window, text="Admins beheren", width=20,
              command=lambda: [selection_window.destroy(), show_main_window(username, password, 'admin')]).pack(pady=10)

    selection_window.mainloop()

# Hoofdvenster voor CRUD
def show_main_window(username, password, table_name):
    def execute_action(action):
        name = name_var.get().strip()
        email = email_var.get().strip()

        if not name or not email:
            messagebox.showerror("Fout", "Naam en e-mailadres zijn verplicht.")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Fout", "Voer een geldig e-mailadres in.")
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
                cursor.execute(f"INSERT INTO {table_name} (name, email) VALUES (%s, %s)", (name, email))
            elif action == 'update':
                cursor.execute(f"UPDATE {table_name} SET name = %s WHERE email = %s", (name, email))
            elif action == 'delete':
                confirm = messagebox.askyesno("Bevestigen", f"Weet je zeker dat je {email} wilt verwijderen uit {table_name}?")
                if not confirm:
                    return
                cursor.execute(f"DELETE FROM {table_name} WHERE email = %s", (email,))

            conn.commit()
            if cursor.rowcount == 0:
                messagebox.showwarning("Geen resultaat", "Geen records bijgewerkt of verwijderd.")
            else:
                messagebox.showinfo("Succes", f"{action.upper()} uitgevoerd voor {name} ({email}) in {table_name}")

        except mysql.connector.Error as err:
            messagebox.showerror("Databasefout", f"Fout bij verbinding of query: {err}")
        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

    main_window = tk.Tk()
    main_window.title(f"Beheer: {table_name.capitalize()}")
    main_window.configure(bg='lightgrey')

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
