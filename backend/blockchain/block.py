import time
from backend.util.crypto_hash import crypto_hash
from backend.util.hex_to_binary import hex_to_binary
from backend.config import MINE_RATE

GENESIS_DATA = {
    'timestamp':1,
    'last_hash':'genesis_last_hash',
    'hash': 'genesis_hash',
    'data':[],
    'difficulty':3,
    'nonce': 'genesis_nonce'
}
class Block:
    """
    Block : unit of storage
    Store transaction in a blockchain that supports a cryptocurrency
    """
    def __init__(self, timestamp, last_hash, hash, data,difficulty,nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.difficulty=difficulty
        self.nonce=nonce
 
    def __repr__(self):
        return (
            'Block('
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash},'
            f'data: {self.data},'
            f'difficulty:{self.difficulty},'
            f'nonce:{self.nonce})'
        )
    
    def __eq__(self,other):
        return self.__dict__ == other.__dict__

    @staticmethod
    def mine_block(last_block,data):
        """
        Mine a block based on the given last_block and data until a block has
        is found that meets the leading 0's proof of work requirement
        """

        timestamp=time.time_ns()
        last_hash=last_block.hash
        difficulty=Block.adjust_difficulty(last_block,timestamp)
        nonce=0
        hash=crypto_hash(timestamp,last_hash,data,difficulty,nonce)

        while hex_to_binary(hash)[0:difficulty]!='0'*difficulty:
            nonce+=1
            timestamp=time.time_ns()
            difficulty=Block.adjust_difficulty(last_block,timestamp)
            hash=crypto_hash(timestamp,last_hash,data,difficulty,nonce)
            

        return Block(timestamp,last_hash,hash,data,difficulty,nonce)

    @staticmethod
    def genesis():
        """
        generate the genesis block - first block's last hash doesnt point to anything this is for this block is made
        """

        # return Block(
        #     timestamp=GENESIS_DATA['timestamp'],
        #     last_hash=GENESIS_DATA['last_hash'],
        #     hash=GENESIS_DATA['hash'],
        #     data=GENESIS_DATA['data']
        #     )
        return Block(**GENESIS_DATA) 
        #unpacking will genesis data will work same as before



    @staticmethod
    def adjust_difficulty(last_block,new_timestamp):
            """
            Calculate the adjusted difficulty acc to MINE_RATE.
            Inc the difficulty for quickly mined block
            Dec the difficulty for slowly mined block
            """
            if(new_timestamp-last_block.timestamp)<MINE_RATE:
                return last_block.difficulty +1

            if(last_block.difficulty-1)>0:
                return last_block.difficulty-1
            
            return 1
    
    @staticmethod
    def is_valid_block(last_block,block):
        """
            validate blcok by enforcing the following rules:
                -the blcok must have the proper last_hasg refrence
                -the block mysr meet the pfoood of work requirement
                -the difficukty must only adjusted by 1
                -the block hash must be a valid combination if the block fields
        """
        if block.last_hash!= last_block.hash:
            raise Exception('The block last_hash must be correct')

        if hex_to_binary(block.hash)[0:block.difficulty]!='0'*block.difficulty:
            raise Exception('The proof of work requirement was not met')

        if abs(last_block.difficulty -block.difficulty)>1:
            raise Exception('The Block difficulty must only adjusted by 1')

        reconstructed_hash=crypto_hash(
            block.timestamp,
            block.last_hash,
            block.data,
            block.nonce,
            block.difficulty
        )
        
        if block.hash!=reconstructed_hash:
            raise Exception('The block hash must be correct')
 

def main():
    genesis_block=Block.genesis()
    bad_block=Block.genesis()
    bad_block=Block.mine_block(genesis_block,'foo')
    bad_block.last_hash='malicious data'

    try:
        Block.is_valid_block(genesis_block,bad_block)
    except Exception as e:
        print(f'is_valid_block :{e}')
    # block = Block.mine_block(genesis_block,'foo')
    # print(block)

if __name__ == '__main__':
    main()

