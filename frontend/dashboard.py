from customtkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def dashboard(main_frame):
    for widget in main_frame.winfo_children():
        widget.destroy()
        
    sales_sum = CTkLabel(main_frame,
                         text="SALES SUMMARY",
                         font = ("Arial",20, "bold"),
                         text_color="#000000")
    sales_sum.pack()
    container = CTkFrame(main_frame,
                         fg_color="white")
    container.pack(fill="x", pady=50)

    
    daily_frame = CTkFrame(container,
                           height=190,
                           width=400,
                           fg_color= "blue")
    daily_frame.pack(side="left", expand = True)
    daily_frame.pack_propagate(False)

    daily_text = CTkLabel(daily_frame,
                          text="$2000",
                          font=("Arial", 30, "bold"),
                          text_color="#fcffaf")
    daily_text.pack(expand = True)
    
    daily_text = CTkLabel(daily_frame,
                          text="DAILY SALES",
                          font=("Arial", 15, "bold"),
                          text_color="#fcffaf")
    daily_text.pack(expand = True)
    

    monthly_frame = CTkFrame(container,
                           height=190,
                           width=400,
                           fg_color= "blue")
    monthly_frame.pack(side="left", expand = True)
    monthly_frame.pack_propagate(False)
    
    products_frame = CTkFrame(container,
                           height=190,
                           width=400,
                           fg_color= "blue")
    products_frame.pack(side="left", expand = True)
    products_frame.pack_propagate(False)
    
    
    graph_frame = CTkFrame(main_frame,
                           fg_color="#fcffff")
    graph_frame.pack()
    
    pie_graph_frame = CTkFrame(graph_frame,
                               width=500,
                               height=500,
                               )
    pie_graph_frame.pack(expand = True,
                         side="left",
                         padx = 50)
    pie_graph_frame.pack_propagate(False)
    
    labels = ["Food","Transport", "Savings"]
    values = [60, 20, 20]

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.pie(values, labels=labels, autopct="%1.1f%%")
    ax.set_title("Monthly Expenses")

    canvas = FigureCanvasTkAgg(fig, master=pie_graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
    
    bar_graph_frame = CTkFrame(graph_frame,
                               width=500,
                               height=500)
    bar_graph_frame.pack(expand = True,
                         side="right",
                         padx = 50)
    bar_graph_frame.pack_propagate(False)
    
    items = ["Frozen Goods", "Eggs", "Sardines"]
    sales = [80, 40, 30]

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.bar(items, sales)
    ax.set_title("Daily Sales")
    ax.set_ylabel("Sales Rate")

    canvas = FigureCanvasTkAgg(fig, master=bar_graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
    
    
    
    history_transaction = CTkLabel(main_frame,
                                   text="TRANSACTION HISTORY",
                                   font=("Arial", 20, "bold"),
                                   text_color= "#000000")
    history_transaction.pack()
    
    scroll = CTkScrollableFrame(main_frame,
                                height=400)
    scroll.pack(fill="both", expand=True, padx=10, pady=10)

    for i in range(5):
        card = CTkFrame(scroll, 
                        height= 70, 
                        corner_radius=10,
                        fg_color ="#aaafff")
        card.pack(fill="x", pady=8)
        card.pack_propagate(False)

        CTkLabel(card, text=f"Product {i+1}", font=("Arial", 14)).pack(anchor="w", padx=15, pady=5)
        CTkLabel(card, text=f"₱ {150+i}.00", text_color="gray").pack(anchor="w", padx=15)