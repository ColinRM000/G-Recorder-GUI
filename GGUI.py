import gspread
import datetime
import tkinter as tk
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from tkinter import messagebox
from ttkthemes import ThemedStyle
from PIL import ImageTk, Image

# GOOGLE DOC / SHEETS CONNECTION

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

cli = gspread.authorize(creds)

sheet = cli.open("G-Recorder").sheet1  # Open the spreadhseet

numRows = sheet.row_count  # Get the number of rows in the sheet
#####################################################################################################################################

root = tk.Tk()
root.iconbitmap("GRecorder.ico")
root.title("G-Recorder")
root.geometry("500x300")

# Configure theme colors
bg_color = '#282828' # Dark gray background
fg_color = '#F5F5F5' # Light gray foreground
highlight_color = '#FFFFFF' # White highlight color

root.configure(bg=bg_color)
root.option_add('*foreground', fg_color)
root.option_add('*background', bg_color)
root.option_add('*highlightBackground', highlight_color)
root.option_add('*highlightColor', fg_color)

# Labels
name_label = tk.Label(root, text="Customer Name:", bg=bg_color, fg=fg_color)
name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

email_label = tk.Label(root, text="Customer Email:", bg=bg_color, fg=fg_color)
email_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

number_label = tk.Label(root, text="Customer Phone #:", bg=bg_color, fg=fg_color)
number_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

product_label = tk.Label(root, text="Product:", bg=bg_color, fg=fg_color)
product_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

quantity_label = tk.Label(root, text="Quantity:", bg=bg_color, fg=fg_color)
quantity_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

price_label = tk.Label(root, text="Price:", bg=bg_color, fg=fg_color)
price_label.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)

# Entry boxes
name_entry = tk.Entry(root, bg=bg_color, fg=fg_color, insertbackground=fg_color)
name_entry.grid(row=0, column=1)

email_entry = tk.Entry(root, bg=bg_color, fg=fg_color, insertbackground=fg_color)
email_entry.grid(row=1, column=1)

number_entry = tk.Entry(root, bg=bg_color, fg=fg_color, insertbackground=fg_color)
number_entry.grid(row=2, column=1)

product_entry = tk.Entry(root, bg=bg_color, fg=fg_color, insertbackground=fg_color)
product_entry.grid(row=3, column=1)

quantity_entry = tk.Entry(root, bg=bg_color, fg=fg_color, insertbackground=fg_color)
quantity_entry.grid(row=4, column=1)

price_entry = tk.Entry(root, bg=bg_color, fg=fg_color, insertbackground=fg_color)
price_entry.grid(row=5, column=1)

def clear_entries():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    number_entry.delete(0, tk.END)
    product_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

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

record_button = tk.Button(root, text="Record Order", command=record_order)
record_button.grid(row=6, column=0, columnspan=2, pady=10)

quit_button = tk.Button(root, text="Quit", command=on_exit)
quit_button.grid(row=6, column=2, columnspan=2, pady=10)

root.mainloop()

