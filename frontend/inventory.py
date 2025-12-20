import customtkinter as ctk
from backend.app import *   # your supabase function


def inventory(main_frame):

    # ===== CLEAR =====
    for w in main_frame.winfo_children():
        w.destroy()

    root = main_frame.winfo_toplevel()

    # ===== HEADER =====
    top = ctk.CTkFrame(main_frame,
                       fg_color="#fcffff")
    top.pack(fill="x", padx=15, pady=10)

    ctk.CTkLabel(
        top,
        text="INVENTORY",
        font=("Arial", 22, "bold"),
        text_color="black"
    ).pack(side="left")

    search_var = ctk.StringVar()

    ctk.CTkEntry(
        top,
        placeholder_text="Search product...",
        textvariable=search_var,
        width=200
    ).pack(side="left", padx=10)

    ctk.CTkButton(
        top, text="Search",
        command=lambda: load_table(search_var.get())
    ).pack(side="left")

    ctk.CTkButton(
        top, text="Refresh", fg_color="green",
        command=lambda: load_table()
    ).pack(side="right")

    ctk.CTkButton(
        top, text="Add", fg_color="green",
        command=lambda: add_popup()
    ).pack(side="right", padx=5)

    # ===== TABLE =====
    scroll = ctk.CTkScrollableFrame(main_frame)
    scroll.pack(fill="both", expand=True,)

    table = ctk.CTkFrame(scroll)
    table.pack(fill="both", expand=True)

    headers = ["ID", "Product", "Category", "Price", "Stock", "Action"]

    def load_table(search=""):
        for w in table.winfo_children():
            w.destroy()

        # Header
        for c, h in enumerate(headers):
            ctk.CTkLabel(
                table,
                text=h,
                font=("Arial", 14, "bold")
            ).grid(row=0, column=c, padx=10, pady=5)

        data = get_products(search)

        for r, item in enumerate(data, start=1):
            bg = "#2a2d2e" 

            values = [
                item["product_id"],
                item["product_name"],
                item["category"],
                f"₱{item['price']}",
                item["quantity"]
            ]

            for c, v in enumerate(values):
                cell = ctk.CTkFrame(table, fg_color=bg)
                cell.grid(row=r, column=c, padx=5, pady=3, sticky="nsew")
                ctk.CTkLabel(cell, text=v).pack(padx=8, pady=5)

            # Action buttons
            btns = ctk.CTkFrame(table)
            btns.grid(row=r, column=5, padx=5)

            ctk.CTkButton(
                btns, text="Edit", width=60,
                command=lambda i=item: edit_popup(i)
            ).pack(side="left", padx=2)

            ctk.CTkButton(
                btns, text="Del", width=60,
                fg_color="red",
                command=lambda i=item: confirm_delete(i)
            ).pack(side="left", padx=2)

        for c in range(len(headers)):
            table.grid_columnconfigure(c, weight=1)

    def popup_base(title):
        popup = ctk.CTkToplevel(root)
        popup.title(title)
        popup.geometry("300x350")

        popup.lift()
        popup.focus_force()
        popup.grab_set()
        popup.attributes("-topmost", True)
        popup.after(200, lambda: popup.attributes("-topmost", False))

        return popup

    def confirm_delete(item):
        popup = ctk.CTkToplevel(root)
        popup.title("Confirm Delete")
        popup.geometry("320x180")

        popup.lift()
        popup.focus_force()
        popup.grab_set()
        popup.attributes("-topmost", True)
        popup.after(200, lambda: popup.attributes("-topmost", False))

        ctk.CTkLabel(
            popup,
            text="Are you sure you want to delete\nthis product?",
            font=("Arial", 14, "bold"),
            text_color="red"
        ).pack(pady=(20, 5))

        ctk.CTkLabel(
            popup,
            text=f"{item['product_name']}",
            font=("Arial", 13)
        ).pack(pady=(0, 15))

        btn_frame = ctk.CTkFrame(popup)
        btn_frame.pack(pady=10)

        def yes_delete():
            delete_product(item["product_id"])
            popup.destroy()
            load_table()

        ctk.CTkButton(
            btn_frame,
            text="Yes, Delete",
            fg_color="red",
            width=120,
            command=yes_delete
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            btn_frame,
            text="Cancel",
            width=120,
            command=popup.destroy
        ).pack(side="left", padx=5)

    def add_popup():
        popup = popup_base("Add Product")

        entries = {}
        for field in ["product_name", "category", "price", "quantity"]:
            ctk.CTkLabel(popup, text=field.capitalize()).pack(pady=(8, 0))
            e = ctk.CTkEntry(popup)
            e.pack(pady=5)
            entries[field] = e

        def save():
            add_product({
                "product_name": entries["product_name"].get(),
                "category": entries["category"].get(),
                "price": int(entries["price"].get()),
                "quantity": int(entries["quantity"].get())
            })
            popup.destroy()
            load_table()

        ctk.CTkButton(popup, text="Save", command=save).pack(pady=15)
        
    def edit_popup(item):
        popup = popup_base("Edit Product")

        entries = {}
        for field in ["product_name", "category", "price", "quantity"]:
            ctk.CTkLabel(popup, text=field.capitalize()).pack(pady=(8, 0))
            e = ctk.CTkEntry(popup)
            e.insert(0, item[field])
            e.pack(pady=5)
            entries[field] = e

        def update():
            update_product(item["product_id"], {
                "product_name": entries["product_name"].get(),
                "category": entries["category"].get(),
                "price": int(entries["price"].get()),
                "quantity": int(entries["quantity"].get())
            })
            popup.destroy()
            load_table()

        ctk.CTkButton(popup, text="Update", command=update).pack(pady=15)

    def delete_and_refresh(pid):
        delete_product(pid)
        load_table()

    load_table()