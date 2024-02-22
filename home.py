
from tkinter import Tk, Frame, Label, Button, Canvas, PhotoImage, Toplevel
import os
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageOps, ImageColor, ImageFile, ImagePalette, ImageStat
from tkinter import messagebox
from tkinter import Toplevel, Text, Scrollbar, END

class UserChatApp:
    def __init__(self, dashboard_window):
        self.dashboard_window = dashboard_window
        self.homepage = Frame(dashboard_window)

        # Window Size and Placement
        dashboard_window.rowconfigure(0, weight=1)
        dashboard_window.columnconfigure(0, weight=1)
        screen_width = dashboard_window.winfo_screenwidth()
        screen_height = dashboard_window.winfo_height()
        app_width = 1340
        app_height = 690
        x = (screen_width/2)-(app_width/2)
        y = (screen_height/160)-(app_height/160)
        dashboard_window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        # window Icon
        icon = PhotoImage(file=r'images\chat_3icon.png')
        dashboard_window.iconphoto(True, icon)
        dashboard_window.title('Secure Chat Application')

        # Navigating through windows
        homepage = Frame(dashboard_window)
        dashboard_page = Frame(dashboard_window)

        for frame in (homepage, dashboard_page):
            frame.grid(row=0, column=0, sticky='nsew')


        def show_frame(frame):
            frame.tkraise()


        show_frame(homepage)

        # ======================================================================================
        # =================== HOME PAGE ========================================================
        # ======================================================================================
        homepage.config(background='#ffffff')

        # ====== MENU BAR ==========
        logoIcon = Image.open(r'images\\chat_icon1.png')
        photo = ImageTk.PhotoImage(logoIcon)
        logo = Label(homepage, image=photo, bg='#ffffff')
        logo.image = photo
        logo.place(x=0, y=0)


        menuBar_line = Canvas(homepage, width=1500, height=1.5, bg="#e6e6e6", highlightthickness=0)
        menuBar_line.place(x=0, y=60)

        home_bgImg = Image.open(r'C:\Users\asus\Desktop\Semester-3rd\programming_and_algorithium-2\project\secure_Chat_Application\images\wp9109411.png')
        home_bgImg = home_bgImg.resize((app_width, app_height), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(home_bgImg)
        home_bg = Label(homepage, image=photo, bg='#ffffff')
        home_bg.image = photo
        home_bg.place(x=0, y=60)

      

        admIcon = Image.open('images\\feeling.png')
        photo = ImageTk.PhotoImage(admIcon)
        adm = Label(homepage, image=photo, bg='#ffffff')
        adm.image = photo
        adm.place(x=1260, y=5)

        admLabel = Label(homepage, text='User', font=('yu gothic ui', 18, 'bold'), fg='#ffc329', bg='#ffffff')
        admLabel.place(x=1200, y=11)

        heading = Label(homepage, text='© Secure Chat Application', bg='black', fg='#ff6c38', font=("yu gothic ui", 17, "bold" ))
        heading.place(x=1000, y=630)

        count = 0
        heading_text = "Empowering Connections, Ensuring Security:\nWhere Every Message Matters"

        label = Label(homepage, text="", font=('Arial', 30, "bold"), fg='orange', bg='black')
        label.pack(pady=100)

                
        def slider():
            nonlocal count, heading_text
            if count >= len(heading_text):
                count = 0
                label.config(text="")
            else:
                label.config(text=heading_text[:count + 1])
            count += 1
            label.after(100, slider)

        slider()

        # ========== HOME BUTTON =======
        home_button = Button(homepage, text='Home', bg='#fd6a36', font=("", 13, "bold"), bd=0, fg='white',
                             cursor='hand2', activebackground='#fd6a36', activeforeground='white')
        home_button.place(x=70, y=15)

        def manage():
            dashboard_window.withdraw()
            os.system("python LoginAndRegistrationPage.py")
            dashboard_window.destroy()

        # ========== MANAGE BUTTON =======
        manage_button = Button(homepage, text='Logout', bg='#fd6a36', font=("", 13, "bold"), bd=0, fg='white',
                             cursor='hand2', activebackground='#fd6a36', activeforeground='white', command= manage)
        manage_button.place(x=150, y=15)


        def get_help_content():
            help_content = """
            Welcome to Secure Chat Application Help!

            Secure Chat Application is a user-friendly application that allows you to securely
            communicate with others. Below are the key features of the application:

            Features:
            - Home: Return to the home page.
            - Logout: Log out of the application.
            - Help: Display this help message.
            - Start Chat: Start a new chat session.
            - Administrator: Access the administrator panel.

            Chat Features:
            - Text Messages: Send and receive text messages securely.
            - Group Chat: Create and participate in group chat sessions.

            Security Measures:
            - End-to-End Encryption: All messages and files are encrypted for privacy.
            - Two-Factor Authentication: Enhance the security of your account.
            - Secure Connection: Your data is transmitted over a secure connection.

            GitHub Repository:
            - Secure Chat Application GitHub Repository: [GitHub - Secure Chat Application](https://github.com/bishal78441)

            For more detailed information and updates, please visit the GitHub repository.

            If you encounter any issues or have suggestions, feel free to open an issue on GitHub.

            Thank you for using Secure Chat Application!
            """
            return help_content


        def help():
            help_text = get_help_content()
            win = Toplevel()
            window_width = 1366
            window_height = 768
            screen_width = win.winfo_screenwidth()
            screen_height = win.winfo_screenheight()
            position_top = int(screen_height / 4 - window_height / 4)
            position_right = int(screen_width / 2 - window_width / 2)
            win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

            win.resizable(0, 0)

    
            text_widget = Text(win, wrap="word", font=("Arial", 12), padx=10, pady=10)
            text_widget.insert("1.0", help_text)
            text_widget.configure(state="disabled")

            scrollbar = Scrollbar(win, command=text_widget.yview)
            scrollbar.pack(side="right", fill="y")

            text_widget.pack(expand=True, fill="both")
            text_widget.config(yscrollcommand=scrollbar.set)

        # Assuming `homepage` and other imports are correctly set up
        help_button = Button(homepage, text='Help', bg='#fd6a36', font=("", 13, "bold"), bd=0, fg='white',
                            cursor='hand2', activebackground='#fd6a36', activeforeground='white', command=help)
        help_button.place(x=230, y=15)

        def logout():
            dashboard_window.withdraw()
            os.system("python LoginAndRegistrationPage.py")
            dashboard_window.destroy()

        def rset():
            os.system("python client.py")

        rset_button = Button(homepage, text='Start Chat', bg='#fd6a36', font=("", 13, "bold"), bd=0, fg='white',
                             cursor='hand2', activebackground='#fd6a36', activeforeground='white', command=rset)
        rset_button.place(x=290, y=15)

        home_button = Button(homepage, text='Administrator', bg='#fd6a36', font=("", 13, "bold"), bd=0, fg='white',
                             cursor='hand2', activebackground='#fd6a36', activeforeground='white', command=manage)
        home_button.place(x=390, y=15)


def create_chat_app():
    window = Tk()
    UserChatApp(window)
    window.mainloop()


if __name__ == '__main__':
    create_chat_app()
