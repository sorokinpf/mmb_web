import os
from hashlib import sha256
import binascii

class Security():
	@staticmethod
	def check_password(hash_string,password):
		(salt,pswd_hash) = hash_string.split(':')
		print (hash_string)
		check_hash =  sha256(bytes(salt+password,'utf-8')).hexdigest()
		print (check_hash)
		if check_hash == pswd_hash:
			return True
		else:
			return False

	def create_password(password):
		print (password,type(password))
		salt = binascii.hexlify(os.urandom(16))
		pswd_hash = sha256(salt+bytes(password,'utf-8')).hexdigest()
		return salt.decode('ascii')+':'+pswd_hash