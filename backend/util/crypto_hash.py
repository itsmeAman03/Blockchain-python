import hashlib
import json


def crypto_hash(*args): #*args an take many input at once
    """
    return a sha-256 hash of the given arguments
    """
    #we have to conert data into string if its o string bcz it willl throw error if other data type ike int , float etc passed as data
    #to convert data into string we use json dump method

    stringified_args=sorted(map(lambda data: json.dumps(data),args)) there is no need to sort data
    # stringified_args=map(json.dumps,args)

    print(f"stringified_args: {stringified_args}")

    joined_data='^'.join(stringified_args)

    print(f"joined data : {joined_data}")

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest() #we need to encode data for hashing

def main():

    print(f"crypto_hash('2','[3]','one'):{crypto_hash('2','[3]','one')}")
    print(f"crypto_hash('one','2','[3]'):{crypto_hash('one','2','[3]')}")

    #above adjustment cant do the hashing of string hence to do it we do stringy it
    """
    print(f"crypto_hash('[2]'):{crypto_hash([2])}") #list
    print(f"\ncrypto_hash('foo'):{crypto_hash('foo')}") #string
    print(f"\ncrypto_hash('1'):{crypto_hash(1)}") #integer
    """

if __name__=='__main__':
    main()

"""
benefits of SHA256

->produce a unique value for unique input
->a one-way function

ENCODING    

CHARACTER ENCODING
example-> utf-8

each character is converted into 8 bits or 1 byte

y encoding anyone in the world can convert data into diffrenet application


"""