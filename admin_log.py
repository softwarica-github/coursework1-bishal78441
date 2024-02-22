import datetime
import tkinter as tk
from tkinter import Text, Scrollbar

class ChatLogViewer:
    def __init__(self, master=None, log_file="chat_log.txt"):
        self.log_file = log_file

        # Use the provided master or create a Toplevel instance
        if master is not None:
            self.window = master
        else:
            self.window = tk.Toplevel()

        self.window.title("Chat Logs")

        # Create a Text widget for displaying logs
        self.log_text = Text(self.window, wrap=tk.WORD, height=20, width=500)
        self.log_text.pack(side=tk.LEFT, fill=tk.Y)

        # Create a Scrollbar for the Text widget
        self.scrollbar = Scrollbar(self.window, command=self.log_text.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text.config(yscrollcommand=self.scrollbar.set)

        # Call the view_logs function when needed
        self.view_logs()

    def view_logs(self):
        try:
            with open(self.log_file, "r") as file:
                logs = file.readlines()

            if not logs:
                self.log_text.insert(tk.END, "No logs available.\n")
                return

            self.log_text.insert(tk.END, "=== Chat Logs ===\n")
            current_user = None

            for log in logs:
                log = log.strip()
                if log.startswith("User:"):
                    user = log.split(":")[1].strip()
                    if user != current_user:
                        self.log_text.insert(tk.END, f"\n{user}:\n")
                        current_user = user
                    else:
                        self.log_text.insert(tk.END, "\n")
                else:
                    self.log_text.insert(tk.END, log + "\n")
        except FileNotFoundError:
            self.log_text.insert(tk.END, "Log file not found.\n")

if __name__ == "__main__":
    root = tk.Tk()
    chat_log_viewer = ChatLogViewer(master=root)
    root.mainloop()
