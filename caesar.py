import tkinter as tk
# Create a Ceasar Cipher Algorithm that takes in a key from the user to determine the encryption

'''
C = E(p,k) mod 26 = (p+k) mod 26 => Encryption
p = D(C,k) mod 26 = (C-k) mod 26 => Decryption
'''
 
'''
 using the ord() function on lowercase letters (ASCII 97)
 to get 'a' == 0 we have to subtract ord('a') by 97 
 now using uppercase letters (ASCII 65)
 
 to return the numbers into characters we can use the chr()
 it converts a number to it's alphabetic representation using ASCII
 '''
 
def Encryption_alg():
    text_input = input("Encrypt Text: ")
    encrypted_text = []
    final_encryption = ""
    while True:
        key_input = input("Key: ")
        try:
            key_input = int(key_input)
            break
        except ValueError:
            print("Key Must Be a Number")
            
    for i in range(len(text_input)):
        if text_input[i].isalpha():
            if text_input[i].isupper():
                encrypted_text.append(uppercaseEncryption(text_input[i], key_input))
            else:
                encrypted_text.append(lowercaseEncryption(text_input[i], key_input))
        else:
            encrypted_text.append(othercharEncrytion(text_input[i], key_input))

    for letter in encrypted_text:
        final_encryption += letter
    
    print(f"Encrypted text: {final_encryption}")
    

def Decryption_alg():
    text_input = input("Decrypt Text: ")
    encrypted_text = []
    final_encryption = ""
    while True:
        key_input = input("Key: ")
        try:
            key_input = int(key_input)
            break
        except ValueError:
            print("Key Must Be a Number")
    for i in range(len(text_input)):
        if text_input[i].isalpha():
            if text_input[i].isupper():
                encrypted_text.append(uppercaseDecryption(text_input[i], key_input))
            else:
                encrypted_text.append(lowercaseDecryption(text_input[i], key_input))
        else:
            encrypted_text.append(othercharDecrytion(text_input[i], key_input))

    for letter in encrypted_text:
        final_encryption += letter
    
    print(f"Encrypted text: {final_encryption}")
    

def lowercaseEncryption(character:str, key:int):
    #turn the character to ASCII numeral
    num_char = ord(character)
    #Encryption using key (char swap)
    new_char = chr((((num_char-97)+key)%26)+97)
    
    return new_char
    
def uppercaseEncryption(character:str, key:int):
    num_char = ord(character) # returns a ASCII number
    new_char = chr((((num_char-65)+key)%26)+65)
    
    return new_char
    
def othercharEncrytion(character:str, key:int):
    num_char = ord(character)
    new_char = chr(num_char+key)
    return new_char

def lowercaseDecryption(character:str, key:int):
    #turn the character to ASCII numeral
    num_char = ord(character)
    #Encryption using key (char swap)
    new_char = chr((((num_char-97)-key)%26)+97)
    
    return new_char
    
def uppercaseDecryption(character:str, key:int):
    num_char = ord(character) # returns a ASCII number
    new_char = chr((((num_char-65)-key)%26)+65)
    
    return new_char
    
def othercharDecrytion(character:str, key:int):
    num_char = ord(character)
    new_char = chr(num_char-key)
    return new_char

if __name__ == "__main__":
    print("Do you want to Encrypt or Decrypt the text?")
    while True:
        try:
            mode = int(input("Press '0' for Encrypt and '1' for Decrypt: "))
            if mode not in [0, 1]:
                print("Please Select '0' Or '1'")
            else:
                break
        except:
            print("Please Select '0' Or '1'")
    
    if mode == 0:
        Encryption_alg()
    else:
        Decryption_alg()
    
    