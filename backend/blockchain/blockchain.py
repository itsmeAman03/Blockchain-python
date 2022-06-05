from backend.blockchain.block import Block

class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions
    """

    def __init__(self): 
        self.chain=[Block.genesis()]

    def addblock(self,data):
        self.chain.append(Block.mine_block(self.chain[-1],data))
    
    def __repr__(self):return f'Blockchain: {self.chain}'

def main():
    blockchain=Blockchain()
    blockchain.addblock('one')
    blockchain.addblock('two')

    print(blockchain)
    print(f'blockchain.py __name__: {__name__} ') #same module
if __name__ == '__main__':
    main()