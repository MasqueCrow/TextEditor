from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
master = Tk()
master.title("Editor")
master.geometry("400x300")

text = Text(master, width = 400, height = 380, font = ("Andale Mono",12), highlightthickness = 0, bd = 2)
text.pack()

# Methods

def new():
	ans = messagebox.askquestion(title = "Save file", message = "Would you like to save this file")
	
	if ans == "yes":
		save()
	delete_all()


def open_file():
	new()
	file = filedialog.askopenfilename()
	with open(file, 'r') as f:
		text.insert(INSERT, f.read())


def save():
	path = filedialog.asksaveasfilename()
	write = open(path, mode = 'w')
	write.write(text.get("1.0", END))

def rename():
	pass

def close():
	save()
	master.quit()

def copy():
	master.clipboard_clear()
	text.clipboard_append(string = text.selection_get())

def cut():
	copy()
	text.delete(1.0,END)

def paste():
	text.insert(INSERT, master.clipboard_get())

def delete():
	text.delete(index1 = SEL_FIRST, index2 = SEL_LAST)

def select_all():
	text.tag_add(SEL, "1.0", END)

def delete_all():
	text.delete(1.0, END)

# **** File Menu **** #

menu = Menu(master)
master.config(menu = menu)
file_menu = Menu(menu)
menu.add_cascade(label = "File",menu = file_menu)

#command is link to the method created above
file_menu.add_command(label = "New", command = new)
file_menu.add_command(label = "Open", command = open_file)
file_menu.add_command(label="Save", command = save)
file_menu.add_separator()
file_menu.add_command(label = "Close", command = close)
file_menu.add_command(label = "Save", command = save)
file_menu.add_command(label = "Rename", command = rename)

# **** Edit Menu **** #
edit_menu = Menu(menu)
menu.add_cascade(label = "Menu", menu = edit_menu)

edit_menu.add_command(label = "Undo", command = text.edit_undo)
edit_menu.add_command(label = "", command = text.edit_redo)
edit_menu.add_separator()
edit_menu.add_command(label = "Cut", command = cut)
edit_menu.add_command(label = "Copy", command = copy)
edit_menu.add_command(label = "Paste", command = paste)
edit_menu.add_command(label = "delete", command = delete)

edit_menu.add_separator()
edit_menu.add_command(label = "Select All", command = select_all)

master.mainloop()

