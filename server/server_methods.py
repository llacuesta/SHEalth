import numpy as np
import json
from Pyfhel import Pyfhel, PyCtxt

class HEServer(Pyfhel):
    def __init__(self):
        super().__init__()

    """ SERVER FUNCTIONS """
    # TODO: Count with a list of conditions
    # encrypt condiion
    # scan all documents in db and compute homomorphic equality (subtract values and check if it returns 0)
    # update counter then return count

    # might be an O(n) operation, check conditions per number of documents in db
    # get all documents in db, iterate through each element if all conditions match
    # return count to client

    # TODO: Dependent lookup
    # use user first and last name to generate new hash in client side
    # use hash to query dependent in dependent table

    # TODO: Decision tree for benefits
        # TODO: create at least 15 documents in advance then generate a decision tree from those documents
    # get document and all relevant fields

    """ SETUP FUNCTIONS """
    def generate_from_context(self, context, publicKey):
        # creating server instance
        try:
            self.from_bytes_context(context)
            self.from_bytes_public_key(publicKey)
        except Exception as e:
            print(e)
    
    def validate_instance(self, cx, cy):
        # performing basic addition to send to client
        # if sum decrypts to the same sum on the client, server is correct
        try:
            x = PyCtxt(pyfhel=self, bytestring=cx)
            y = PyCtxt(pyfhel=self, bytestring=cy)
            csum = x + y

            return json.dumps({
                "success": True,
                "sum": csum.to_bytes().decode('cp437')
            })
        except Exception as e:
            print(e)

            return json.dumps({
                "success": False,
                "message": e.args[0]
            })
