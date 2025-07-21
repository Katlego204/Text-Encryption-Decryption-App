import tkinter as tk


window = tk.Tk()

window.geometry("800x500")
window.title("Encryption GUI")

# Title
label = tk.Label(window, text="Caeser Cipher", font=('Arial bold', 25))
label.pack(padx=10, pady=10)

# Textbox (Entering the text that needs Encryption)
textbox = tk.Text(window, heigh=4, font=('Arial', 35))
textbox.pack(padx=10, pady=1)

key_frame = tk.Frame(window)
key_frame.pack(padx=10, pady=10)

# Label(key)
key_label = tk.Label(key_frame, text="Key: ", height = 1, width=4, 
                     font=('Arial', 16))
key_label.grid(padx=20, pady=10, row=0, column=0, sticky= 'e')

key_entry = tk.Entry(key_frame, font=('Arial', 16))
key_entry.grid(padx=20, pady=10, row=0, column=1, sticky= 'e')

# Checkbox
checkbox_var = tk.IntVar()
checkbox_nl = tk.Checkbutton(key_frame, text="Encrypt/Decrypt non-letters", 
                             variable=checkbox_var, font=('Arial', 16))
checkbox_nl.grid(row=0, column=2, padx=10, pady=10, sticky='n')

def print_textbox_content():
    content = textbox.get("1.0", tk.END).strip()
    print("User typed:", content)

# Grid button
buttonframe = tk.Frame(window)
buttonframe.columnconfigure((0,1), weight=1)
    
def process_inputs(mode):
    # Get all user inputs
    text_content = textbox.get("1.0", tk.END).strip()
    key = key_entry.get()
    encrypt_non_letters = bool(checkbox_var.get())

    try:
        key = int(key)  # Validate key is an integer
    except ValueError:
        print("Key must be a number!")
        return

    if mode == "encrypt":
        print(f"ENCRYPTING with key {key}")
        # Add encryption logic here
    elif mode == "decrypt":
        print(f"DECRYPTING with key {key}")
        # Add decryption logic here

# Update button commands
encryptbutton = tk.Button(buttonframe, text="Encrypt", 
                          command=lambda: process_inputs("encrypt"))# Pass mode
decryptbutton = tk.Button(buttonframe, text="Decrypt", 
                          command=lambda: process_inputs("decrypt"))  # Pass mode

def encrypt():
    text_content = textbox.get("1.0", tk.END).strip()
    key = int(key_entry.get())
    print(f"Encrypting: {text_content} with key {key}")

def decrypt():
    text_content = textbox.get("1.0", tk.END).strip()
    key = int(key_entry.get())
    print(f"Decrypting: {text_content} with key {key}")

# Assign functions directly
encryptbutton = tk.Button(buttonframe, text="Encrypt", command=encrypt)
decryptbutton = tk.Button(buttonframe, text="Decrypt", command=decrypt)

encryptbutton = tk.Button(buttonframe, text="Encryption", height=5, 
                          font=('Arial', 18), command=lambda: process_inputs("encrypt"))
encryptbutton.grid(padx=20, pady=10, row=1, column=0, sticky= 'ew')
decryptbutton = tk.Button(buttonframe, text="Decryption", height=5, 
                          command=lambda: process_inputs("decrypt")  , font=('Arial', 18))
decryptbutton.grid(padx=20, pady=10, row=1, column=1, sticky= 'ew')

buttonframe.pack(fill='x')

window.mainloop()
