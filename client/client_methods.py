import numpy as np
import requests      # for sending http requests
import json
from random import randint
from Pyfhel import Pyfhel, PyCtxt

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
