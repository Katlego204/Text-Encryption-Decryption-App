import tkinter as tk

# I will create a Ceasar Cipher Algorithm that takes in a key from the user 
# to determine the encryption or decryption
# I will then create the GUI for it


'''
C = E(p,k) mod 26 = (p+k) mod 26 => Encryption
p = D(C,k) mod 26 = (C-k) mod 26 => Decryption

 using the ord() function on lowercase letters (ASCII 97)
 to get 'a' == 0 we have to subtract ord('a') by 97 
 now using uppercase letters (ASCII 65)
 
 to return the numbers into characters we can use the chr()
 it converts a number to it's alphabetic representation using ASCII
 '''
 
def lowercaseEncryption(character: str, key: int):
    num_char = ord(character)
    new_char = chr((((num_char-97)+key)%26)+97)
    return new_char
    
def uppercaseEncryption(character: str, key: int):
    num_char = ord(character)
    new_char = chr((((num_char-65)+key)%26)+65)
    return new_char
    
def othercharEncryption(character: str, key: int):
    num_char = ord(character)
    new_char = chr(num_char+key)
    return new_char

def lowercaseDecryption(character: str, key: int):
    num_char = ord(character)
    new_char = chr((((num_char-97)-key)%26)+97)
    return new_char
    
def uppercaseDecryption(character: str, key: int):
    num_char = ord(character)
    new_char = chr((((num_char-65)-key)%26)+65)
    return new_char
    
def othercharDecryption(character: str, key: int):
    num_char = ord(character)
    new_char = chr(num_char-key)
    return new_char

def caesar_encrypt(text: str, key: int, process_non_letters: bool):
    encrypted_text = []
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            if char.isupper():
                encrypted_text.append(uppercaseEncryption(char, key))
            else:
                encrypted_text.append(lowercaseEncryption(char, key))
        else:
            if process_non_letters:
                encrypted_text.append(othercharEncryption(char, key))
            else:
                encrypted_text.append(char)
    return ''.join(encrypted_text)

def caesar_decrypt(text: str, key: int, process_non_letters: bool):
    decrypted_text = []
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            if char.isupper():
                decrypted_text.append(uppercaseDecryption(char, key))
            else:
                decrypted_text.append(lowercaseDecryption(char, key))
        else:
            if process_non_letters:
                decrypted_text.append(othercharDecryption(char, key))
            else:
                decrypted_text.append(char)
    return ''.join(decrypted_text)

'''
--------GUI--------- 
 '''

window = tk.Tk()
window.geometry("800x500")  
window.title("Encryption GUI")

# Title
label = tk.Label(window, text="Caesar Cipher", font=('Arial bold', 25))
label.pack(padx=10, pady=10)

# Textbox (Entering the text that needs Encryption)
textbox = tk.Text(window, height=5, font=('Arial', 25))
textbox.pack(padx=20, pady=1, fill='x')

key_frame = tk.Frame(window)
key_frame.pack(padx=10, pady=10, fill='x')

# Label(key)
key_label = tk.Label(key_frame, text="Key: ", height=1, width=4, 
                     font=('Arial', 16))
key_label.grid(padx=20, pady=10, row=0, column=0, sticky='e')

key_entry = tk.Entry(key_frame, font=('Arial', 16))
key_entry.grid(padx=20, pady=10, row=0, column=1, sticky='e')

# Checkbox
checkbox_var = tk.IntVar()
checkbox_nl = tk.Checkbutton(key_frame, text="Encrypt/Decrypt non-letters", 
                             variable=checkbox_var, font=('Arial', 16))
checkbox_nl.grid(row=0, column=2, padx=10, pady=10, sticky='n')

# Button Frame
buttonframe = tk.Frame(window)
buttonframe.columnconfigure((0,1), weight=1)
buttonframe.pack(fill='x', padx=10, pady=1)

# Result Display Area 
result_frame = tk.Frame(window)
result_frame.pack(padx=20, pady=10, fill='both', expand=True)

result_label = tk.Label(result_frame, text="Result:", font=('Arial bold', 16))
result_label.pack(anchor='w', padx=5, pady=(0, 5))

result_display = tk.Text(result_frame, height=6, font=('Arial', 14),
                         state='disabled',wrap='word')
result_display.pack(fill='both', expand=True, padx=5)

# Scrollbar for result display
scrollbar = tk.Scrollbar(result_display)
scrollbar.pack(side='right', fill='y')
result_display.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=result_display.yview)

''' 
Button Setup
 '''
 
# Buttons 
encryptbutton = tk.Button(buttonframe, text="Encryption", height=2, font=('Arial', 18), 
                          command=lambda: process_inputs("encrypt"))
encryptbutton.grid(padx=20, pady=10, row=1, column=0, sticky='ew')

decryptbutton = tk.Button(buttonframe, text="Decryption", height=2, font=('Arial', 18),
                          command=lambda: process_inputs("decrypt"))
decryptbutton.grid(padx=20, pady=10, row=1, column=1, sticky='ew')

def process_inputs(mode):
    # Get all user inputs 
    text_content = textbox.get("1.0", tk.END).strip()
    key = key_entry.get()
    encrypt_non_letters = bool(checkbox_var.get())

    try:
        key = int(key)  # Validate key is an integer
    except ValueError:
        
        result_display.config(state='normal')
        result_display.delete(1.0, tk.END)
        result_display.insert(1.0, "Error: Key must be a number!")
        result_display.config(state='disabled')
        return

    if mode == "encrypt":
        result = caesar_encrypt(text_content, key, encrypt_non_letters)
    else:
        result = caesar_decrypt(text_content, key, encrypt_non_letters)
    
    # Display result in the bottom text box
    result_display.config(state='normal')
    result_display.delete(1.0, tk.END)
    result_display.insert(1.0, result)
    result_display.config(state='disabled')


# Start the GUI
window.mainloop()
