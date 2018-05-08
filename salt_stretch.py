import bcrypt
import hashlib

def hashPass(password,salt):
	hashpass = hashlib.sha256(password + salt).hexdigest()
	return hash

def stretchPass(password, salt, r):
	x = "0"
	for i in range(0,r):
		x = hashlib.sha256(x + password + salt).digest()
	return x



