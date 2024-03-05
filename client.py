import tkinter as tk

from tkinter import scrolledtext

import socket

import threading



HOST = '127.0.0.1'

PORT = 5500



class ChatApplication:

    def __init__(self, root):

        self.root = root

        self.root.title("ChatApp")

        self.root.configure(bg="#1e3d59")  



        self.username_label = tk.Label(root, text="Enter your username:", bg="#1e3d59", fg="white", font=("Comic Sans MS", 12))  # Text color and font

        self.username_label.grid(row=0, column=0, padx=10, pady=5)



        self.username_entry = tk.Entry(root, width=30)

        self.username_entry.grid(row=0, column=1, padx=10, pady=5)



        self.confirm_button = tk.Button(root, text="Confirm", command=self.confirm_username, bg="#41b3a3", fg="white")  # Button color

        self.confirm_button.grid(row=0, column=2, padx=10, pady=5)



        self.chat_box = scrolledtext.ScrolledText(root, width=40, height=10, bg="#eef5db", font=("Comic Sans MS", 15))  # Font, and background color

        self.chat_box.grid(row=1, column=0, padx=10, pady=10, columnspan=3)



        self.entry_label = tk.Label(root, text="Enter your message:", bg="#1e3d59", fg="white", font=("Comic Sans MS", 12))  # Text color and font

        self.entry_label.grid(row=2, column=0, padx=10, pady=5)



        self.entry_field = tk.Entry(root, width=30)

        self.entry_field.grid(row=2, column=1, padx=10, pady=5)

        self.entry_field.bind('<Return>', self.send_message_on_enter)



        self.send_button = tk.Button(root, text="Send", command=self.send_message, state=tk.DISABLED, bg="#f8961e", fg="white")  # Button color

        self.send_button.grid(row=2, column=2, padx=10, pady=5)



        self.username = None

        self.client = None



    def confirm_username(self):

        self.username = self.username_entry.get()

        if self.username:

            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            self.client.connect((HOST, PORT))

            self.confirm_button.config(state=tk.DISABLED)

            self.username_entry.config(state=tk.DISABLED)

            self.send_button.config(state=tk.NORMAL)

            receive_thread = threading.Thread(target=self.receive)

            receive_thread.start()



    def send_message(self, event=None):

        message = self.entry_field.get()

        if message:

            self.client.send(f"{self.username}: {message}".encode('utf-8'))

            self.entry_field.delete(0, 'end')



    def send_message_on_enter(self, event):

        self.send_message()



    def receive(self):

        while True:

            try:

                message = self.client.recv(1024).decode('utf-8')

                username = message.split(':', 1)[0]  # Extract username from message

                message_body = message.split(':', 1)[1]  # Extract message body from message

                self.chat_box.tag_config("username", foreground="#008000")  # Configuring tag for username color

                self.chat_box.insert(tk.END, username + ":", "username")  # Applying tag to username

                self.chat_box.insert(tk.END, message_body + '\n')  # Appending the rest of the message

                self.chat_box.see(tk.END)

                self.chat_box.update()

            except:

                break



root = tk.Tk()

app = ChatApplication(root)

root.mainloop()

