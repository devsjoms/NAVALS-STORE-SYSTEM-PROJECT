from customtkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from frontend.dashboard import *
from frontend.sales import *
from frontend.inventory import *
from frontend.products import *
from frontend.customers import *

def main():
    gui.geometry("1200x600")
    gui.title("JOCELYN NAVAL STORE")
    
    side_bar = CTkFrame(gui,
                        width=250,
                        corner_radius = 0,
                        fg_color= "grey",
                        bg_color="grey")
    side_bar.pack(side = "left", fill = "y")
    side_bar.pack_propagate(False)

    sidebar_text = CTkLabel(side_bar,
                            text="ADMIN JOMS",
                            font=("Arial",30, "bold"),
                            text_color="white")
    sidebar_text.pack(pady=20)
    
    head_bar = CTkFrame(gui,
                        height=100,
                        corner_radius = 0,
                        fg_color= "#a099ff",
                        bg_color="#a099ff")
    head_bar.pack(side = "top", fill = "x")
    head_bar.pack_propagate(False)
    
    title_text = CTkLabel(head_bar, 
                          text="ALING LEN-LEN SARI SARI STORE",
                          font=("Arial", 35, "bold"),
                          text_color="#f00524")
    title_text.pack(fill = "both", expand = True)
    
    main_frame = CTkScrollableFrame(gui,
                          fg_color="#fcffff",
                          bg_color="#fcffff",
                          corner_radius=0)
    main_frame.pack(fill= "both", expand = True)
    
    admin_text = CTkLabel(side_bar,
                           text= "ADMIN",
                           text_color="brown",
                           font=("Arial", 10, "bold"))
    admin_text.pack()
    admin_text.pack_propagate(False)
    
    home_btn = CTkButton(side_bar,
                         text="HOME",
                         height= 40,
                         fg_color="#d6d0d6",
                         text_color="#060a3d")
    home_btn.pack(fill = "both", pady = 5)
    
    dash_btn = CTkButton(side_bar,
                         text="DASHBOARD",
                         height= 40,
                         fg_color="#d6d0d6",
                         text_color="#060a3d",
                         command=lambda:dashboard(main_frame))
    dash_btn.pack(fill = "both", pady = 5)
    
    manage_text = CTkLabel(side_bar,
                           text= "MANAGE",
                           text_color="brown",
                           font=("Arial", 10, "bold"))
    manage_text.pack()
    manage_text.pack_propagate(False)
    
    
    invent_btn = CTkButton(side_bar,
                         text="INVENTORY",
                         height= 40,
                         fg_color="#d6d0d6",
                         text_color="#060a3d",
                         command = lambda:inventory(main_frame))
    invent_btn.pack(fill = "both", pady = 5)
    invent_btn.pack_propagate(False)
    
    sales_btn = CTkButton(side_bar,
                         text="SALES",
                         height= 40,
                         fg_color="#d6d0d6",
                         text_color="#060a3d",
                         command=lambda:sales(main_frame))
    sales_btn.pack(fill = "both", pady = 5)
    
    product_btn = CTkButton(side_bar,
                         text="PRODUCT",
                         height= 40,
                         fg_color="#d6d0d6",
                         text_color="#060a3d",
                         command = lambda:products(main_frame))
    product_btn.pack(fill = "both", pady = 5)
    
    customers_btn = CTkButton(side_bar,
                         text="CUSTOMERS",
                         height= 40,
                         fg_color="#d6d0d6",
                         text_color="#060a3d",
                         command = lambda:customers(main_frame))
    customers_btn.pack(fill = "both", pady = 5)
    
gui = CTk()
main()
gui.mainloop()