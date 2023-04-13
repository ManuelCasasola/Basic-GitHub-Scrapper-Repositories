from tkinter import *
from tkinter import ttk



def create_gui(search_callback):
    root = Tk()
    root.configure(bg="#F4F6F6")

    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12), foreground="blue")
    style.configure("TLabel", font=("Helvetica", 12))
    style.configure("Treeview.Heading", font=("Helvetica", 14))

    frame1 = Frame(root, bg="#F4F6F6")
    frame1.pack(pady=10)

    label = ttk.Label(frame1, text="Nombre de usuario de GitHub: ")
    label.grid(row=0, column=0)

    entry = ttk.Entry(frame1)
    entry.grid(row=0, column=1)

    button = ttk.Button(frame1, text="Buscar", command=lambda: search_callback(entry.get()))
    button.grid(row=0,column=2)

    frame2 = Frame(root, bg="#F4F6F6")
    frame2.pack(pady=10)

    tree = ttk.Treeview(frame2, columns=("No", "Repo", "URL"), show="headings")
    tree.heading("No", text="No")
    tree.heading("Repo", text="Repo")
    tree.heading("URL", text="URL")
    tree.pack(fill=BOTH, expand=True)

    return root, tree