import numpy as np
import requests      # for sending http requests
import json
import hashlib       # for sha-256
import os            # for saving
from random import randint
from Pyfhel import Pyfhel, PyCtxt
from datetime import date, datetime

class HEClient(Pyfhel):
    def __init__(self):
        super().__init__()

    """ SETUP FUNCTIONS """
    def generate_context(self, scheme):
        params = {
            'scheme': scheme,
            'n': 2**13,
            't': 65537,
            't_bits': 20,
            'sec': 128,
        }
        self.contextGen(**params)
        self.keyGen()

        return self.to_bytes_public_key()
    
    def send_context_to_server(self):
        x, y, cx, cy = self.generate_test()

        r = requests.post(
            'http://127.0.0.1:5000/send-context',
            json={
                "context": self.to_bytes_context().decode('cp437'),
                "pubKey": self.to_bytes_public_key().decode('cp437'),
                "cx": cx.decode('cp437'),
                "cy": cy.decode('cp437')
            },
        )

        # handling server response
        if r.status_code == 200:
            res = json.loads(r.text)
            if (res['success']):
                # validating sum computed by server
                if self.validate_server(x, y, res['sum'].encode('cp437')):
                    print(f"Server validated.")
                else:
                    print(f"Error occured: Server validation failed.")
            else:
                print(f"Error occured: {res['message']}")
        else:
            print(f"Error occured: Status code {r.status_code}")

    """ OPERATIONS """
    def encrypt_data(self, user_data):
        # encrypts and sends data from client to server
        last_name = self.encrypt(np.frombuffer(user_data['last_name'].encode(), dtype=np.uint8))
        first_name = self.encrypt(np.frombuffer(user_data['first_name'].encode(), dtype=np.uint8))
        middle_name = self.encrypt(np.frombuffer(user_data['middle_name'].encode(), dtype=np.uint8))
        birthday = self.encrypt(np.frombuffer(user_data['birthday'].encode(), dtype=np.uint8))
        age = self.encrypt(np.array([self.calculate_age(user_data['birthday'])], dtype=np.uint8))
        birthplace = self.encrypt(np.frombuffer(user_data['birthplace'].encode(), dtype=np.uint8))
        income = self.encrypt(np.frombuffer(user_data['income'].encode(), dtype=np.uint8))
        sex = self.encrypt(np.frombuffer(user_data['sex'].encode(), dtype=np.uint8))
        civil = self.encrypt(np.frombuffer(user_data['civil'].encode(), dtype=np.uint8))
        citizenship = self.encrypt(np.frombuffer(user_data['citizenship'].encode(), dtype=np.uint8))
        dep_last_name = self.encrypt(np.frombuffer(user_data['dep_last_name'].encode(), dtype=np.uint8))
        dep_first_name = self.encrypt(np.frombuffer(user_data['dep_first_name'].encode(), dtype=np.uint8))
        dep_middle_name = self.encrypt(np.frombuffer(user_data['dep_middle_name'].encode(), dtype=np.uint8))
        dep_bday = self.encrypt(np.frombuffer(user_data['dep_bday'].encode(), dtype=np.uint8))
        dep_relationship = self.encrypt(np.frombuffer(user_data['dep_relationship'].encode(), dtype=np.uint8))
        dep_citizenship = self.encrypt(np.frombuffer(user_data['dep_citizenship'].encode(), dtype=np.uint8))

        # generating hashes
        user_hash = hashlib.sha256(f"{user_data['last_name']}{user_data['first_name']}{user_data['middle_name']}".encode('utf-8')).hexdigest()
        dep_hash = hashlib.sha256(f"{user_data['dep_last_name']}{user_data['dep_first_name']}{user_data['dep_middle_name']}".encode('utf-8')).hexdigest()

        # TODO: modify enc_data to use int on fields that apply
        enc_data = {
            'user_hash': user_hash,
            'last_name': last_name.to_bytes(),
            'first_name': first_name.to_bytes(),
            'middle_name': middle_name.to_bytes(),
            'birthday': birthday.to_bytes(),
            'age': age.to_bytes(),
            'birthplace': birthplace.to_bytes(),
            'income': income.to_bytes(),
            'sex': sex.to_bytes(),
            'civil': civil.to_bytes(),
            'citizenship': citizenship.to_bytes(),
            'dep_hash': dep_hash,
            'dep_last_name': dep_last_name.to_bytes(),
            'dep_first_name': dep_first_name.to_bytes(),
            'dep_middle_name': dep_middle_name.to_bytes(),
            'dep_bday': dep_bday.to_bytes(),
            'dep_relationship': dep_relationship.to_bytes(),
            'dep_citizenship': dep_citizenship.to_bytes(),
        }

        # sending data to server
        self.send_data_to_server(enc_data)

        # returning only some ciphertext bytes for preview
        return enc_data['last_name']
    
    def send_data_to_server(self, data):
        r = requests.post(
            'http://127.0.0.1:5000/save-data',
            json = {
                "user_hash": data['user_hash'],
                "last_name": data['last_name'].decode('cp437'),
                "first_name": data['first_name'].decode('cp437'),
                "middle_name": data['middle_name'].decode('cp437'),
                "birthday": data['birthday'].decode('cp437'),
                "age": data['age'].decode('cp437'),
                "birthplace": data['birthplace'].decode('cp437'),
                "income": data['income'].decode('cp437'),
                "sex": data['sex'].decode('cp437'),
                "civil": data['civil'].decode('cp437'),
                "citizenship": data['citizenship'].decode('cp437'),
                "dependent": {
                    "dep_hash": data['dep_hash'],
                    "last_name": data['dep_last_name'].decode('cp437'),
                    "first_name": data['dep_first_name'].decode('cp437'),
                    "middle_name": data['dep_middle_name'].decode('cp437'),
                    "bday": data['dep_bday'].decode('cp437'),
                    "relationship": data['dep_relationship'].decode('cp437'),
                    "citizenship": data['dep_citizenship'].decode('cp437'),
                }
            }
        )

        # handling server response
        if r.status_code == 200:
            res = json.loads(r.text)
            if (res['success']):
                print("Data saved successfully.")
            else:
                print(f"Error occured: {res['message']}")
        else:
            print(f"Error occured: Status code {r.status_code}")
    
    """ UTILS """
    def calculate_age(self, birthday):
        # calculates age of a user given a string of birthday
        today = date.today()
        dob = datetime.strptime(birthday, "%d/%m/%Y")
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    
    def save_keys(self, save_dir):
        # save into directory
        self.save_context(os.path.join(save_dir, "context"))
        self.save_public_key(os.path.join(save_dir, "pub.key"))
        self.save_secret_key(os.path.join(save_dir, "sec.key"))
    
    def load_keys(self, c, k, s):
        # load into pyfhel instance
        self.load_context(c)
        self.load_public_key(k)
        self.load_secret_key(s)

    """ DEBUGGING FUNCTIONS """
    def generate_test(self):
        # generates a random x and y between 1 to 100 and encrypts them
        # the server must compute its sum and return the correct sum
        x, y = randint(1, 100), randint(1, 100)
        cx = self.encrypt(np.array([x], dtype=np.int64))
        cy = self.encrypt(np.array([y], dtype=np.int64))

        return (x, y, cx.to_bytes(), cy.to_bytes())
    
    def validate_server(self, x, y, server_response):
        # server sends the sum computed homomorphically and client checks if the sum is correct
        try: 
            c_res = PyCtxt(pyfhel=self, bytestring=server_response)
            res = self.decrypt(c_res)

            assert x + y == res[0]
            return True
        except AssertionError as e:
            print(e)
            return False
        except Exception as e:
            print(e)
            return False
