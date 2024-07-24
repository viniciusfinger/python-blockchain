from datetime import datetime

        
class Payload:
    def __init__(self, sequence, data, previous_hash = '') -> None:
        self.sequence = sequence
        self.timestamp = datetime.now().timestamp()
        self.data = data
        self.previous_hash = previous_hash
    

class Block:
    def __init__(self, hash, nonce, payload) -> None:
        self.hash = hash
        self.nonce = nonce
        self.payload = payload