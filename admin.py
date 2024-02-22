from tkinter import Tk, Frame, Label, Button, Canvas, PhotoImage, Toplevel, Text, Scrollbar
from PIL import Image, ImageTk
import os

class FirstPage:
    def __init__(self, dashboard_window):
        self.dashboard_window = dashboard_window
        self.app_width = 1340
        self.app_height = 690
        self.setup_window()
        self.setup_window_icon()
        self.setup_frames()
        self.setup_homepage()

    def setup_window(self):
        self.dashboard_window.rowconfigure(0, weight=1)
        self.dashboard_window.columnconfigure(0, weight=1)
        screen_width = self.dashboard_window.winfo_screenwidth()
        screen_height = self.dashboard_window.winfo_screenheight()
        x = (screen_width / 2) - (self.app_width / 2)
        y = (screen_height / 160) - (self.app_height / 160)
        self.dashboard_window.geometry(f"{self.app_width}x{self.app_height}+{int(x)}+{int(y)}")

    def setup_window_icon(self):
        icon = PhotoImage(file=r'images\\final-removebg-preview2.png')
        self.dashboard_window.iconphoto(True, icon)
        self.dashboard_window.title('Secure Chat Application')

    def setup_frames(self):
        self.homepage = Frame(self.dashboard_window)
        dashboard_page = Frame(self.dashboard_window)

        for frame in (self.homepage, dashboard_page):
            frame.grid(row=0, column=0, sticky='nsew')

        def show_frame(frame):
            frame.tkraise()
        show_frame(self.homepage)

    def setup_homepage(self):
        homepage = self.homepage
        homepage.config(background='#ffffff')

        self.setup_menu_bar()
        self.setup_background_image()  # Check this method for the correct image path
        self.setup_admin_section()
        self.setup_heading_labels()
        self.setup_slider()
        self.setup_buttons()

    def setup_menu_bar(self):
        logoIcon = Image.open(r'images\\final-removebg-preview1.png')
        photo = ImageTk.PhotoImage(logoIcon)
        logo = Label(self.homepage, image=photo, bg='#ffffff')
        logo.image = photo
        logo.place(x=0, y=0)

        menuBar_line = Canvas(self.homepage, width=1500, height=1.5, bg="#e6e6e6", highlightthickness=0)
        menuBar_line.place(x=0, y=60)

    def setup_background_image(self):
        # Check the image path here
        home_bgImg = Image.open(r'C:\Users\asus\Desktop\Semester-3rd\programming_and_algorithium-2\project\secure_Chat_Application\images\wp9109411.png')
        home_bgImg = home_bgImg.resize((self.app_width, self.app_height), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(home_bgImg)
        home_bg = Label(self.homepage, image=photo, bg='#ffffff')
        home_bg.image = photo
        home_bg.place(x=0, y=60)

    def setup_admin_section(self):
        admIcon = Image.open('images\\feeling.png')
        photo = ImageTk.PhotoImage(admIcon)
        adm = Label(self.homepage, image=photo, bg='#ffffff')
        adm.image = photo
        adm.place(x=1260, y=5)

        admLabel = Label(self.homepage, text='Admin', font=('yu gothic ui', 18, 'bold'), fg='#ffc329', bg='#ffffff')
        admLabel.place(x=1180, y=11)

    def setup_heading_labels(self):
        heading = Label(self.homepage, text='© Secure Chat Application', bg='black', fg='#ff6c38',
                        font=("yu gothic ui", 19, "bold"))
        heading.place(x=1000, y=630)

    def setup_slider(self):
        count = 0
        heading_text = "Empowering Connections, Ensuring Security:\nWhere Every Message Matters"

        label = Label(self.homepage, text="", font=('Arial', 30, "bold"), fg='orange', bg='black')
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

    def setup_buttons(self):
        home_button = Button(self.homepage, text='Home', bg='#fd6a36', font=("", 13, "bold"), bd=0, fg='white',
                             cursor='hand2', activebackground='#fd6a36', activeforeground='white')
        home_button.place(x=70, y=15)

        def manage():
            self.dashboard_window.withdraw()
            os.system("python manage.py")
            self.dashboard_window.destroy()

        self.manage_button = Button(self.homepage, text='Manage User', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                    fg='#7a7a7a',
                                    cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',
                                    command=manage)
        self.manage_button.place(x=150, y=15)

        def logout():
            self.dashboard_window.withdraw()
            os.system("python LoginAndRegistrationPage.py")
            self.dashboard_window.destroy()

        product_button = Button(self.homepage, text='Logout', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                                cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',
                                command=logout)
        product_button.place(x=275, y=15)

        def get_help_content():
            help_content = """
            Welcome to Secure Chat Application Help!

            Secure Chat Application is a user-friendly application that allows you to securely
            communicate with others. Below are the key features of the application:

            Features:
            - Home: Return to the home page.
            - Logout: Log out of the application.
            - Help: Display this help message.
            - Start Server: Start a new Server session.
            - Administrator: Access the administrator panel.

            Chat Features:
            - Text Messages: Send and receive text messages securely.
            - Group Chat: Create and participate in group chat sessions.

            Security Measures:
            - End-to-End Encryption: All messages and files are encrypted for privacy.
            - Two-Factor Authentication: Enhance the security of your account.
            - Secure Connection: Your data is transmitted over a secure connection.

            User Management (Administrator Only):
            - Add User: Add a new user to the system.
            - Delete User: Remove an existing user from the system.
            - Manage Users: View and update user information.

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

        help_button = Button(self.homepage, text='Help', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                             cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a', command=help)
        help_button.place(x=360, y=15)

        def rset():
            os.system("python server.py")

        rset_button = Button(self.homepage, text='Start Server', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                             cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a', command=rset)
        rset_button.place(x=420, y=15)

def page():
    window = Tk()
    FirstPage(window)
    window.mainloop()

if __name__ == '__main__':
    page()
