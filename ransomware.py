# author @rebwar_me
# ------------------------------
import os
# ---------------------
def encrypt(file):
	i_f = None
	with open(file,"rb") as f:
		i_f = f.read()
	i_f = b'.enc'+i_f[:32][::-1]+i_f[32:]
	with open(file,"wb") as f:
		f.write(i_f)

# ---------------------
def decrypt(file):
	i_f = None
	with open(file,"rb") as f:
		i_f = f.read()
	if i_f[:4]==b'.enc':
		i_f = i_f[4:]#delete .enc
		i_f = i_f[:32][::-1]+i_f[32:]
		with open(file,"wb") as f:
			f.write(i_f)

# ---------------------
def run(mode):
	cwd = os.getcwd()
	os.chdir(os.path.join(cwd,"files"))
	files = os.listdir()
	for file in files:
		try:
			if mode == "0":
				encrypt(file)
			elif mode == "1":
				decrypt(file)
		except:
			pass

mode = input("Enter 0 to Encryption"+
			"\nOr 1 to Decryption : ")
run(mode)