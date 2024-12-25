import tkinter as tk
from tkinter import messagebox

# Enigma Cipher sederhana
class EnigmaCipher:
    def __init__(self, rotors):
        self.rotors = rotors

    def encrypt(self, text):
        result = []
        for i, char in enumerate(text):
            if char.isalpha():
                shift = self.rotors[i % len(self.rotors)]
                base = ord('A') if char.isupper() else ord('a')
                result.append(chr((ord(char) - base + shift) % 26 + base))
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, text):
        result = []
        for i, char in enumerate(text):
            if char.isalpha():
                shift = self.rotors[i % len(self.rotors)]
                base = ord('A') if char.isupper() else ord('a')
                result.append(chr((ord(char) - base - shift) % 26 + base))
            else:
                result.append(char)
        return ''.join(result)

# GUI untuk aplikasi Enigma Cipher
class EnigmaApp:
    def __init__(self, root):  # Fixed the typo here (from _init_ to __init__)
        self.root = root
        self.root.title("Enigma Cipher Sederhana")
        
        # Default rotor settings
        self.rotors = [3, 1, 4]

        # Label dan Input
        tk.Label(root, text="Pesan:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.input_text = tk.Entry(root, width=50)
        self.input_text.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="Hasil:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.result_text = tk.Entry(root, width=50, state='readonly')
        self.result_text.grid(row=1, column=1, padx=10, pady=10)

        # Tombol Enkripsi dan Dekripsi
        tk.Button(root, text="Enkripsi", command=self.encrypt_message).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(root, text="Dekripsi", command=self.decrypt_message).grid(row=2, column=1, padx=10, pady=10, sticky="w")

    def encrypt_message(self):
        message = self.input_text.get()
        if not message:
            messagebox.showerror("Error", "Pesan tidak boleh kosong!")
            return
        cipher = EnigmaCipher(self.rotors)
        encrypted_message = cipher.encrypt(message)
        self.result_text.config(state='normal')
        self.result_text.delete(0, tk.END)
        self.result_text.insert(0, encrypted_message)
        self.result_text.config(state='readonly')

    def decrypt_message(self):
        message = self.input_text.get()
        if not message:
            messagebox.showerror("Error", "Pesan tidak boleh kosong!")
            return
        cipher = EnigmaCipher(self.rotors)
        decrypted_message = cipher.decrypt(message)
        self.result_text.config(state='normal')
        self.result_text.delete(0, tk.END)
        self.result_text.insert(0, decrypted_message)
        self.result_text.config(state='readonly')

if __name__ == "__main__":
    root = tk.Tk()
    app = EnigmaApp(root)
    root.mainloop()
