def caesar_cipher_encryptor(text: str, key: int) -> str:
    result = []
    key = key % 26
    for char in text:
        shifted = ord(char) + key
        if shifted > ord('z'):
            shifted -= 26
        result.append(chr(shifted))
    return ''.join(result)