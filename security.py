```python
import hashlib
import os
from cryptography.fernet import Fernet
import json

# Define the class for the security module
class HomeAutomationSecurity:

    def __init__(self):
        # Generate a key for symmetric encryption
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    # Function to hash passwords
    def hash_password(self, password):
        # Use the SHA-256 hashing algorithm
        return hashlib.sha256(password.encode()).hexdigest()

    # Function to verify passwords
    def verify_password(self, hashed_password, user_password):
        return hashed_password == hashlib.sha256(user_password.encode()).hexdigest()

    # Function to encrypt data
    def encrypt_data(self, data):
        # Convert the data to JSON format
        data = json.dumps(data)

        # Encrypt the data
        encrypted_data = self.cipher_suite.encrypt(data.encode())

        return encrypted_data

    # Function to decrypt data
    def decrypt_data(self, encrypted_data):
        # Decrypt the data
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)

        # Convert the data back from JSON format
        data = json.loads(decrypted_data.decode())

        return data

# Main function
if __name__ == "__main__":
    # Initialize the security module
    security_module = HomeAutomationSecurity()

    # Example usage
    password = "my_password"
    hashed_password = security_module.hash_password(password)

    print("Hashed password:", hashed_password)
    print("Password verification:", security_module.verify_password(hashed_password, "my_password"))

    data = {"temperature": 24, "humidity": 50, "light": 300, "motion": False}
    encrypted_data = security_module.encrypt_data(data)

    print("Encrypted data:", encrypted_data)
    print("Decrypted data:", security_module.decrypt_data(encrypted_data))
```
