#App Name: Virtual ATM Login
#Login Password: 12345
#Python Version 3.5
#Developper: Larry Georges Muala

import tkinter
from tkinter import messagebox

window_login = tkinter.Tk()

#window title
window_login.title('Virtual ATM')

#window size
window_login.geometry("190x220")

#code to disable maximize
window_login.resizable(0,0)

#window background color
window_login.configure(background="light slate gray")

#modify icons
#window_login.wm_iconbitmap('lelu.ico')


#Menu Bar

def about_app():
	print("App Name: Virtual ATM Login Form")
	print("App Description: ATM Login with 3 attempts security check")
	print("Virtual ATM Pin ~ 12345 ~")
	print("Python Version 3.5")
	print("Developper: Larry Georges Muala")
	
	messagebox.showinfo("App Info", "App Name: Virtual ATM Login Form\n" + 
						"\nApp description:  ATM Login with 3 attempts security check\n" + 
						"\nVirtual ATM Pin ~ 12345 ~\n" +
						"\nPython Version 3.5 \n" + 
						"\nDevelopper: Larry Georges Muala")

menubar = tkinter.Menu(window_login)
myMenu = tkinter.Menu(menubar, tearoff=0)
myMenu.add_command(label="About", command=about_app)
myMenu.add_separator()
myMenu.add_command(label="Exit", command=window_login.quit)
menubar.add_cascade(label="App Info", menu=myMenu)

#display the menu
window_login.config(menu=menubar)


#Login form
lbl_main = tkinter.Label(window_login, text="ATM", font=("Helvetica", 20), bg="gray1", fg="white")
lbl_main.pack(fill=tkinter.X)

#blank label for space separator
lbl_blank = tkinter.Label(window_login, text=" ", bg="light slate gray")
lbl_blank.pack()

#welcome label
lbl_name = tkinter.Label(window_login, text="Welcome to the Virtual ATM", bg="light slate gray")
lbl_name.pack()

lbl_pin = tkinter.Label(window_login, text="Please enter your PIN", bg="light slate gray")
lbl_pin.pack()

#pin text entry
ent_pin = tkinter.Entry(window_login, show="*")
ent_pin.pack()
ent_pin.focus()

#counter security value
count = 3

#login function
def login_check():

	var_pin = ent_pin.get()
	password = 12345
	
	global count
	
	if var_pin.isdigit():
	
		var_pin = int(var_pin)
		
		if var_pin == password:
			messagebox.showinfo("Successful", "Login Successful")
			window_login.destroy()
			
		else:
			messagebox.showerror("Error", "Incorrect Password" + "\n   Attempts left: " + str(count - 1))
			ent_pin.delete(0, tkinter.END)
			ent_pin.focus()
			count -= 1
			print(count)
	else:
		messagebox.showerror("Error", "Incorrect Password" + "\n   Attempts left: " + str(count - 1))
		ent_pin.delete(0, tkinter.END)
		ent_pin.focus()
		count -= 1
		print(count)
	
	if count == 0:
		messagebox.showerror("Error", "   Incorrect Password" + "\nTransaction Canceled")
		window_login.destroy()

#login button		
btn_login = tkinter.Button(window_login, text="Login", command=login_check)
btn_login.pack()

#blank label for space separator
lbl_blank = tkinter.Label(window_login, text=" ", bg="light slate gray")
lbl_blank.pack()


window_login.mainloop()