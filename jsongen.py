import tkinter as tk
import json

def save():
    data = {
        "executable_name": executable_name_entry.get(),
        "program_name": program_name_entry.get(),
        "github_repo": github_repo_entry.get(),
        "folder_remove": folder_remove_var.get(),
        "delete_zerobyte": delete_zerobyte_var.get()
    }
    with open('management.json', 'w') as f:
        json.dump(data, f)
    root.destroy()

root = tk.Tk()
root.title("Configuration")

tk.Label(root, text="Executable Name").grid(row=0)
tk.Label(root, text="Program Name").grid(row=1)
tk.Label(root, text="GitHub Repository").grid(row=2)
tk.Label(root, text="Remove Folder").grid(row=3)
tk.Label(root, text="Delete Zerobyte").grid(row=4)

executable_name_entry = tk.Entry(root)
program_name_entry = tk.Entry(root)
github_repo_entry = tk.Entry(root)
folder_remove_var = tk.BooleanVar()
folder_remove_checkbutton = tk.Checkbutton(root, variable=folder_remove_var)
delete_zerobyte_var = tk.BooleanVar()
delete_zerobyte_checkbutton = tk.Checkbutton(root, variable=delete_zerobyte_var)

executable_name_entry.grid(row=0, column=1)
program_name_entry.grid(row=1, column=1)
github_repo_entry.grid(row=2, column=1)
folder_remove_checkbutton.grid(row=3, column=1)
delete_zerobyte_checkbutton.grid(row=4, column=1)

tk.Button(root, text='Save', command=save).grid(row=5, column=0, sticky=tk.W, pady=4)

tk.mainloop()
