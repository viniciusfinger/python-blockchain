from block import Block, Payload
from hash import hash_payload, validate_proof_of_work
from datetime import datetime


class Blockchain:
    proof_of_work_prefix = '6'
    difficulty = 3
    
    def __init__(self) -> None:
        self.chain = []
        
        self.chain.append(self.create_genesis_block())
    
        
    def create_genesis_block(self):
        payload = Payload(0, 'Genesis Block', '')
    
        return Block(hash_payload(payload), 0, payload)
    
    
    def get_last_block(self) -> Block:
        return self.chain[-1]
    
    
    def hash_last_block(self) -> str:
        return self.get_last_block().hash
    
    
    def add_block(self, data) -> Payload:
        payload = Payload(self.get_last_block().payload.sequence + 1, data, self.hash_last_block())
        print(f'Adding block {payload.sequence} with data: {payload.data}')
        
        return payload
    
    
    def mine(self, payload: Payload):
        nonce = 0
        start_date = datetime.now()
        
        while True:
        
            payload_hash = hash_payload(payload)
        
            pow_hash = hash_payload(payload, nonce)
        
            if (validate_proof_of_work(pow_hash, Blockchain.proof_of_work_prefix, Blockchain.difficulty)):
                final_date = datetime.now()
                
                print(f'Mined block {payload.sequence} in {final_date - start_date} seconds')
                
                return Block(payload_hash, nonce, payload)
            else:
                nonce += 1


    def block_is_valid(self, block: Block) -> bool:
        if (block.payload.previous_hash != self.hash_last_block()):
            print("Block previous hash is invalid.")
            return False
        
        test_hash = hash_payload(block.payload, block.nonce)
        
        if (validate_proof_of_work(test_hash, Blockchain.proof_of_work_prefix, Blockchain.difficulty) is False):
            print("Block hash and nonce is invalid.")
            return False
        
        return True

                
    def add_to_chain(self, block: Block) -> list[Block]:
        if (self.block_is_valid(block)):
            print(f'Block {block.payload.sequence} is valid and added to blockchain.')
            self.chain.append(block)
            return self.chain
        else:
            print(f'Block {block.payload.sequence} is invalid and not added to blockchain.')
