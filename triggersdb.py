import customtkinter as ctk
import tkinter.messagebox as messagebox
import mysql.connector
import re

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

def show_login_window():
    login_window = ctk.CTk()
    login_window.title("Login - MySQL")
    login_window.geometry("350x250")  # Iets hoger dan voorheen
    login_window.iconbitmap('NoorderpoortLogo.ico')

    ctk.CTkLabel(login_window, text="Gebruikersnaam:").pack(pady=(20, 5))
    username_entry = ctk.CTkEntry(login_window)
    username_entry.pack(pady=5)

    ctk.CTkLabel(login_window, text="Wachtwoord:").pack(pady=5)
    password_entry = ctk.CTkEntry(login_window, show="*")
    password_entry.pack(pady=5)

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
            messagebox.showerror("Verbindingsfout", f"MySQL fout:\n{err}")

    login_window.bind('<Return>', lambda e: login())

    ctk.CTkButton(
        login_window,
        text="Inloggen",
        command=login,
        corner_radius=15,
        border_width=2,
        border_color="black",
        fg_color="#e0e0e0",
        hover_color="#4da6ff",
        text_color="black"  # Zwarte tekst
    ).pack(pady=15)

    login_window.mainloop()

def show_table_selection(username, password):
    win = ctk.CTk()
    win.title("Selecteer tabel")
    win.geometry("300x200")
    win.iconbitmap('NoorderpoortLogo.ico')


    ctk.CTkLabel(win, text="Kies een tabel:").pack(pady=20)

    ctk.CTkButton(
        win,
        text="Users beheren",
        command=lambda: [win.destroy(), show_main_window(username, password, 'users')],
        corner_radius=15,
        border_width=2,
        border_color="black",
        fg_color="#e0e0e0",
        hover_color="#4da6ff",
        text_color="black"
    ).pack(pady=10)

    ctk.CTkButton(
        win,
        text="Admins beheren",
        command=lambda: [win.destroy(), show_main_window(username, password, 'admin')],
        corner_radius=15,
        border_width=2,
        border_color="black",
        fg_color="#e0e0e0",
        hover_color="#4da6ff",
        text_color="black"
    ).pack(pady=10)

    win.mainloop()

def show_main_window(username, password, table_name):
    def execute_action(action):
        id_val = id_entry.get().strip()
        name = name_entry.get().strip()
        email = email_entry.get().strip()

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
                if not id_val.isdigit():
                    messagebox.showerror("Fout", "Voer een numerieke ID in.")
                    return
                cursor.execute(f"UPDATE {table_name} SET name = %s, email = %s WHERE id = %s", (name, email, id_val))
            elif action == 'delete':
                confirm = messagebox.askyesno("Bevestigen", f"Weet je zeker dat je {email} wilt verwijderen?")
                if not confirm:
                    return
                cursor.execute(f"DELETE FROM {table_name} WHERE email = %s", (email,))

            conn.commit()
            if cursor.rowcount == 0:
                messagebox.showwarning("Let op", "Geen rijen gewijzigd.")
            else:
                messagebox.showinfo("Succes", f"{action.upper()} voltooid.")

        except mysql.connector.Error as err:
            messagebox.showerror("Fout", f"MySQL-fout:\n{err}")
        finally:
            cursor.close()
            conn.close()

    main_win = ctk.CTk()
    main_win.title(f"Beheer {table_name}")
    main_win.geometry("450x350")  # Groter venster
    main_win.iconbitmap('NoorderpoortLogo.ico')


    ctk.CTkLabel(main_win, text="ID:").pack(pady=(10, 0))
    id_entry = ctk.CTkEntry(main_win)
    id_entry.pack(pady=5)

    ctk.CTkLabel(main_win, text="Naam:").pack()
    name_entry = ctk.CTkEntry(main_win)
    name_entry.pack(pady=5)

    ctk.CTkLabel(main_win, text="Email:").pack()
    email_entry = ctk.CTkEntry(main_win)
    email_entry.pack(pady=5)

    button_style = {
        "corner_radius": 15,
        "border_width": 2,
        "border_color": "black",
        "fg_color": "#e0e0e0",
        "hover_color": "#4da6ff",
        "text_color": "black"
    }

    button_frame = ctk.CTkFrame(main_win)
    button_frame.pack(pady=15, fill="x", padx=20)

    ctk.CTkButton(button_frame, text="Insert", command=lambda: execute_action('insert'), **button_style).pack(side="left", expand=True, padx=5)
    ctk.CTkButton(button_frame, text="Update", command=lambda: execute_action('update'), **button_style).pack(side="left", expand=True, padx=5)
    ctk.CTkButton(button_frame, text="Delete", command=lambda: execute_action('delete'), **button_style).pack(side="left", expand=True, padx=5)

    main_win.mainloop()

# Start de GUI
show_login_window()
