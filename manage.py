from tkinter import *
from tkinter import ttk, messagebox, simpledialog
import mysql.connector
import os

class AdminManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title('AdminManagementPage')

        # Database Connection
        self.db_admin = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="chat"
        )

        self.cursor_admin = self.db_admin.cursor()

        # UI Setup
        self.setup_ui()

    def setup_ui(self):
        frame_admin = Frame(self.root)
        frame_admin.pack(pady=20)

        self.user_tree = ttk.Treeview(frame_admin, columns=(1, 2, 3, 4, 5), show="headings", height=15)
        self.user_tree.pack(side=LEFT)

        self.user_tree.heading(1, text="ID")
        self.user_tree.heading(2, text="Email")
        self.user_tree.heading(3, text="Full Name")
        self.user_tree.heading(4, text="Password")
        self.user_tree.heading(5, text="UserRole")

        scrollbar = ttk.Scrollbar(frame_admin, orient="vertical", command=self.user_tree.yview)
        scrollbar.pack(side=RIGHT, fill="y")
        self.user_tree.configure(yscrollcommand=scrollbar.set)

        delete_button = Button(self.root, text="Delete User", command=self.delete_user)
        delete_button.place(x=250, y=400)

        refresh_button = Button(self.root, text="Refresh Panel", command=self.refresh_panel)
        refresh_button.place(x=350, y=400)

        add_button = Button(self.root, text="Add User", command=self.add_user)
        add_button.place(x=460, y=400)

        see_log_button = Button(self.root, text="See Logs", command=self.log)
        see_log_button.place(x=550, y=400)

        back_button = Button(self.root, text="Go back", command=self.go_back)
        back_button.place(x=640, y=400)

        self.show_users()

    def delete_user(self):
        selected_item = self.user_tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a user to delete")
            return

        user_id = self.user_tree.item(selected_item, 'values')[0]
        try:
            self.cursor_admin.execute("DELETE FROM user WHERE id = %s", (user_id,))
            self.db_admin.commit()
            self.show_users()
            messagebox.showinfo("Success", "User deleted successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error deleting user: {err}")


    def add_user(self):
        os.system("python admin_add_user.py")

    def show_users(self):
        try:
            self.cursor_admin.execute("SELECT id, Email, FullName, Password, UserRole FROM user")
            rows = self.cursor_admin.fetchall()

            # Clear existing items in the tree
            self.user_tree.delete(*self.user_tree.get_children())

            for row in rows:
                self.user_tree.insert("", "end", values=row)

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error accessing database: {err}")


    def log(self):
        os.system("python admin_log.py")

    def refresh_panel(self):
        self.root.destroy()
        os.system("python manage.py")

    def go_back(self):
        self.root.destroy()
        os.system("python admin.py")

if __name__ == "__main__":
    window_admin = Tk()
    app = AdminManagementApp(window_admin)
    window_admin.mainloop()
