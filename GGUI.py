import gspread
import datetime
import tkinter as tk
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from tkinter import messagebox
from ttkthemes import ThemedStyle
from PIL import ImageTk, Image
import customtkinter as ctk

# GOOGLE DOC / SHEETS CONNECTION

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

cli = gspread.authorize(creds)

sheet = cli.open("G-Recorder").sheet1  # Open the spreadhseet

numRows = sheet.row_count  # Get the number of rows in the sheet

#####################################################################################################################################

root = ctk.CTk()
root.iconbitmap("GRecorder.ico")
root.title("G-Recorder")
root.geometry("450x400")

# Configure theme colors
style = ThemedStyle(root)
style.set_theme("arc")
ctk.set_appearance_mode('dark')

# Labels
name_label = ctk.CTkLabel(root, text="Customer Name:")
name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

email_label = ctk.CTkLabel(root, text="Customer Email:")
email_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

number_label = ctk.CTkLabel(root, text="Customer Phone #:")
number_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

product_label = ctk.CTkLabel(root, text="Product:")
product_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

quantity_label = ctk.CTkLabel(root, text="Quantity:")
quantity_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

price_label = ctk.CTkLabel(root, text="Price:")
price_label.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)

# Entry boxes
name_entry = ctk.CTkEntry(root)
name_entry.grid(row=0, column=1)

email_entry = ctk.CTkEntry(root)
email_entry.grid(row=1, column=1)

number_entry = ctk.CTkEntry(root)
number_entry.grid(row=2, column=1)

product_entry = ctk.CTkEntry(root)
product_entry.grid(row=3, column=1)

quantity_entry = ctk.CTkEntry(root)
quantity_entry.grid(row=4, column=1)

price_entry = ctk.CTkEntry(root)
price_entry.grid(row=5, column=1)

def clear_entries():
    name_entry.delete(0, ctk.END)
    email_entry.delete(0, ctk.END)
    number_entry.delete(0, ctk.END)
    product_entry.delete(0, ctk.END)
    quantity_entry.delete(0, ctk.END)
    price_entry.delete(0, ctk.END)

def record_order():
    cxname = name_entry.get()
    email = email_entry.get()
    number = number_entry.get()
    product = product_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()

    row = [cxname, email, number, product, quantity, price, f'{datetime.datetime.utcnow()}']
    sheet.append_row(row)
    
    clear_entries() 

    messagebox.showinfo("Order Recorded", "The order has been recorded successfully!")

def on_exit():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        root.destroy()

record_button = ctk.CTkButton(root, text="Record Order", command=record_order)
record_button.grid(row=6, column=0, columnspan=2, pady=10)

quit_button = ctk.CTkButton(root, text="Quit", command=on_exit)
quit_button.grid(row=6, column=2, columnspan=2, pady=10)

root.mainloop()
