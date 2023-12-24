from cryptography.fernet import Fernet
import os

#generate random key which is being used for encryption and store it in txt.secret text file
def generate_and_save_key():
    try :
        key = Fernet.generate_key()
        with open('secret.txt', 'wb') as key_file:
            key_file.write(key)
    except Exception as e :
        print(f"There is some error with generate_and_save_key :{str(e)}")
        
#it reads the key that is stored in the secret file and returns the key value from it used by both encyption and decryption code  
def load_key():
    try :
        with open('secret.txt', 'rb') as key_file:
            key = key_file.read()
        return key
    except Exception as e :
        print(f"There is some error with load_key :{str(e)}")
        
        

 #replaces original message with encrypted message       
def encrypt_and_overwrite(file_name, key, cipher_suite):
    try :
        with open(file_name, 'rb') as file:
            message = file.read()
            encrypted_message = cipher_suite.encrypt(message)
        with open(file_name, 'wb') as file:
            file.write(encrypted_message)
    except Exception as e :
        print(f"There is some error with encrypt_and_overwrite :{str(e)}")
        
        
#reads encrypted message from the file and decrpts it and replace encrypted message with the decrypted message       
def decrypt_and_overwrite(file_name, key, cipher_suite):
    try :
        with open(file_name, 'rb') as file:
            encrypted_message = file.read()
            decrypted_message = cipher_suite.decrypt(encrypted_message)
        with open(file_name, 'wb') as file:
            file.write(decrypted_message)
    except Exception as e :
        print(f"There is some error with decrypt_and_overwrite :{str(e)}")