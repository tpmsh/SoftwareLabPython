class Cipher:
    def __init__(self, key = 2):
        self.key = key

    def cipher(self, word):
        encoded = ''
        for ch in word:
            new = ord(ch) + self.key
            encoded += chr(new)
        return encoded

    def decipher(self, word):
        decoded = ''
        for ch in word:
            new = ord(ch) - self.key
            decoded += chr(new)
        return decoded

msg = input("Enter your Message ")
key = int(input("Enter your Key :"))
c = Cipher(key)
enc = c.cipher(msg)
print("Encoded Word is "+enc)
dec = c.decipher(enc)
print("Decoded Word is "+dec)
