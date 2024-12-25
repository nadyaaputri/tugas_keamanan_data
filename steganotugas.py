import tkinter as tk
from tkinter import filedialog, messagebox
from stegano import lsb
import os

def hide_message():
    def perform_hide():
        image_path = entry_image_path.get()
        message = entry_message.get("1.0", tk.END).strip()
        save_path = entry_save_path.get()

        if not os.path.exists(image_path) or not image_path.endswith(('.png', '.jpg')):
            messagebox.showerror("Error", "Invalid image file path.")
            return

        if not message:
            messagebox.showerror("Error", "Message cannot be empty.")
            return

        try:
            secret_image = lsb.hide(image_path, message)
            secret_image.save(save_path)
            messagebox.showinfo("Success", f"Message hidden and saved to {save_path}")
            hide_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    hide_window = tk.Toplevel(root)
    hide_window.title("Hide Message")

    tk.Label(hide_window, text="Image Path:").grid(row=0, column=0, padx=10, pady=10)
    entry_image_path = tk.Entry(hide_window, width=50)
    entry_image_path.grid(row=0, column=1, padx=10, pady=10)
    tk.Button(hide_window, text="Browse", command=lambda: entry_image_path.insert(0, filedialog.askopenfilename())).grid(row=0, column=2, padx=10, pady=10)

    tk.Label(hide_window, text="Message:").grid(row=1, column=0, padx=10, pady=10)
    entry_message = tk.Text(hide_window, width=50, height=10)
    entry_message.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

    tk.Label(hide_window, text="Save Path:").grid(row=2, column=0, padx=10, pady=10)
    entry_save_path = tk.Entry(hide_window, width=50)
    entry_save_path.grid(row=2, column=1, padx=10, pady=10)
    tk.Button(hide_window, text="Browse", command=lambda: entry_save_path.insert(0, filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")]))).grid(row=2, column=2, padx=10, pady=10)

    tk.Button(hide_window, text="Hide Message", command=perform_hide).grid(row=3, column=1, pady=10)

def reveal_message():
    def perform_reveal():
        image_path = entry_image_path.get()

        if not os.path.exists(image_path) or not image_path.endswith(('.png', '.jpg')):
            messagebox.showerror("Error", "Invalid image file path.")
            return

        try:
            hidden_message = lsb.reveal(image_path)
            if hidden_message:
                messagebox.showinfo("Hidden Message", hidden_message)
            else:
                messagebox.showinfo("Info", "No hidden message found in the image.")
            reveal_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    reveal_window = tk.Toplevel(root)
    reveal_window.title("Reveal Message")

    tk.Label(reveal_window, text="Image Path:").grid(row=0, column=0, padx=10, pady=10)
    entry_image_path = tk.Entry(reveal_window, width=50)
    entry_image_path.grid(row=0, column=1, padx=10, pady=10)
    tk.Button(reveal_window, text="Browse", command=lambda: entry_image_path.insert(0, filedialog.askopenfilename())).grid(row=0, column=2, padx=10, pady=10)

    tk.Button(reveal_window, text="Reveal Message", command=perform_reveal).grid(row=1, column=1, pady=10)

# Main Application
root = tk.Tk()
root.title("Steganography App")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Hide Message", command=hide_message)
file_menu.add_command(label="Reveal Message", command=reveal_message)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

tk.Label(root, text="Welcome to Steganography App", font=("Arial", 16)).pack(pady=20)

tk.Button(root, text="Hide a Message", command=hide_message, width=20).pack(pady=10)
tk.Button(root, text="Reveal a Message", command=reveal_message, width=20).pack(pady=10)

root.mainloop()