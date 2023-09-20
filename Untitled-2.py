from tkinter import *
from tkinter import ttk


import customtkinter
from CTkTable import *


import customtkinter
import os
from PIL import Image
import create_db 


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(main):
        super().__init__()

        main.title("Книжная полка")
        main.geometry(f"{600}x{450}")

        x = (main.winfo_screenwidth() - main.winfo_reqwidth()) / 4
        y = 0

        main.wm_geometry("+%d+%d" % (x, y))
        main.resizable(False, False)

        main.columnconfigure(index=0, minsize=600)
        main.rowconfigure(index=0, minsize=450)

        main.create_main_frame()

    ### MAIN FRAIME ###
    def create_main_frame(main):

        main.geometry(f"{900}x{500}")

        main.home = customtkinter.CTkFrame(main)
        main.home.grid(row=0, column=0, sticky="nsew")


        for i in range(0, 9):
            main.home.columnconfigure(index=i, minsize=100)

        for i in range(0, 10):
            main.home.rowconfigure(index=i, minsize=50)

        
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")

        # create main background
        main.home.main_background_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "background.png")), size=(900,500))

        main.home.main_background = customtkinter.CTkLabel(main.home, text="", image=main.home.main_background_image)
        main.home.main_background.grid(row=0, column=0, sticky='NSEW', rowspan = 9, columnspan = 8)

         # create main button
        main.home.main_buttom_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "main_button.png")), size=(100,50))

        main.home.main_buttome = customtkinter.CTkLabel(main.home, text="", image=main.home.main_buttom_image)
        main.home.main_buttome.grid(row=4, column=6, sticky='NSEW')

        def change_frame(event):
           main.button_menu_event()

        main.home.main_buttome.bind('<Button-1>', change_frame)        

    ### MENU FRAIME ###
    def create_menu_frame(main):
        main.geometry(f"{800}x{600}")

        main.home = customtkinter.CTkFrame(main)
        main.home.grid(row=0, column=0, sticky="nsew")

        main.home.columnconfigure(index=0, minsize=80)
        
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")

        main.home.menu_background_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "background.png")), size=(800,600))
        main.home.menu_frame_background = customtkinter.CTkLabel(main.home, text="", image=main.home.menu_background_image)
        main.home.menu_frame_background.grid(row=0, column=0, sticky='NSEW', rowspan = 4, columnspan = 7)
        
        main.home.menu_button_1 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "menu_button_1.png")), size=(150,150))
        main.home.menu_button_2 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "menu_button_2.png")), size=(150,150))
        main.home.menu_button_3 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "menu_button_3.png")), size=(150,150))
        main.home.menu_button_4 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "menu_button_4.png")), size=(150,150))
        main.home.menu_button_5 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "menu_button_5.png")), size=(150,150))
        main.home.menu_button_6 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "menu_button_6.png")), size=(150,150))

        main.home.menu_frame_button_1 = customtkinter.CTkLabel(main.home, fg_color="transparent", text = '', image=main.home.menu_button_1)
        main.home.menu_frame_button_1.grid(row=1, column=1)

        main.home.menu_frame_button_2 = customtkinter.CTkLabel(main.home, fg_color="transparent", text = '', image=main.home.menu_button_2)
        main.home.menu_frame_button_2.grid(row=1, column=2)

        main.home.menu_frame_button_3 = customtkinter.CTkLabel(main.home, fg_color="transparent", text = '', image=main.home.menu_button_3)
        main.home.menu_frame_button_3.grid(row=1, column=3)

        main.home.menu_frame_button_4 = customtkinter.CTkLabel(main.home, fg_color="transparent", text = '', image=main.home.menu_button_4)
        main.home.menu_frame_button_4.grid(row=2, column=1)

        main.home.menu_frame_button_5 = customtkinter.CTkLabel(main.home, fg_color="transparent", text = '', image=main.home.menu_button_5)
        main.home.menu_frame_button_5.grid(row=2, column=2)

        main.home.menu_frame_button_6 = customtkinter.CTkLabel(main.home, fg_color="transparent", text = '', image=main.home.menu_button_6)
        main.home.menu_frame_button_6.grid(row=2, column=3)



        def change_frame_1(event):
           main.button_menu_1_event()

        def change_frame_2(event):
           main.button_menu_2_event()

        def change_frame_3(event):
           main.button_menu_3_event()

        def change_frame_4(event):
           main.button_menu_4_event()

        def change_frame_5(event):
           main.button_menu_5_event()

        def change_frame_6(event):
           main.button_menu_6_event()

        main.home.menu_frame_button_1.bind('<Button-1>', change_frame_1)        
        main.home.menu_frame_button_2.bind('<Button-1>', change_frame_2) 
        main.home.menu_frame_button_3.bind('<Button-1>', change_frame_3) 
        main.home.menu_frame_button_4.bind('<Button-1>', change_frame_4) 
        main.home.menu_frame_button_5.bind('<Button-1>', change_frame_5) 
        main.home.menu_frame_button_6.bind('<Button-1>', change_frame_6) 

    ### MENU_1 FRAIME ###
    def create_menu_1_frame(main):
        main.geometry(f"{800}x{600}")

        main.home = customtkinter.CTkFrame(main)
        main.home.grid(row=0, column=0, sticky="nsew")

        main.home.columnconfigure(index=0, minsize=80)
        
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")

        main.home.menu_1_background_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "background.png")), size=(800,600))
        main.home.menu_1_frame_background = customtkinter.CTkLabel(main.home, text="", image=main.home.menu_1_background_image)
        main.home.menu_1_frame_background.grid(row=0, column=0, sticky='NSEW', rowspan = 5, columnspan = 7)
        

        main.home.menu_1_button_1 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "menu_button_1.png")), size=(150,150))

        main.home.menu_1_frame_button = customtkinter.CTkLabel(main.home, fg_color="transparent", text = '', image=main.home.menu_1_button_1)
        main.home.menu_1_frame_button.grid(row=4, column=0)

        def change_frame(event):
           main.button_menu_event()

        main.home.menu_1_frame_button.bind('<Button-1>', change_frame)
        #main.geometry(f"{800}x{600}")

        #main.diary = customtkinter.CTkFrame(main)
        #main.diary.grid(row=0, column=0, sticky="nsew")
        main.data = create_db.print_dairy_data()

        # create textbox
        main.home.textbox = customtkinter.CTkTextbox(main.home, width=400, height=400)
        main.home.textbox.grid(row=0, column=0, rowspan = 4)

        for i in main.data:
            main.home.textbox.insert("0.0", str(i) + "\n\n")

        #print(main.data)
    
    ### MENU_2 FRAIME ###
    def create_menu_2_frame(main):
        pass
        # таблица с выгрузкой из базы + выход
    ### MENU_3 FRAIME ###
    def create_menu_3_frame(main):
        pass
        # таблица с выгрузкой из базы + выход
    ### MENU_4 FRAIME ###
    def create_menu_4_frame(main):
        pass
        # таблица с выгрузкой из базы + выход
    ### MENU_5 FRAIME ###
    def create_menu_5_frame(main):
        pass
        # таблица с выгрузкой из базы + выход
    ### MENU_6 FRAIME ###
    def create_menu_6_frame(main):
        pass
        # таблица с выгрузкой из базы + выход

    ### EVENT_BUTTON_MENU ###
    def button_menu_event(main):
        main.create_menu_frame()

    ### EVENT_BUTTON_MENU_1 ###
    def button_menu_1_event(main):
        main.create_menu_1_frame()

    ### EVENT_BUTTON_MENU_2 ###
    def button_menu_2_event(main):
        main.create_menu_2_frame()
    
    ### EVENT_BUTTON_MENU_3 ###
    def button_menu_3_event(main):
        main.create_menu_3_frame()
    
    ### EVENT_BUTTON_MENU_4 ###
    def button_menu_4_event(main):
        main.create_menu_4_frame()
    
    ### EVENT_BUTTON_MENU_5 ###
    def button_menu_5_event(main):
        main.create_menu_5_frame()

    ### EVENT_BUTTON_MENU_6 ###
    def button_menu_6_event(main):
        main.create_menu_6_frame()

    ### EVENT_BUTTON_EXIT ###
    def button_exit_event(main):
        main.destroy()

if __name__ == "__main__": 
    app = App()
    app.mainloop()