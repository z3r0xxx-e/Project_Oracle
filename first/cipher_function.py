def caesar_cipher_forward(text, shift=3):
    protocol = "https://"
    if text.startswith(protocol):
        payload = text[len(protocol):]
    else:
        payload = text
        protocol = ""
        
    encrypted_chars = []
    for char in payload:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            new_char = chr(start + (ord(char) - start + shift) % 26)
            encrypted_chars.append(new_char)
        elif char.isdigit():
            new_char = chr(ord('0') + (ord(char) - ord('0') + shift) % 10)
            encrypted_chars.append(new_char)
        else:
            encrypted_chars.append(char)
            
    return protocol + "".join(encrypted_chars)
