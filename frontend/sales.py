from backend.app import *
from customtkinter import *

def sales(main_frame):
    for widget in main_frame.winfo_children():
        widget.destroy()
    
    
    row_container = CTkFrame(main_frame)
    row_container.pack(expand=True, fill="x")

    products = get_products()

    for prods in products:
        # Create a frame for each product (one row)
        product_row = CTkFrame(row_container)
        product_row.pack(fill="x", pady=5)  # fill horizontally, add spacing between rows

        CTkLabel(product_row, text=f"ID: {prods['product_id']}").pack(side="left", padx=5)
        CTkLabel(product_row, text=f"Name: {prods['product_name']}").pack(side="left", padx=5)
        CTkLabel(product_row, text=f"Category: {prods.get('category', '')}").pack(side="left", padx=5)
        CTkLabel(product_row, text=f"Price: {prods.get('price', '')}").pack(side="left", padx=5)