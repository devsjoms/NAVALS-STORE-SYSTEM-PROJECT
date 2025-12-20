import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("650x350")
app.title("CTK TableFrame Sample")

# ===== Scrollable Container =====
scroll = ctk.CTkScrollableFrame(app)
scroll.pack(fill="both", expand=True, padx=10, pady=10)

table = ctk.CTkFrame(scroll, corner_radius=10)
table.pack(fill="both", expand=True)

# ===== Table Data =====
headers = ["ID", "Product", "Category", "Price", "Stock"]
data = [
    [1, "Rice", "Food", "₱50", 20],
    [2, "Sugar", "Food", "₱45", 15],
    [3, "Coffee", "Drink", "₱120", 10],
    [4, "Milk", "Drink", "₱60", 25],
    [5, "Soap", "Hygiene", "₱35", 30],
]

# ===== Header =====
for col, text in enumerate(headers):
    ctk.CTkLabel(
        table,
        text=text,
        font=("Arial", 14, "bold")
    ).grid(row=0, column=col, padx=10, pady=8, sticky="w")

# ===== Rows =====
for row_index, row in enumerate(data, start=1):
    bg = "#2a2d2e" if row_index % 2 == 0 else "#1f2223"

    for col_index, cell in enumerate(row):
        cell_frame = ctk.CTkFrame(
            table,
            fg_color=bg,
            corner_radius=6
        )
        cell_frame.grid(
            row=row_index,
            column=col_index,
            padx=5,
            pady=3,
            sticky="nsew"
        )

        ctk.CTkLabel(
            cell_frame,
            text=cell,
            font=("Arial", 13)
        ).pack(padx=8, pady=6)

# ===== Make columns responsive =====
for col in range(len(headers)):
    table.grid_columnconfigure(col, weight=1)

app.mainloop()
