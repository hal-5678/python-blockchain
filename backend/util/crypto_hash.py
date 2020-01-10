import hashlib
import json

def crypto_hash(*args):
    """
    Return a sha-256 hash of the given data ( or arguments). Stringify data using json library so hashlib library can hash any data (ie: integer, etc.)
    """
    stringified_args = sorted(map(lambda data: json.dumps(data), args))
    print(f'stringified_args: {stringified_args}')
    joined_data=''.join(stringified_args)
    
    
    print(f'joined_data: {joined_data}')
    
    """
    Meaning of encoding: The process of converting data into an alternate representation. 
    """
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()
    
def main():
    print(f"crypto_hash('one',2,[3]): {crypto_hash('one',2,[3])}")
    print(f"crypto_hash(2,'one',[3]): {crypto_hash(2,'one',[3])}")
    
if __name__ == '__main__':
    main()
