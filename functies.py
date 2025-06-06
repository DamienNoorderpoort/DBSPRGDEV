import customtkinter as ctk
import tkinter.messagebox as messagebox
import mysql.connector
import re

def add_close_button(window):
    def afsluiten():
        window.destroy()
        ctk.CTk().quit()

    ctk.CTkButton(
        window,
        text="Afsluiten",
        command=afsluiten,
        corner_radius=15,
        border_width=2,
        border_color="black",
        fg_color="#ff5353",
        hover_color="#ff1a1a",
        text_color="white"
    ).pack(pady=5)

def add_back_button(window, command):
    ctk.CTkButton(
        window,
        text="Terug",
        command=command,
        corner_radius=15,
        border_width=2,
        border_color="black",
        fg_color="#ffffff",
        hover_color="#ff3333",
        text_color="black"
    ).pack(pady=10)
    