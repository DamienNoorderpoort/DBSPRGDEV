import customtkinter as ctk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk
import mysql.connector
import re

import functies 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def show_login_window(geometry_position=None):
    login_window = ctk.CTk()
    login_window.title("Login - MySQL")
    login_window.geometry(geometry_position or "350x250")
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
            pos = login_window.geometry()
            login_window.destroy()
            show_table_selection(username, password, pos)
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
        text_color="black"
    ).pack(pady=10)

    functies.add_close_button(login_window)

    login_window.mainloop()


def show_table_selection(username, password, geometry_position=None):
    win = ctk.CTk()
    win.title("Selecteer tabel")
    win.geometry(geometry_position or "300x250")
    win.iconbitmap('NoorderpoortLogo.ico')

    ctk.CTkLabel(win, text="Kies een tabel:").pack(pady=20)

    def open_users():
        win.destroy()
        show_main_window(username, password, 'users', None)

    def open_admins():
        win.destroy()
        show_main_window(username, password, 'admins', None)

    def terug_naar_login():
        pos = win.geometry()
        win.destroy()
        show_login_window(pos)

    button_style = {
        "corner_radius": 15,
        "border_width": 2,
        "border_color": "black",
        "fg_color": "#e0e0e0",
        "hover_color": "#4da6ff",
        "text_color": "black"
    }

    ctk.CTkButton(win, text="Users beheren", command=open_users, **button_style).pack(pady=10)
    ctk.CTkButton(win, text="Admins beheren", command=open_admins, **button_style).pack(pady=10)

    functies.add_back_button(win, terug_naar_login)
    functies.add_close_button(win)

    win.mainloop()


def show_main_window(username, password, table_name, geometry_position=None):
    sort_order = {"id": True, "name": True, "email": True} 
    current_sort_col = "id"

    def update_headings():
        arrows = {"asc": " ▲", "desc": " ▼"}
        for col in ("id", "name", "email"):
            arrow = ""
            if col == current_sort_col:
                arrow = arrows["asc" if sort_order[col] else "desc"]
            display_name = {"id": "ID", "name": "Naam", "email": "Email"}[col]
            tree.heading(col, text=display_name + arrow, command=lambda c=col: sort_column(c))

    def load_data(sort_by="id", ascending=True):
        nonlocal current_sort_col
        current_sort_col = sort_by
        update_headings()
        for row in tree.get_children():
            tree.delete(row)
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user=username,
                password=password,
                database='logsdb'
            )
            cursor = conn.cursor()
            order = "ASC" if ascending else "DESC"
            cursor.execute(f"SELECT id, name, email FROM {table_name} ORDER BY {sort_by} {order}")
            rows = cursor.fetchall()
            for row in rows:
                tree.insert("", "end", values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("Fout", f"MySQL-fout bij ophalen van data:\n{err}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def sort_column(col):
        sort_order[col] = not sort_order[col] 
        load_data(sort_by=col, ascending=sort_order[col])

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

            id_entry.delete(0, 'end')
            name_entry.delete(0, 'end')
            email_entry.delete(0, 'end')
            load_data(current_sort_col, sort_order[current_sort_col])

        except mysql.connector.Error as err:
            messagebox.showerror("Fout", f"MySQL-fout:\n{err}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def terug_naar_selectie():
        pos = main_win.geometry()
        main_win.destroy()
        show_table_selection(username, password, pos)

    main_win = ctk.CTk()
    main_win.title(f"Beheer {table_name}")
    main_win.geometry(geometry_position or "700x550")
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
    button_frame.pack(pady=10, fill="x", padx=20)

    ctk.CTkButton(button_frame, text="Insert", command=lambda: execute_action('insert'), **button_style).pack(side="left", expand=True, padx=5)
    ctk.CTkButton(button_frame, text="Update", command=lambda: execute_action('update'), **button_style).pack(side="left", expand=True, padx=5)
    ctk.CTkButton(button_frame, text="Delete", command=lambda: execute_action('delete'), **button_style).pack(side="left", expand=True, padx=5)

    tree_frame = ctk.CTkFrame(main_win)
    tree_frame.pack(pady=10, padx=20, fill="both", expand=True)

    tree = ttk.Treeview(tree_frame, columns=("id", "name", "email"), show="headings")

    update_headings()  

    tree.column("id", width=50)
    tree.column("name", width=200)
    tree.column("email", width=250)
    tree.pack(fill="both", expand=True)

    tree.bind("<ButtonRelease-1>", lambda e: None)  

    functies.add_back_button(main_win, terug_naar_selectie)
    functies.add_close_button(main_win)

    load_data()
    main_win.mainloop()


show_login_window()
