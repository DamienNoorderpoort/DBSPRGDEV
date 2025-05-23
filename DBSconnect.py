import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
import mysql.connector

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    database="dbs_triggers",
    user="pieter",
    password="Welkom01",
    port=3306
)
mycursor = mydb.cursor()

# functie om de query uit te voeren
def execute_query():
    schema = schema_combobox.get()
    if not schema.strip():
        messagebox.showwarning("Input Error", "Selecteer een geldig schema.")
        return
    
    schema2 = schemaselectjoin_combobox.get()
    if not schema2.strip():
        messagebox.showwarning("Input Error", "Selecteer een geldig schema.")
        return

    query = query_entry.get()
    if not query.strip():
        messagebox.showwarning("Input Error", "Selecteer een geldig ID.")
        return

    queryupdate = queryupdate_entry.get()
    if not queryupdate.strip():
        messagebox.showwarning("Input Error", "Maak een geldige mail")
        return


    try:
        # Maakt query en voert uit.
        if schemaleftjoin_combobox.get() == "nee":
            sql_query = f"UPDATE users SET email = '{queryupdate}' WHERE id = {query};"
            mycursor.execute(sql_query)
            mydb.commit()

        # Kolom namen
        column_names = [desc[0] for desc in mycursor.description]

        # Cleart treeview
        results_tree.delete(*results_tree.get_children())

        # Update Treeview kolommen
        results_tree["columns"] = column_names
        results_tree["show"] = "headings"

        for col in column_names:
            results_tree.heading(col, text=col)
            results_tree.column(col, width=150, anchor="w")

        # voegt rijen toe aan de treeview
        for row in results:
            results_tree.insert("", "end", values=row)
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

# Maakt de GUI
root = tk.Tk()
root.title("SQL ID Search")

# Maakt een paneel om een schema te selecteren
tk.Label(root, text="Selecteer Schema:").pack(pady=5)
schema_combobox = ttk.Combobox(root, values=["users", "user_log"])  # Voeg schema's hier statisch toe
schema_combobox.pack(pady=5)
schema_combobox.set("users")  # default schema

tk.Label(root, text="Selecteer left join schema:").pack(pady=5)
schemaselectjoin_combobox = ttk.Combobox(root, values=["users", "user_log"])  # Voeg schema's hier statisch toe
schemaselectjoin_combobox.pack(pady=5)
schemaselectjoin_combobox.set("user_log")  # default left join schema

tk.Label(root, text="Left join?").pack(pady=5)
schemaleftjoin_combobox = ttk.Combobox(root, values=["ja", "nee"])  # ja en nee optie
schemaleftjoin_combobox.pack(pady=5)
schemaleftjoin_combobox.set("nee")  # default nee

# ID invoeren
tk.Label(root, text="Voer ID in:").pack(pady=5)
query_entry = tk.Entry(root, width=50)
query_entry.pack(pady=5)

# Email invoeren
tk.Label(root, text="Voer nieuw e-mailadres in:").pack(pady=5)
queryupdate_entry = tk.Entry(root, width=50)
queryupdate_entry.pack(pady=5)

# Knop om de query uit te voeren
execute_button = tk.Button(root, text="Execute", command=execute_query)
execute_button.pack(pady=5)

# Resultaten Treeview
tk.Label(root, text="Results:").pack(pady=5)
results_tree = ttk.Treeview(root, height=20)
results_tree.pack(pady=5, fill="both", expand=True)

# laat de code draaien
root.mainloop()
