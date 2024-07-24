from blockchain import Blockchain


blockchain = Blockchain()

for i in range(10):
    payload = blockchain.add_block(f'Block {i}')
    block = blockchain.mine(payload)
    blockchain.add_to_chain(block)
    
for block in blockchain.chain:
    print(f'Block {block.payload.sequence} with data: {block.payload.data} and hash: {block.hash}')
