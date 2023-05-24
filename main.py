import customtkinter
import os
from PIL import Image

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(main):
        super().__init__()

        ### create main frame ###

        main.title("Книжная полка")
        main.geometry(f"{600}x{450}")

        x = (main.winfo_screenwidth() - main.winfo_reqwidth()) / 4
        y = (main.winfo_screenheight() - main.winfo_reqheight()) / 4

        main.wm_geometry("+%d+%d" % (x, y))
        main.resizable(False, False)

        main.columnconfigure(index=0, minsize=600)
        main.rowconfigure(index=0, minsize=450)

        main.create_home_frame()

    ### create frame ###

    def create_home_frame(main):
        ### create home frame ###

        main.home = customtkinter.CTkFrame(main)
        main.home.grid(row=0, column=0, sticky="nsew")

        main.home.columnconfigure(index=0, minsize=100)
        main.home.columnconfigure(index=1, minsize=300)
        main.home.rowconfigure(index=0, minsize=100)

        for i in range(1, 4):
            main.home.columnconfigure(index=i, minsize=50)

        
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")

        main.home.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home_label.png")), size=(300,300))
        main.home.logo_image_1 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home_label_1.png")), size=(600,70))
        main.home.diary_button_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "diary_button.png")), size=(200, 50))
        main.home.add_book_button_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "add_book_button.png")), size=(200, 50))
        main.home.about_button_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "about_button.png")), size=(200, 50))
        main.home.exit_button_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "exit_button.png")), size=(200, 50))

        main.home.home_frame_label = customtkinter.CTkLabel(main.home, text="", image=main.home.logo_image)
        main.home.home_frame_label.grid(row=1, column=0, sticky='NSEW', rowspan = 4, pady=10)

        main.home.home_frame_label_1 = customtkinter.CTkLabel(main.home, text="", image=main.home.logo_image_1)
        main.home.home_frame_label_1.grid(row=0, column=0, sticky='NSEW', columnspan = 2, pady=10)

        # create home button
        main.home.diary_button = customtkinter.CTkButton(main.home, command=main.diary_button_event, fg_color="transparent", text = '', image=main.home.diary_button_image, hover_color="#e5e5e5")
        main.home.diary_button.grid(row=1, column=1, padx=5, pady=5, sticky='NSEW')

        main.home.add_book_button = customtkinter.CTkButton(main.home, command=main.add_book_button_event, fg_color="transparent", text = '', image=main.home.add_book_button_image, hover_color="#e5e5e5")
        main.home.add_book_button.grid(row=2, column=1, padx=5, pady=5, sticky='NSEW')

        main.home.about_button = customtkinter.CTkButton(main.home, command=main.about_button_event, fg_color="transparent", text = '', image=main.home.about_button_image, hover_color="#e5e5e5")
        main.home.about_button.grid(row=3, column=1, padx=5, pady=5, sticky='NSEW')

        main.home.exit_button = customtkinter.CTkButton(main.home, command=main.exit_button_event, fg_color="transparent", text = '', image=main.home.exit_button_image, hover_color="#e5e5e5")
        main.home.exit_button.grid(row=4, column=1, padx=5, pady=5, sticky='NSEW')

    def create_diary_frame(main):
        main.diary = customtkinter.CTkFrame(main)
        main.diary.grid(row=0, column=0, sticky="nsew")

        main.diary.columnconfigure(index=0, minsize=300)
        main.diary.columnconfigure(index=1, minsize=300)
        main.diary.rowconfigure(index=0, minsize=50)
        main.diary.rowconfigure(index=1, minsize=200)
        main.diary.rowconfigure(index=2, minsize=150)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")

        main.diary.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "dairy_label.png")), size=(500,50))
        main.diary.back_button_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "back_button.png")), size=(200, 50))

        main.diary.logo = customtkinter.CTkLabel(main.diary, text="", image=main.diary.logo_image)
        main.diary.logo.grid(row=0, column=0, sticky='NSEW', columnspan = 2, pady=10)
        
        main.diary.diary_table = customtkinter.CTkLabel(main.diary, text=create_db.print_dairy_data())
        main.diary.diary_table.grid(row=1, column=0, sticky='NSEW', columnspan = 2)

        main.diary.back_button = customtkinter.CTkButton(main.diary, command=main.back_button_event, fg_color="transparent", text = '', image=main.diary.back_button_image, hover_color="#e5e5e5")
        main.diary.back_button.grid(row=2, column=1, sticky='S')

    def create_add_book_frame(main):
        pass

    def create_about_frame(main):
        main.about = customtkinter.CTkFrame(main)
        main.about.grid(row=0, column=0, sticky="nsew")

        main.about.columnconfigure(index=0, minsize=300)
        main.about.columnconfigure(index=1, minsize=300)
        main.about.rowconfigure(index=0, minsize=50)
        main.about.rowconfigure(index=1, minsize=200)
        main.about.rowconfigure(index=2, minsize=150)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")

        main.about.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "about_label.png")), size=(500,50))
        main.about.about_text_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "about_text.png")), size=(600, 200))
        main.about.back_button_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "back_button.png")), size=(200, 50))

        main.about.logo = customtkinter.CTkLabel(main.about, text="", image=main.about.logo_image)
        main.about.logo.grid(row=0, column=0, sticky='NSEW', columnspan = 2, pady=10)

        main.about.about_text = customtkinter.CTkLabel(main.about, text="", image=main.about.about_text_image)
        main.about.about_text.grid(row=1, column=0, sticky='NSEW', columnspan = 2)

        main.about.back_button = customtkinter.CTkButton(main.about, command=main.back_button_event, fg_color="transparent", text = '', image=main.about.back_button_image, hover_color="#e5e5e5")
        main.about.back_button.grid(row=2, column=1, sticky='S')

    ### create button event ###

    def diary_button_event(main):
        main.create_diary_frame()

    def add_book_button_event(main):
        main.create_add_book_frame()

    def about_button_event(main):
        main.create_about_frame()

    def exit_button_event(main):
        main.destroy()

    def back_button_event(main):
        main.create_home_frame()

if __name__ == "__main__": 
    app = App()
    app.mainloop()