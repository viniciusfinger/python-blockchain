import hashlib
import json
from block import Payload

def hash_payload(payload: Payload, nonce = None) -> str:
    payload_json = json.dumps(payload.__dict__)
    
    if (nonce is not None):
        payload_json += str(nonce)
    
    return hashlib.sha256(payload_json.encode()).hexdigest()

def validate_proof_of_work(hash: str, pow_prefix: str, difficulty: int) -> bool:
    if (hash.startswith(pow_prefix * difficulty)):
        print(f'Found valid hash: {hash}')
        return True
    return False