```python
import unittest
import json
from machine_learning import HomeAutomationML
from communication import send_data_to_iot, receive_data_from_iot
from security import encrypt_data, decrypt_data

class TestHomeAutomation(unittest.TestCase):

    def setUp(self):
        self.ml_model = HomeAutomationML()
        self.test_data = {
            'temperature': 24,
            'humidity': 50,
            'light': 300,
            'motion': 0
        }

    def test_machine_learning(self):
        # Load test data
        self.ml_model.load_data(json.dumps([self.test_data]))

        # Preprocess data
        self.ml_model.preprocess_data()

        # Split data
        self.ml_model.split_data()

        # Train model
        self.ml_model.train_model()

        # Evaluate model
        self.ml_model.evaluate_model()

        # Predict control signals
        prediction = self.ml_model.predict(json.dumps([self.test_data]))
        self.assertIsInstance(prediction, list)

    def test_communication(self):
        # Send data to IoT component
        send_data_to_iot(json.dumps(self.test_data))

        # Receive data from IoT component
        received_data = receive_data_from_iot()
        self.assertEqual(json.loads(received_data), self.test_data)

    def test_security(self):
        # Encrypt data
        encrypted_data = encrypt_data(json.dumps(self.test_data))

        # Decrypt data
        decrypted_data = decrypt_data(encrypted_data)
        self.assertEqual(json.loads(decrypted_data), self.test_data)

if __name__ == '__main__':
    unittest.main()
```
