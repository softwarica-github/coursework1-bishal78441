from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox
import re
import os
import bcrypt

window = Tk()
window.geometry("1330x700")
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.title('Login and Registration Page')

# Window Icon Photo
icon = PhotoImage(file='images\\pic-icon.png')
window.iconphoto(True, icon)

LoginPage = Frame(window)
RegistrationPage = Frame(window)

for frame in (LoginPage, RegistrationPage):
    frame.grid(row=0, column=0, sticky='nsew')


def show_frame(frame):
    frame.tkraise()


show_frame(LoginPage)


# ========== DATABASE VARIABLES ============
Email = StringVar()
FullName = StringVar()
Password = StringVar()
ConfirmPassword = StringVar()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="chat"
)

cursor = db.cursor()


design_frame1 = Listbox(LoginPage, bg='#0c71b9', width=115,
                        height=50, highlightthickness=0, borderwidth=0)
design_frame1.place(x=0, y=0)

design_frame2 = Listbox(LoginPage, bg='#1e85d0', width=115,
                        height=50, highlightthickness=0, borderwidth=0)
design_frame2.place(x=676, y=0)

design_frame3 = Listbox(LoginPage, bg='#1e85d0', width=100,
                        height=33, highlightthickness=0, borderwidth=0)
design_frame3.place(x=75, y=106)

design_frame4 = Listbox(LoginPage, bg='#f8f8f8', width=100,
                        height=33, highlightthickness=0, borderwidth=0)
design_frame4.place(x=676, y=106)

# ====== Email ====================
email_entry = Entry(design_frame4, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,
                    textvariable=Email)
email_entry.place(x=134, y=170, width=256, height=34)
email_entry.config(highlightbackground="black", highlightcolor="black")
email_label = Label(design_frame4, text='• Email account',
                    fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
email_label.place(x=130, y=140)

# ==== Password ==================
password_entry1 = Entry(design_frame4, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2,
                        textvariable=Password)
password_entry1.place(x=134, y=250, width=256, height=34)
password_entry1.config(highlightbackground="black", highlightcolor="black")
password_label = Label(design_frame4, text='• Password',
                       fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
password_label.place(x=130, y=220)


# function for show and hide password
def password_command():
    if password_entry1.cget('show') == '•':
        password_entry1.config(show='')
    else:
        password_entry1.config(show='•')


# ====== checkbutton ==============
checkButton = Checkbutton(design_frame4, bg='#f8f8f8',
                          command=password_command, text='show password')
checkButton.place(x=140, y=288)

# ========= Buttons ===============
SignUp_button = Button(LoginPage, text='Sign up', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                       command=lambda: show_frame(RegistrationPage), borderwidth=0, activebackground='#1b87d2', cursor='hand2')
SignUp_button.place(x=1100, y=175)

# ===== Welcome Label ==============
welcome_label = Label(design_frame4, text='Welcome',
                      font=('Arial', 20, 'bold'), bg='#f8f8f8')
welcome_label.place(x=130, y=15)

# ======= top Login Button =========
login_button = Button(LoginPage, text='Login', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      borderwidth=0, activebackground='#1b87d2', cursor='hand2')
login_button.place(x=845, y=175)

login_line = Canvas(LoginPage, width=60, height=5, bg='#1b87d2')
login_line.place(x=840, y=203)

# ==== LOGIN  down button ============
loginBtn1 = Button(design_frame4, fg='#f8f8f8', text='Login', bg='#1b87d2', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1b87d2', command=lambda: login())
loginBtn1.place(x=133, y=340, width=256, height=50)


# ======= ICONS =================

# ===== Email icon =========
email_icon = Image.open('images\\email-icon.png')
photo = ImageTk.PhotoImage(email_icon)
emailIcon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
emailIcon_label.image = photo
emailIcon_label.place(x=105, y=174)

# ===== password icon =========
password_icon = Image.open('images\\pass-icon.png')
photo = ImageTk.PhotoImage(password_icon)
password_icon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
password_icon_label.image = photo
password_icon_label.place(x=105, y=254)

# ===== picture icon =========
picture_icon = Image.open('images\\pic-icon.png')
photo = ImageTk.PhotoImage(picture_icon)
picture_icon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
picture_icon_label.image = photo
picture_icon_label.place(x=280, y=5)

# ===== Left Side Picture ============
side_image = Image.open(r'images\\final-removebg-preview.png')
photo = ImageTk.PhotoImage(side_image)
side_image_label = Label(design_frame3, image=photo, bg='#1e85d0')
side_image_label.image = photo
side_image_label.place(x=150, y=150)


def login():
    global db, cursor

    try:
        cursor.execute("SELECT * FROM user WHERE Email = %s AND Password = %s",
                       (email_entry.get(), password_entry1.get()))
        result = cursor.fetchall()

        if result:
            if result[0][5] == 'admin':
                window.withdraw()  # Hide the current window
                os.system("python admin.py")
                window.destroy()
            else:
                window.withdraw()  # Hide the current window
                os.system("python home.py")
                window.destroy()
        else:
            # User does not exist
            response = messagebox.askquestion(
                "User not found", "Do you want to register?")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error accessing database: {err}")


# ================================================================================================================
# === FORGOT PASSWORD  PAGE =========================================================================================
def forgot_password():
    def password_command():
        if new_password_entry.cget('show') == '•':
            new_password_entry.config(show='')
        else:
            new_password_entry.config(show='•')

        if confirm_password_entry.cget('show') == '•':
            confirm_password_entry.config(show='')
        else:
            confirm_password_entry.config(show='•')

    win = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(
        f'{window_width}x{window_height}+{position_right}+{position_top}')
    win.title('Forgot Password')
    win.iconbitmap('images\\aa.ico')
    win.configure(background='#f8f8f8')
    win.resizable(0, 0)

    # Variables
    email = StringVar()
    password = StringVar()
    confirmPassword = StringVar()

    # ====== Email ====================
    email_entry2 = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,
                         textvariable=email)
    email_entry2.place(x=40, y=30, width=256, height=34)
    email_entry2.config(highlightbackground="black", highlightcolor="black")
    email_label2 = Label(win, text='• Email account', fg="#89898b", bg='#f8f8f8',
                         font=("yu gothic ui", 11, 'bold'))
    email_label2.place(x=40, y=0)

    # ====  New Password ==================
    new_password_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2,
                               textvariable=password)
    new_password_entry.place(x=40, y=110, width=256, height=34)
    new_password_entry.config(
        highlightbackground="black", highlightcolor="black")
    new_password_label = Label(win, text='• New Password', fg="#89898b",
                               bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
    new_password_label.place(x=40, y=80)

    checkButton1 = Checkbutton(
        win, bg='#f8f8f8', command=password_command, text='Show Password')
    checkButton1.place(x=190, y=148)

    # ====  Confirm Password ==================
    confirm_password_entry = Entry(win, fg="#a7a7a7", font=(
        "yu gothic ui semibold", 12), show='•', highlightthickness=2, textvariable=confirmPassword)
    confirm_password_entry.place(x=40, y=190, width=256, height=34)
    confirm_password_entry.config(
        highlightbackground="black", highlightcolor="black")
    confirm_password_label = Label(win, text='• Confirm Password', fg="#89898b", bg='#f8f8f8',
                                   font=("yu gothic ui", 11, 'bold'))
    confirm_password_label.place(x=40, y=160)

    # checkButton2 = Checkbutton(win, bg='#f8f8f8', command=password_command, text='Show Password')
    # checkButton2.place(x=190, y=165)

    # ======= Update password Button ============
    update_pass = Button(win, fg='#f8f8f8', text='Update Password', bg='#1b87d2', font=("yu gothic ui bold", 14),
                         cursor='hand2', activebackground='#1b87d2', command=lambda: change_password())
    update_pass.place(x=40, y=240, width=256, height=50)

    # ========= DATABASE CONNECTION FOR FORGOT PASSWORD=====================

    def change_password():
        new_password = new_password_entry.get()
        confirm_password = confirm_password_entry.get()

        # Check password format
        if not re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', new_password):
            messagebox.showerror('Error!', 'New password must be at least 8 characters long and include a combination of an uppercase letter, a digit, and a special character.')
            return

        if new_password == confirm_password:
            try:
                db = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="chat"
                )
                cursor = db.cursor()

                # Hash the new password using bcrypt
                hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

                update_query = "UPDATE user SET Password = %s, ConfirmPassword = %s WHERE Email = %s"
                data = (hashed_password, hashed_password, email_entry2.get())

                cursor.execute(update_query, data)
                db.commit()
                db.close()

                messagebox.showinfo('Congrats', 'Password changed successfully')

            except mysql.connector.Error as err:
                messagebox.showerror('Error!', f"Error updating password: {err}")

        else:
            messagebox.showerror('Error!', "Passwords didn't match")


forgotPassword = Button(design_frame4, text='Forgot password', font=("yu gothic ui", 8, "bold underline"), bg='#f8f8f8',
                        borderwidth=0, activebackground='#f8f8f8', command=lambda: forgot_password(), cursor="hand2")
forgotPassword.place(x=290, y=290)


# =====================================================================================================================
# =====================================================================================================================
# ==================== REGISTRATION PAGE ==============================================================================

design_frame5 = Listbox(RegistrationPage, bg='#0c71b9',
                        width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame5.place(x=0, y=0)

design_frame6 = Listbox(RegistrationPage, bg='#1e85d0',
                        width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame6.place(x=676, y=0)

design_frame7 = Listbox(RegistrationPage, bg='#1e85d0',
                        width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame7.place(x=75, y=106)

design_frame8 = Listbox(RegistrationPage, bg='#f8f8f8',
                        width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame8.place(x=676, y=106)

# ==== Full Name =======
name_entry = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,
                   textvariable=FullName)
name_entry.place(x=284, y=150, width=286, height=34)
name_entry.config(highlightbackground="black", highlightcolor="black")
name_label = Label(design_frame8, text='•Full Name', fg="#89898b",
                   bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
name_label.place(x=280, y=120)

# ======= Email ===========
email_entry = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,
                    textvariable=Email)
email_entry.place(x=284, y=220, width=286, height=34)
email_entry.config(highlightbackground="black", highlightcolor="black")
email_label = Label(design_frame8, text='•Email', fg="#89898b",
                    bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
email_label.place(x=280, y=190)


# ====== Password =========
password_entry = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2,
                       textvariable=Password)
password_entry.place(x=284, y=295, width=286, height=34)
password_entry.config(highlightbackground="black", highlightcolor="black")
password_label = Label(design_frame8, text='• Password', fg="#89898b", bg='#f8f8f8',
                       font=("yu gothic ui", 11, 'bold'))
password_label.place(x=280, y=265)


def password_command():
    if password_entry1.cget('show') == '•':
        password_entry1.config(show='')
    else:
        password_entry1.config(show='•')


def password_command2():
    if password_entry.cget('show') == '•':
        password_entry.config(show='')
        confirmPassword_entry.config(show='')
    else:
        password_entry.config(show='•')
        confirmPassword_entry.config(show='•')


# ====== Confirm Password =============
confirmPassword_entry = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,
                              textvariable=ConfirmPassword)
confirmPassword_entry.place(x=284, y=385, width=286, height=34)
confirmPassword_entry.config(
    highlightbackground="black", highlightcolor="black")
confirmPassword_label = Label(design_frame8, text='• Confirm Password', fg="#89898b", bg='#f8f8f8',
                              font=("yu gothic ui", 11, 'bold'))
confirmPassword_label.place(x=280, y=355)

checkButton = Checkbutton(design_frame8, bg='#f8f8f8',
                          command=password_command2, text='show password')
checkButton.place(x=290, y=330)
# ========= Buttons ====================
SignUp_button = Button(RegistrationPage, text='Sign up', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                       command=lambda: show_frame(LoginPage), borderwidth=0, activebackground='#1b87d2', cursor='hand2')
SignUp_button.place(x=1100, y=175)

SignUp_line = Canvas(RegistrationPage, width=60, height=5, bg='#1b87d2')
SignUp_line.place(x=1100, y=203)

# ===== Welcome Label ==================
welcome_label = Label(design_frame8, text='Welcome',
                      font=('Arial', 20, 'bold'), bg='#f8f8f8')
welcome_label.place(x=130, y=15)

# ========= Login Button =========
login_button = Button(RegistrationPage, text='Login', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      borderwidth=0, activebackground='#1b87d2', command=lambda: show_frame(LoginPage), cursor='hand2')
login_button.place(x=845, y=175)

# ==== SIGN UP down button ============
signUp2 = Button(design_frame8, fg='#f8f8f8', text='Sign Up', bg='#1b87d2', font=("yu gothic ui bold", 15),
                 cursor='hand2', activebackground='#1b87d2', command=lambda: submit())
signUp2.place(x=285, y=435, width=286, height=50)

# ===== password icon =========
password_icon = Image.open('images\\pass-icon.png')
photo = ImageTk.PhotoImage(password_icon)
password_icon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
password_icon_label.image = photo
password_icon_label.place(x=255, y=300)

# ===== confirm password icon =========
confirmPassword_icon = Image.open('images\\pass-icon.png')
photo = ImageTk.PhotoImage(confirmPassword_icon)
confirmPassword_icon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
confirmPassword_icon_label.image = photo
confirmPassword_icon_label.place(x=255, y=390)

# ===== Email icon =========
email_icon = Image.open('images\\email-icon.png')
photo = ImageTk.PhotoImage(email_icon)
emailIcon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
emailIcon_label.image = photo
emailIcon_label.place(x=255, y=225)

# ===== Full Name icon =========
name_icon = Image.open('images\\name-icon.png')
photo = ImageTk.PhotoImage(name_icon)
nameIcon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
nameIcon_label.image = photo
nameIcon_label.place(x=252, y=153)

# ===== picture icon =========
picture_icon = Image.open('images\\pic-icon.png')
photo = ImageTk.PhotoImage(picture_icon)
picture_icon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
picture_icon_label.image = photo
picture_icon_label.place(x=280, y=5)

# ===== Left Side Picture ============
side_image = Image.open(r'images\\final-removebg-preview.png')
photo = ImageTk.PhotoImage(side_image)
side_image_label = Label(design_frame7, image=photo, bg='#1e85d0')
side_image_label.image = photo
side_image_label.place(x=150, y=150)

# heading = Label(window, text='Secure Chat Application', fg='#00FF00', font=("yu gothic ui", 19, "bold"), bg='#1e85d0')
# heading.place(x=210, y=560)



def submit():
    global db, cursor

    check_counter = 0
    warn = ""

    if name_entry.get() == "":
        warn = "Full Name can't be empty"
    else:
        check_counter += 1

    if email_entry.get() == "" or not re.match(r'^[a-zA-Z0-9_.+-]+@gmail\.com$', email_entry.get()):
        warn = "Invalid email format"
    else:
        check_counter += 1

    if password_entry.get() == "":
        warn = "Password can't be empty"
    elif not re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password_entry.get()):
        warn = "Passwords must be at least 8 characters long and include a combination of an uppercase letter, a digit, and a special character for enhanced security."
    else:
        check_counter += 1

    if confirmPassword_entry.get() == "":
        warn = "Confirm Password can't be empty"
    elif password_entry.get() != confirmPassword_entry.get():
        warn = "Passwords didn't match!"
    else:
        check_counter += 1

    if check_counter == 4:
        try:
            # Hash the password using bcrypt
            hashed_password = bcrypt.hashpw(password_entry.get().encode('utf-8'), bcrypt.gensalt())

            cursor.execute("INSERT INTO user (Email, FullName, Password, ConfirmPassword, UserRole) VALUES (%s, %s, %s, %s, %s)",
                           (email_entry.get(), name_entry.get(), hashed_password, hashed_password, 'user'))

            db.commit()
            messagebox.showinfo("Success", "New account created successfully")

            # Clear the form fields
            name_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            confirmPassword_entry.delete(0, END)

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error accessing database: {err}")

    else:
        messagebox.showerror('Error', warn)


window.mainloop()
