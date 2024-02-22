import tkinter as tk
from tkinter import ttk
import mysql.connector
import bcrypt
import re

class AddUserWindow:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Add User")

        # Create and place labels and entry widgets
        self.email_label = tk.Label(parent, text="Email:")
        self.email_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.email_entry = tk.Entry(parent)
        self.email_entry.grid(row=0, column=1, padx=10, pady=10)

        self.full_name_label = tk.Label(parent, text="Full Name:")
        self.full_name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.full_name_entry = tk.Entry(parent)
        self.full_name_entry.grid(row=1, column=1, padx=10, pady=10)

        self.password_label = tk.Label(parent, text="Password:")
        self.password_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.password_entry = tk.Entry(parent, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)

        self.confirm_password_label = tk.Label(parent, text="Confirm Password:")
        self.confirm_password_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.confirm_password_entry = tk.Entry(parent, show="*")
        self.confirm_password_entry.grid(row=3, column=1, padx=10, pady=10)

        self.user_role_label = tk.Label(parent, text="User Role:")
        self.user_role_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.user_roles = ["admin", "User"]
        self.user_role_combobox = ttk.Combobox(parent, values=self.user_roles)
        self.user_role_combobox.grid(row=4, column=1, padx=10, pady=10)

        # Create and place the Add User button
        self.add_user_button = tk.Button(parent, text="Add User", command=self.add_user)
        self.add_user_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Create and place a label for displaying the result
        self.result_label = tk.Label(parent, text="", fg="green")
        self.result_label.grid(row=6, column=0, columnspan=2, pady=10)

    def insert_query(self, email, full_name, password, confirm_password, user_role):
        connection = None
        try:
            # Check email format
            if not re.match(r'^[a-zA-Z0-9_.+-]+@gmail\.com$', email):
                raise ValueError("Invalid email format")

            # Check password format
            if not re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password):
                raise ValueError("Passwords must be at least 8 characters long and include a combination of an uppercase letter, a digit, and a special character for enhanced security.")

            # Encrypt the password using bcrypt
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            # Replace the placeholder values with your MySQL server details
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="chat"
            )

            cursor = connection.cursor()

            # Insert data into the database
            query = "INSERT INTO user (Email, FullName, Password, ConfirmPassword, UserRole) VALUES (%s, %s, %s, %s, %s)"
            data = (email, full_name, hashed_password, hashed_password, user_role)
            cursor.execute(query, data)

            connection.commit()
            self.result_label.config(text="User added successfully.", fg="green")

        except ValueError as ve:
            self.result_label.config(text=f"Error: {ve}", fg="red")

        except mysql.connector.Error as err:
            self.result_label.config(text=f"Error: {err}", fg="red")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def add_user(self):
        email = self.email_entry.get()
        full_name = self.full_name_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        user_role = self.user_role_combobox.get()

        # Basic validation
        if not email or not full_name or not password or not confirm_password:
            self.result_label.config(text="Please fill in all fields.", fg="red")
            return
        elif password != confirm_password:
            self.result_label.config(text="Passwords do not match.", fg="red")
            return

        # Insert data into the database
        self.insert_query(email, full_name, password, confirm_password, user_role)

        # Clear the input fields
        self.email_entry.delete(0, tk.END)
        self.full_name_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.confirm_password_entry.delete(0, tk.END)
        self.user_role_combobox.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = AddUserWindow(root)
    root.mainloop()
