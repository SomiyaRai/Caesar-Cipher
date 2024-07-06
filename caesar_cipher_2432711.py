def welcome():
    """
    Prints an introduction for the Caesar Cipher program.
    """
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")

def enter_message():
    """
    Requests the input from user to determine the mode of conversion and the message.

    Returns:
     mode in str: The mode of conversion ('e' for encrypt, 'd' for decrypt).
     message in str: The message to be encrypted or decrypted.
     shift in int: The shift number for encrypting or decrypting.
    """
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d)? ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid Mode")
    
    message = input("What message would you like to {}? ".format("encrypt" if mode == 'e' else "decrypt"))
    
    while True:
        try:
            shifting_number = int(input("What is the shift number: "))
            if 0 <= shifting_number <= 25:
                break
            else:
                print("Invalid Shift")
        except ValueError:
            print("Invalid Shift")

            
    return mode, message, shifting_number

def encrypt(message, shifting_number):
    """
    Encrypts a plain text message using Caesar Cipher.

    Arguments:
     message: The message to be encrypted.
     shifting_number: The shift number for encryption.

    Returns:
     encrypted_message in str: The encrypted message.
    """
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted_char = chr(((ord(char) - 65 + shifting_number) % 26) + 65)
            encrypted_message += shifted_char
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, shifting_number):
    """
    Decrypts a message encrypted with Caesar Cipher.

    Arguments:
     message: The encrypted message.
     shifting_number: The shift number for decryption.

    Returns:
     decrypted_message in str: The decrypted message.
    """
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted_char = chr(((ord(char) - 65 - shifting_number) % 26) + 65)
            decrypted_message += shifted_char
        else:
            decrypted_message += char
    return decrypted_message

def is_file(filename):
    """
    Checks if the file exists in the current directory.

    Arguments:
     filename: The name of the file to check.

    Returns:
     exists in bool: True if the file exists, False if not.
    """
    try:
        with open(filename, 'r'):
            pass
        return True
    except FileNotFoundError:
        return False

def process_file(filename, mode):
    """
    Processes the messages from a file and encrypts or decrypts them.

    Arguments:
     filename: The name of the file to process.
     mode: The mode of operation ('e' for encrypting, 'd' for decrypting).

    Returns:
     messages in list: A list of encrypted or decrypted messages.
    """
    if not is_file(filename):
        print("File '{}' not found.".format(filename))
        return []
    
    messages = []
    while True:
        try:
            shifting_number = int(input("What is the shift number: "))
            if 0 <= shifting_number <= 25:
                break
            else:
                print("Invalid Shift")
        except ValueError:
            print("Invalid Shift")
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().upper()
            if mode == 'e':
                messages.append(encrypt(line, shifting_number))
            else:
                messages.append(decrypt(line, shifting_number))
    return messages


def write_messages(messages):
    """
    Writes the messages to the selected file.

    Arguments:
     messages: A list of messages to write to the file.
    """
    with open('results.txt', 'w') as file:
        for message in messages:
            file.write(message + '\n')

def message_or_file():
    """
    Determines if the user wants to process the messages from either the console or a file.

    Returns:
     mode in str: The mode of conversion ('e' for encrypt, 'd' for decrypt).
     message in str : The message to be encrypted or decrypted (or None if processing from file).
     filename in str : The name of the file to be process (or None if processing from console).
    """
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d)? ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid Mode")
    
    while True:
        source_option = input("Would you like to read from a file (f) or the console (c)? ").lower()
        if source_option == 'c':
            message = input("What message would you like to {}? ".format("encrypt" if mode == 'e' else "decrypt")).upper()
            filename = None
            break
        elif source_option == 'f':
            filename = input("Enter a filename: ")
            if is_file(filename):
                message = None
                break
            else:
                print("Invalid Filename")
        else:
            print("Invalid Input")
    
    return mode, message, filename

def main():
    """
    Main function for running the Caesar Cipher program.
    """
    welcome()
    while True:
        mode, message, filename = message_or_file()
        
        if filename:
            messages = process_file(filename, mode)
            write_messages(messages)
            print("Output written to results.txt")
        else:
            shifting_number = int(input("What is the shift number: "))
            if mode == 'e':
                print("Encrypted Message:", encrypt(message, shifting_number))
            else:
                print("Decrypted Message:", decrypt(message, shifting_number))
        
        choice = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
        if choice != 'y':
            print("Thanks for using the program, goodbye!")
            break
        else:
            print()

main()
