from customtkinter import *

def dashboard():
    for i in gui.winfo_children():
        i.destroy()
def sales(main_frame):
    for widget in main_frame.winfo_children():
        widget.destroy()
        
    container = CTkFrame(main_frame,
                         fg_color="white")
    container.pack(fill="x", pady=50)

    daily_frame = CTkFrame(container,
                           height=190,
                           width=290,
                           fg_color= "blue")
    daily_frame.pack(side="left", expand = True)
    daily_frame.pack_propagate(False)

    monthly_frame = CTkFrame(container,
                           height=190,
                           width=290,
                           fg_color= "blue")
    monthly_frame.pack(side="left", expand = True)
    monthly_frame.pack_propagate(False)
    
    products_frame = CTkFrame(container,
                           height=190,
                           width=290,
                           fg_color= "blue")
    products_frame.pack(side="left", expand = True)
    products_frame.pack_propagate(False)
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
                          text="TITA LEN-LEN STORE",
                          font=("Arial", 35, "bold"),
                          text_color="#f00524")
    title_text.pack(fill = "both", expand = True)
    
    main_frame = CTkScrollableFrame(gui,
                          fg_color="white",
                          bg_color="white",
                          corner_radius=0)
    main_frame.pack(fill= "both", expand = True)
    
    home_btn = CTkButton(side_bar,
                         text="HOME",
                         height= 40,
                         fg_color="#d6d0d6",
                         text_color="#060a3d")
    home_btn.pack(fill = "both", pady = 5)
    
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
                         text_color="#060a3d")
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
                         text_color="#060a3d")
    product_btn.pack(fill = "both", pady = 5)
    
    customers_btn = CTkButton(side_bar,
                         text="CUSTOMERS",
                         height= 40,
                         fg_color="#d6d0d6",
                         text_color="#060a3d")
    customers_btn.pack(fill = "both", pady = 5)
    
gui = CTk()
main()
gui.mainloop()