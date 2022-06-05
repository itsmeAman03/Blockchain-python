from backend.util.crypto_hash import crypto_hash

def test_crypto():
    #it should create the same hash with the arguments of diff data types
    #in any order
    assert crypto_hash(1,[2],'three')==crypto_hash('three',1,[2])
