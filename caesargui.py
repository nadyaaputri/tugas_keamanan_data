import tkinter as tk
from tkinter import messagebox

# Fungsi enkripsi Caesar Cipher
def enkripsi(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isupper():
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            cipher_text += char
    return cipher_text

# Fungsi deskripsi Caesar Cipher
def deskripsi(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plain_text += char
    return plain_text

# GUI untuk Caesar Cipher
class CaesarCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher")

        # Label dan Input untuk teks asli (plaintext)
        tk.Label(root, text="Teks Asli (Plaintext):").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.input_text = tk.Entry(root, width=50)
        self.input_text.grid(row=0, column=1, padx=10, pady=10)

        # Label dan Input untuk nilai pergeseran (shift)
        tk.Label(root, text="Nilai Pergeseran (1-25):").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.shift_value = tk.Entry(root, width=10)
        self.shift_value.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Label dan Input untuk hasil
        tk.Label(root, text="Hasil:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.result_text = tk.Entry(root, width=50, state='readonly')
        self.result_text.grid(row=2, column=1, padx=10, pady=10)

        # Tombol untuk enkripsi dan deskripsi
        tk.Button(root, text="Enkripsi", command=self.encrypt_message).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(root, text="Dekripsi", command=self.decrypt_message).grid(row=3, column=1, padx=10, pady=10, sticky="w")

    def encrypt_message(self):
        plain_text = self.input_text.get()
        shift = self.get_shift_value()
        if plain_text and shift is not None:
            cipher_text = enkripsi(plain_text, shift)
            self.update_result(cipher_text)

    def decrypt_message(self):
        cipher_text = self.input_text.get()
        shift = self.get_shift_value()
        if cipher_text and shift is not None:
            plain_text = deskripsi(cipher_text, shift)
            self.update_result(plain_text)

    def get_shift_value(self):
        try:
            shift = int(self.shift_value.get())
            if 1 <= shift <= 25:
                return shift
            else:
                messagebox.showerror("Error", "Nilai pergeseran harus antara 1 dan 25!")
        except ValueError:
            messagebox.showerror("Error", "Nilai pergeseran harus berupa angka!")
        return None

    def update_result(self, result):
        self.result_text.config(state='normal')
        self.result_text.delete(0, tk.END)
        self.result_text.insert(0, result)
        self.result_text.config(state='readonly')

if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()
