from tkinter import *
from tkinter import messagebox, filedialog

# Functions
def open_file():
    file = filedialog.askopenfilename()
    if file:
        listbox.insert(END, file)

def show_selected():
    try:
        selected = listbox.get(listbox.curselection())
        messagebox.showinfo("Selected Item", selected)
    except:
        messagebox.showwarning("Warning", "No item selected")

def delete_item():
    try:
        listbox.delete(listbox.curselection())
    except:
        messagebox.showerror("Error", "Select an item to delete")

def exit_app():
    root.quit()

# Main window
root = Tk()
root.title("GUI Application")
root.geometry("400x400")

# Menu Bar
menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# Menubutton
mb = Menubutton(root, text="Options", relief=RAISED)
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu

mb.menu.add_command(label="Show Selected", command=show_selected)
mb.menu.add_command(label="Delete Selected", command=delete_item)

mb.pack(pady=10)

# Frame for Listbox and Scrollbar
frame = Frame(root)
frame.pack()

# Scrollbar
scrollbar = Scrollbar(frame)

# Listbox
listbox = Listbox(frame, width=40, height=10, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

scrollbar.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT)

# Buttons
btn_open = Button(root, text="Open File", command=open_file)
btn_open.pack(pady=5)

btn_show = Button(root, text="Show Selected", command=show_selected)
btn_show.pack(pady=5)

btn_delete = Button(root, text="Delete Selected", command=delete_item)
btn_delete.pack(pady=5)

# Run application
root.mainloop()