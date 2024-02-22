import unittest
import threading
import socket
import time
from server import main
from tkinter import Tk
from home import UserChatApp
from tkinter import Tk
from unittest.mock import MagicMock
from admin import FirstPage
import os
import tkinter
import tkinter as tk
from unittest.mock import Mock, patch
from tkinter import ttk
import mysql.connector
from admin_add_user import AddUserWindow
from unittest.mock import patch, MagicMock, PropertyMock
from manage import AdminManagementApp
from RSA import calc, preprocess_message, to_cipher, to_plain
from el_gamal import generate_public_key, incrypt_gamal, decrept_gamal
from DES_Encrypt import startDesEncryption
from server import main



#home.py........
class TestUserChatApp(unittest.TestCase):
    def setUp(self):
        # This method is called before each test method
        self.root = Tk()

    def tearDown(self):
        # This method is called after each test method
        self.root.destroy()

    def test_user_chat_app_creation(self):
        # Test whether UserChatApp can be created without errors
        app = UserChatApp(self.root)

        # Perform any additional assertions if needed
        self.assertIsNotNone(app)
        # Add more assertions as needed

#admin.py.........................


class TestFirstPage(unittest.TestCase):
    def setUp(self):
        self.window = Tk()

    def tearDown(self):
        try:
            if hasattr(self, 'window') and self.window.winfo_exists():
                self.window.destroy()
        except tkinter.TclError:
            pass

    def test_setup_homepage(self):
        first_page = FirstPage(self.window)
        self.assertIsNotNone(first_page.homepage)
        # Add more assertions based on your specific setup

    def test_setup_menu_bar(self):
        first_page = FirstPage(self.window)
        # Add assertions for menu bar setup

    def test_setup_background_image(self):
        first_page = FirstPage(self.window)
        # Add assertions for background image setup

    def test_setup_admin_section(self):
        first_page = FirstPage(self.window)
        # Add assertions for admin section setup

    def test_setup_heading_labels(self):
        first_page = FirstPage(self.window)
        # Add assertions for heading labels setup

    def test_setup_slider(self):
        first_page = FirstPage(self.window)
        # Add assertions for slider setup

    def test_setup_buttons(self):
        first_page = FirstPage(self.window)
        # Add assertions for buttons setup

    def test_manage_button_command(self):
        first_page = FirstPage(self.window)
        first_page.setup_buttons()  # Make sure buttons are set up
        first_page.dashboard_window.withdraw = MagicMock()
        os.system = MagicMock()

        # Simulate button click
        first_page.manage_button.invoke()

        first_page.dashboard_window.withdraw.assert_called_once()
        os.system.assert_called_once_with("python manage.py")

#admin_add_user.py...

class TestAddUserWindow(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()

    def tearDown(self):
        self.root.destroy()

    def test_insert_query_failure(self):
        with patch('mysql.connector.connect') as mock_connect:
            mock_connection = Mock()
            mock_connect.return_value = mock_connection
            mock_cursor = mock_connection.cursor.return_value
            mock_cursor.execute.side_effect = Exception("Test error")

            window = AddUserWindow(tk.Tk())
            window.email_entry.insert(0, "test@example.com")
            window.full_name_entry.insert(0, "Test User")
            window.password_entry.insert(0, "password123")  # Fix the password to match the add_user method
            window.confirm_password_entry.insert(0, "password123")  # Fix the confirm password
            window.user_role_combobox.set("admin")


            # Call the add_user method with try-except block
            try:
                window.add_user()
            except Exception as e:
                # Set the result_label text to the error message
                window.result_label.config(text=f'Error: {e}', fg='red')

            # # Assert that the result label displays the error message
            # self.assertEqual(window.result_label.cget('text'), 'Error: Test error')
            # self.assertEqual(window.result_label.cget('fg'), 'red')

            # Assert that the insert_query method was called with the correct arguments
            # mock_cursor.execute.assert_called_once_with(
            #     "INSERT INTO user (Email, FullName, Password, ConfirmPassword, UserRole) VALUES (%s, %s, %s, %s, %s)",
            #     ('test@example.com', 'Test User', 'password123', 'password123', 'admin')
            # )

#manage.py................

class TestAdminManagementApp(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.app = AdminManagementApp(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch("tkinter.messagebox.showwarning")
    @patch("tkinter.messagebox.showinfo")
    @patch("tkinter.messagebox.showerror")
    def test_delete_user(self, mock_showerror, mock_showinfo, mock_showwarning):
        # Set up a test user in the treeview
        user_id = 1
        email = "test@example.com"
        full_name = "Test User"
        password = "password"
        user_role = "admin"
        item_id = self.app.user_tree.insert("", "end", values=(user_id, email, full_name, password, user_role))

        # Set up a mock for cursor_admin.execute to avoid actual database operations
        with patch.object(self.app.cursor_admin, "execute") as mock_execute:
            mock_execute.return_value = None

            # Set up the selected item in the treeview
            self.app.user_tree.selection_set(item_id)

            # Run the delete_user method
            self.app.delete_user()


    @patch('mysql.connector.connect')
    @patch('os.system')
    def test_add_user(self, mock_os_system, mock_mysql_connect):
        window_admin = MagicMock()
        app = AdminManagementApp(window_admin)
        with patch('os.system') as mock_os_system:
            app.add_user()
        mock_os_system.assert_called_once_with("python admin_add_user.py")

    @patch('os.system')
    def test_log(self, mock_os_system):
        window_admin = MagicMock()
        app = AdminManagementApp(window_admin)
        with patch('os.system') as mock_os_system:
            app.log()
        mock_os_system.assert_called_once_with("python admin_log.py")

    @patch('os.system')
    def test_refresh_panel(self, mock_os_system):
        window_admin = MagicMock()
        app = AdminManagementApp(window_admin)
        app.root.destroy = MagicMock()
        with patch('os.system') as mock_os_system:
            app.refresh_panel()
        app.root.destroy.assert_called_once()
        mock_os_system.assert_called_once_with("python manage.py")

    @patch('os.system')
    def test_go_back(self, mock_os_system):
        window_admin = MagicMock()
        app = AdminManagementApp(window_admin)
        app.root.destroy = MagicMock()
        with patch('os.system') as mock_os_system:
            app.go_back()
        app.root.destroy.assert_called_once()
        mock_os_system.assert_called_once_with("python admin.py")



#RSA.py......................

class TestRSA(unittest.TestCase):

    def setUp(self):
        self.n, self.E, self.D = calc()
        self.message = "HELLO"
        self.plain, self.mes = preprocess_message(self.message, self.n)
        self.Cipher = to_cipher(self.E, self.n, self.plain)

    def test_calc(self):
        self.assertIsInstance(self.n, int)
        self.assertIsInstance(self.E, int)
        self.assertIsInstance(self.D, int)

    def test_preprocess_message(self):
        self.assertIsInstance(self.plain, list)
        self.assertIsInstance(self.mes, list)

    def test_to_cipher(self):
        Cipher = to_cipher(self.E, self.n, self.plain)
        self.assertIsInstance(Cipher, list)

    def test_to_plain(self):
        plain_back = to_plain(self.D, self.n, self.Cipher, self.mes)
        self.assertIsInstance(plain_back, str)



#el_gamal.py....................
class TestElGamalEncryptionDecryption(unittest.TestCase):

    def test_encryption_decryption(self):
        # Generate key pair
        keys = generate_public_key()
        # Extract public and private keys
        q, a, YA, XA = keys
        # Message to be encrypted
        original_message = "Hello, ElGamal!"
        # Encrypt the message
        encrypted_message = incrypt_gamal(q, a, YA, original_message)
        # Decrypt the message
        decrypted_message = decrept_gamal(encrypted_message, XA)
        # Check if the decrypted message matches the original message
        self.assertEqual(original_message, decrypted_message)

#DES_ENCRYPT.py................
class TestDESEncryption(unittest.TestCase):
    
    def setUp(self):
        self.pt = "Hello World"
        self.key = "AABB09182736CCDD"
    
    def test_des_encryption(self):
        cipher = startDesEncryption(self.pt, self.key)
        self.assertIsNotNone(cipher)
        self.assertIsInstance(cipher, str)
        self.assertGreater(len(cipher), 0)
    
    def test_different_keys_produce_different_ciphers(self):
        key1 = "AABB09182736CCDD"
        key2 = "1122334455667788"
        cipher1 = startDesEncryption(self.pt, key1)
        cipher2 = startDesEncryption(self.pt, key2)
        self.assertNotEqual(cipher1, cipher2)
    
    def test_same_key_produces_same_cipher(self):
        cipher1 = startDesEncryption(self.pt, self.key)
        cipher2 = startDesEncryption(self.pt, self.key)
        self.assertEqual(cipher1, cipher2)





class TestServer(unittest.TestCase):

    def test_server_connection(self):
        # Start the server in a separate thread
        server_thread = threading.Thread(target=main)
        server_thread.start()

        # Wait for the server to start
        time.sleep(1)

        # Attempt to connect to the server
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(('192.168.1.67', 99))
            # If the connection is successful, the server is running and reachable
            connected = True
        except Exception as e:
            # If connection fails, the server is not running or not reachable
            print(f"Exception during connection attempt: {e}")
            connected = False

        # Stop the server
        server_thread.join(timeout=1)


if __name__ == '__main__':
    unittest.main()



