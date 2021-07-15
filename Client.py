import socket
import pickle

import phe as paillier
import json

def storeKeys():
	public_key, private_key = paillier.generate_paillier_keypair()
	keys={}
	keys['public_key'] = {'n': public_key.n}
	keys['private_key'] = {'p': private_key.p,'q':private_key.q}
	with open('keys.json', 'w') as file: 
		json.dump(keys, file)

def getKeys():
	with open('keys.json', 'r') as file: 
		keys=json.load(file)
		pub_key=paillier.PaillierPublicKey(n=int(keys['public_key']['n']))
		priv_key=paillier.PaillierPrivateKey(pub_key,keys['private_key']['p'],keys['private_key']['q'])
		return pub_key, priv_key 

def serializeData(public_key, data):
	encrypted_data_list = [public_key.encrypt(x) for x in data]
	encrypted_data={}
	encrypted_data['public_key'] = {'n': public_key.n}
	encrypted_data['values'] = [(str(x.ciphertext()), x.exponent) for x in encrypted_data_list]
	serialized = encrypted_data
	return serialized



def loadAnswer():
    with open('answer.json', 'r') as file: 
        ans=json.load(file)
        answer=json.loads(ans)
        return answer

def recv(soc, buffer_size=1024, recv_timeout=100):
    print('abc')
    received_data = b""
    while str(received_data)[-3] != ']':
        try:
            print('123')
            soc.settimeout(recv_timeout)
            received_data += soc.recv(buffer_size)
            
        except socket.timeout:
            print("A socket.timeout exception occurred because the server did not send any data for {recv_timeout} seconds.".format(recv_timeout=recv_timeout))
            return None, 0
        except BaseException as e:
            return None, 0
            print("An error occurred while receiving data from the server {msg}.".format(msg=e))

    try:
        print('def')
        received_data = json.loads(received_data)
        
    except BaseException as e:
        print("Error Decoding the Client's Data: {msg}.\n".format(msg=e))
        return None, 0
   
    return received_data, 1

soc = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
print("Socket Created.\n")

try:
    soc.connect(("localhost", 5000))
except BaseException as e:
    print("Error Connecting to the Server: {msg}".format(msg=e))
    soc.close()
    print("Socket Closed.")

print("Successful Connection to the Server.\n")


while True:
    
    storeKeys()
    pub_key, priv_key = getKeys()
    data = age, he, al, gen = [24,4,6,1]
    serializeData(pub_key, data)
    datafile=serializeData(pub_key, data)
    data_byte = json.dumps(datafile).encode('utf-8')
    
    
    print("Sending Data to the Server.\n")
    print(data_byte)
    soc.sendall(data_byte)
    
    print("Receiving Reply from the Server.")
    received_data, status = recv(soc=soc, 
                                 buffer_size=1024, 
                                 recv_timeout=100)
    if status == 0:
        print("Nothing Received from the Server.")
        break
    else:
        print(received_data, end="\n\n")
        answer_file=received_data
        print(answer_file)
        answer_key=paillier.PaillierPublicKey(n=int(answer_file['pubkey']['n']))
        answer = paillier.EncryptedNumber(answer_key, int(answer_file['values'][0]), int(answer_file['values'][1]))
        if (answer_key==pub_key):
            print(priv_key.decrypt(answer))
     
soc.close()
print("Socket Closed.\n")
