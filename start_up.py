from tkinter import *
from tkinter.ttk import Progressbar
import sys
import os
from PIL import Image, ImageTk

class SecureChatApp:
    def __init__(self):
        self.window = Tk()
        self.original_image = Image.open(r'images\final-removebg-preview.png')
        self.image = None  # Store PhotoImage as an instance variable
        self.setup_gui()

    def setup_gui(self):
        height = 430
        width = 530
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.window.overrideredirect(1)
        self.window.wm_attributes('-topmost', True)
        self.window.config(background='#3498db')

        self.welcome_label = Label(text='GREETING TO THE SECURE CHAT APPLICATION!', bg='#3498db',
                                   font=("yu gothic ui", 13, "bold"), fg='black')
        self.welcome_label.place(x=75, y=10)

        resized_image = self.original_image.resize((200, 200), Image.Resampling.LANCZOS)
        self.image = ImageTk.PhotoImage(resized_image)  # Store it as an instance variable

        self.bg_label = Label(self.window, image=self.image, bg='#3498db')
        self.bg_label.image = self.image  # Store the PhotoImage as an attribute of the Label
        self.bg_label.place(x=170, y=110)

        self.progress_label = Label(self.window, text="Please Wait...", font=('yu gothic ui', 13, 'bold'),
                                    fg='black', bg='#3498db')
        self.progress_label.place(x=190, y=350)

        self.progress = Progressbar(self.window, orient=HORIZONTAL, length=500, mode='determinate')
        self.progress.place(x=15, y=390)

        self.exit_btn = Button(text='x', bg='#3498db', command=self.exit_window, bd=0,
                               font=("yu gothic ui", 16, "bold"), activebackground='#3498db', fg='white')
        self.exit_btn.place(x=490, y=0)

        self.i = 0
        self.load()

    def exit_window(self):
        sys.exit(self.window.destroy())

    def top(self):
        self.window.withdraw()
        os.system("python LoginAndRegistrationPage.py")
        self.window.destroy()

    def load(self):
        if self.i <= 10:
            txt = 'Please Wait...  ' + (str(10 * self.i) + '%')
            self.progress_label.config(text=txt)
            self.progress_label.after(1000, self.load)
            self.progress['value'] = 10 * self.i
            self.i += 1
        else:
            self.top()

    def run(self):
        self.window.mainloop()

# Run the application if executed directly
if __name__ == "__main__":
    app = SecureChatApp()
    app.run()
