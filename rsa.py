from Crypto.PublicKey import RSA
from Crypto import Random
from base64 import *

random = Random.new().read
rsa = RSA.generate(8192,random)

def key():
	public = b64encode(rsa.publickey().exportKey('DER'))
	priv = rsa.exportKey('DER')
	open('priv.pem','wb').write(priv)
	return public

def encrypt(message,public):
	keyDer = RSA.importKey(b64decode(public))
	encrypt = keyDer.encrypt(message,rsa)
	return b64encode(encrypt[0])

def decrypt(message):
	priv = open('priv.pem','rb').read()
	keyDer = RSA.importKey(priv)
	decrypt = keyDer.decrypt(b64decode(message))
	return decrypt
