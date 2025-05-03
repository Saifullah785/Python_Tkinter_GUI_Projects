import tkinter as tk
from tkinter import messagebox
import mysql.connector

class DBhelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost", user="root", password="", database="hit-db-demo"
            )
            self.mycursor = self.conn.cursor()
        except:
            messagebox.showerror("Error", "Could not connect to database.")
            exit()
    
    def register(self, name, email, password):
        try:
            self.mycursor.execute(f"""
                INSERT INTO user (id, name, email, password)
                VALUES (NULL, '{name}', '{email}', '{password}');
            """)
            self.conn.commit()
            return True
        except:
            return False

    def search(self, email, password):
        self.mycursor.execute(f"""
            SELECT * FROM user WHERE email = '{email}' AND password = '{password}'
        """)
        return self.mycursor.fetchall()

    def get_profile(self, user_id):
        self.mycursor.execute(f"""
            SELECT id, name, email FROM user WHERE id = {user_id}
        """)
        return self.mycursor.fetchone()

    def update_profile(self, user_id, name, email, password):
        try:
            self.mycursor.execute(f"""
                UPDATE user SET name = '{name}', email = '{email}', password = '{password}'
                WHERE id = {user_id}
            """)
            self.conn.commit()
            return True
        except:
            return False

    def delete_profile(self, user_id):
        try:
            self.mycursor.execute(f"DELETE FROM user WHERE id = {user_id}")
            self.conn.commit()
            return True
        except:
            return False


class FlipkartApp:
    def __init__(self, root):
        self.db = DBhelper()
        self.root = root
        self.root.title("PD User App")
        self.root.geometry("400x400")
        self.user_id = None
        self.login_screen()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login_screen(self):
        self.clear_window()
        tk.Label(self.root, text="Login", font=("Arial", 20)).pack(pady=10)
        
        tk.Label(self.root, text="Email").pack()
        email = tk.Entry(self.root)
        email.pack()

        tk.Label(self.root, text="Password").pack()
        password = tk.Entry(self.root, show='*')
        password.pack()

        def do_login():
            data = self.db.search(email.get(), password.get())
            if data:
                self.user_id = data[0][0]
                messagebox.showinfo("Success", f"Welcome {data[0][1]}")
                self.profile_menu()
            else:
                messagebox.showerror("Error", "Invalid credentials")

        tk.Button(self.root, text="Login", command=do_login).pack(pady=5)
        tk.Button(self.root, text="Register", command=self.register_screen).pack()

    def register_screen(self):
        self.clear_window()
        tk.Label(self.root, text="Register", font=("Arial", 20)).pack(pady=10)

        tk.Label(self.root, text="Name").pack()
        name = tk.Entry(self.root)
        name.pack()

        tk.Label(self.root, text="Email").pack()
        email = tk.Entry(self.root)
        email.pack()

        tk.Label(self.root, text="Password").pack()
        password = tk.Entry(self.root, show="*")
        password.pack()

        def do_register():
            if self.db.register(name.get(), email.get(), password.get()):
                messagebox.showinfo("Success", "Registration successful")
                self.login_screen()
            else:
                messagebox.showerror("Error", "Registration failed")

        tk.Button(self.root, text="Submit", command=do_register).pack(pady=5)
        tk.Button(self.root, text="Back to Login", command=self.login_screen).pack()

    def profile_menu(self):
        self.clear_window()
        tk.Label(self.root, text="User Profile Menu", font=("Arial", 20)).pack(pady=10)

        tk.Button(self.root, text="View Profile", command=self.view_profile).pack(pady=5)
        tk.Button(self.root, text="Edit Profile", command=self.edit_profile).pack(pady=5)
        tk.Button(self.root, text="Delete Profile", command=self.delete_profile).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.login_screen).pack(pady=5)

    def view_profile(self):
        profile = self.db.get_profile(self.user_id)
        if profile:
            messagebox.showinfo("Profile", f"ID: {profile[0]}\nName: {profile[1]}\nEmail: {profile[2]}")
        else:
            messagebox.showerror("Error", "Profile not found")

    def edit_profile(self):
        self.clear_window()
        tk.Label(self.root, text="Edit Profile", font=("Arial", 20)).pack(pady=10)

        user = self.db.get_profile(self.user_id)
        name_var = tk.StringVar(value=user[1])
        email_var = tk.StringVar(value=user[2])
        password_var = tk.StringVar()

        tk.Label(self.root, text="Name").pack()
        name_entry = tk.Entry(self.root, textvariable=name_var)
        name_entry.pack()

        tk.Label(self.root, text="Email").pack()
        email_entry = tk.Entry(self.root, textvariable=email_var)
        email_entry.pack()

        tk.Label(self.root, text="New Password").pack()
        password_entry = tk.Entry(self.root, textvariable=password_var, show="*")
        password_entry.pack()

        def submit_update():
            if self.db.update_profile(self.user_id, name_var.get(), email_var.get(), password_var.get()):
                messagebox.showinfo("Success", "Profile updated successfully")
                self.profile_menu()
            else:
                messagebox.showerror("Error", "Update failed")

        tk.Button(self.root, text="Update", command=submit_update).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.profile_menu).pack()

    def delete_profile(self):
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete your profile?")
        if confirm:
            if self.db.delete_profile(self.user_id):
                messagebox.showinfo("Deleted", "Your profile has been deleted.")
                self.login_screen()
            else:
                messagebox.showerror("Error", "Failed to delete profile")


if __name__ == "__main__":
    root = tk.Tk()
    app = FlipkartApp(root)
    root.mainloop()
