import hashlib
message = "Hello World"
cipherMessage = hashlib.sha1(message.encode()).hexdigest()
print("Message: "+message)
print("Cipher Message: "+cipherMessage)