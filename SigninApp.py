from tkinter import *
from tkinter import messagebox
from sqlite3 import Error
import sqlite3

# INITIALIZE THE WINDOW FOR SIGN IN
root_0 = Tk()
root_0.title("Profile Simulator")
root_0.geometry("450x200")
root_0.configure(background="grey")

def connect_to_database():
	conn = sqlite3.connect('user_inf.db')
	cc = conn.cursor()
	try:
		cc.execute(""" CREATE TABLE infos (
			f_name text,
			l_name text,
			email text,
			password text
		)""")
	except Error as e:
		print(e)
	conn.commit()
	conn.close()

class Register:

	def __init__(self):

		self.root = Tk()
		self.root.title("Profile Simulator")
		self.root.geometry("450x200")
		self.root.configure(background="grey")
		
		self.name_entry = Entry(self.root, width=50)
		self.surname_entry = Entry(self.root, width=50)
		self.email_entry = Entry(self.root, width=50)
		self.password_entry = Entry(self.root, width=50)
		self.register_button = Button(self.root, text="Register",command=self.register, height=3, width=10)

		Label(self.root, text="Name: ", width=10).grid(row=0, column=0, padx=5, pady=5)
		Label(self.root, text="Surname: ", width=10).grid(row=1, column=0, padx=5, pady=5)
		Label(self.root, text="E-mail: ", width=10).grid(row=2, column=0, padx=5, pady=5)
		Label(self.root, text="Password: ", width=10).grid(row=3, column=0, padx=5, pady=5)

		self.name_entry.grid(row=0, column=1, padx=5, pady=5)
		self.surname_entry.grid(row=1, column=1, padx=5, pady=5)
		self.email_entry.grid(row=2, column=1, padx=5, pady=5)
		self.password_entry.grid(row=3, column=1, padx=5, pady=5)
		self.register_button.grid(row=4, column=1, padx=5, pady=10)

	def register(self):
		name = self.name_entry.get()
		surname = self.surname_entry.get()
		email = self.email_entry.get()
		password = self.password_entry.get()

		if name == "" or surname == "" or email == "" or password == "":
			messagebox.showerror("Messagebox", "Please fill out every form.")

		else:
			
			conn = sqlite3.connect('user_inf.db')
			c = conn.cursor()
			c.execute("INSERT INTO infos VALUES (:f_name, :l_name, :email, :password)", {
				'f_name': name,
				'l_name': surname,
				'email': email,
				'password': password
			})
			conn.commit()
			conn.close()

			self.name_entry.delete(0, END)
			self.surname_entry.delete(0, END)
			self.email_entry.delete(0, END)
			self.password_entry.delete(0, END)

			messagebox.showinfo("Messagebox", "Successfully Registered.")
			self.root.destroy()

class Sign_in:

	def __init__(self, master):

		self.email_entry = Entry(master, width=50)
		self.password_entry = Entry(master, width=50)
		self.signin_button = Button(master, text="Sign in",command=self.signin_click, height=3, width=10)
		self.register_button  = Button(master, text="Register",command=self.register_click, height=3, width=10)

		Label(master, text="E-mail: ", width=10).grid(row=0, column=0, padx=5, pady=5)
		Label(master, text="Password: ", width=10).grid(row=1, column=0, padx=5, pady=5)

		self.email_entry.grid(row=0, column=1, padx=5, pady=5)
		self.password_entry.grid(row=1, column=1, padx=5, pady=5)
		self.signin_button.grid(row=2, column=1, padx=5, pady=5)
		self.register_button.grid(row=3, column=1, padx=5, pady=5)
	
	def register_click(self):
		Register()

	def signin_click(self):

		email = self.email_entry.get()
		psw = self.password_entry.get()

		conn = sqlite3.connect("user_inf.db")
		c = conn.cursor()
		c.execute("SELECT *, oid FROM infos")
		all_users = c.fetchall()
		found = 0
		for all_info in all_users:
			if all_info[2] == email and all_info[3] == psw:
				messagebox.showinfo("Messagebox", f"Welcome to the app {all_info[0].upper()} !")
				self.email_entry.delete(0, END)
				self.password_entry.delete(0, END)
				found = 1
		if not found:
			messagebox.showerror("Messagebox", "Wrong email or password, please try again.")
		
		conn.commit()
		conn.close()

if __name__ == '__main__':
	connect_to_database()
	e = Sign_in(root_0)
	root_0.mainloop()