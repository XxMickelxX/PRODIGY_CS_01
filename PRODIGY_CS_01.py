def encrypt_text(plain_text, key):
    encrypted_text = ""
    for char in plain_text:
        if char.isupper():
            encrypted_text += chr(((ord(char) - 65 + key) % 26) + 65)
        elif char.islower():
            encrypted_text += chr(((ord(char) - 97 + key) % 26) + 97)
        else:
            encrypted_text += char
    return encrypted_text
def decrypt_text(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isupper():
            decrypted_text += chr((ord(char) - key - 65) % 26 + 65)
        elif char.islower():
            decrypted_text += chr((ord(char) - key - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text
operation='?'
while(operation.upper()!='E'and operation.upper()!='D'):
    operation = input("Enter 'E' for encryption or 'D' for decryption: ")
    if operation.upper() == 'E':
        
        plain_text = input("Enter the message to encrypt: ")
        key = int(input("Enter the key for encryption: "))
        print(encrypt_text(plain_text,key))
        
    elif operation.upper() == 'D':
        
        encrypted_text = input("Enter the message to decrypt: ")
        key = int(input("Enter the key for decryption: "))
        print(decrypt_text(encrypted_text,key))       
    else:
        print("Invalid operation!\n")