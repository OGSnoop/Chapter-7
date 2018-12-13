from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
import hashlib
import subprocess
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from base64 import b64encode
from base64 import b64decode


file=''
dirc='.'
file_hash=''
dir_hash=''
dir_hash_dic={}
file_hash_dic={}
org_dir_dic={}
org_file_dic={}
key=b''
enc=''
#system file for directories' permissions is dirp.txt
#system file for file permissions' is firp.txt

#input for file comparison
def input_file():
	global file, file_hash
	file = input('Give the path of the file:\n')
	try:
                #runs linux command to get file permisions
		perm = subprocess.check_output(['ls', '-l', file])
		#hashes the file permissions
		file_hash = hashlib.sha1(perm).hexdigest()
	except:
		print('Improper path')

#input for directory comparison
def input_dir():
	global dirc, dir_hash
	dirc = input('Give the path of the directory:\n')
	try:
                #runs linux command to get file permisions
		perm = subprocess.check_output(['ls', '-l', dirc])
		#hashes the file permissions
		dir_hash = hashlib.sha1(perm).hexdigest()
	except:
		print('Improper path')
		
#creates dictionary for new directory hashes
def new_dirhashdic(dirc, dir_hash):
	global dir_hash_dic
	dir_hash_dic[dirc]=dir_hash

#creates dictionary for new file hashes
def new_filehashdic(file, file_hash):
	global file_hash_dic
	file_hash_dic[file]=file_hash

#creates dictionary of directory permissions that will be stored in a file
def org_dirdic():
        global org_dir_dic, dirc, dir_hash
        contin = 'y'
        while contin == 'y':
                contin = input('Do you wish to continue [y/n]]:\n').lower()
                if contin == 'y':
                    dirc = input('Give the path of the directory:\n')
                    try:
                        #linux permission command
                        perm = subprocess.check_output(['ls', '-l', dirc])
                        #hashing output from the commands
                        dir_hash = hashlib.sha1(perm).hexdigest()
                        print(dir_hash)
                    except:
                        print('Improper path')
                    org_dir_dic[dirc]=dir_hash
                elif contin == 'n':
                    contin = 'n'
                else:
                    print('Not a valid input')
                    contin = 'y'

#creates dictionary of file permissions that will be stored in a file
def org_filehashdic():
	global org_file_dic, file, file_hash
	contin = 'y'
	while contin == 'y':
                contin = input('Do you wish to continue [y/n]:\n').lower()
                if contin == 'y':
                        file = input('Give the path of the file:\n')
                        try:
                                #linux permission command
                                perm = subprocess.check_output(['ls', '-l', file])
                                #hashing output from the commands
                                file_hash = hashlib.sha1(perm).hexdigest()
                        except:
                                print('Improper path')
                        org_file_dic[file]=file_hash
                elif contin == 'n':
                        contin == 'n'
                else:
                        print('Not a valid input')
                        contin = 'y'
                


#writes directory permissions to dirp.txt
def write_dir():
        global org_dir_dic
        dirp = open('/root/Documents/dirp.txt', 'a')
        for key,value in org_dir_dic.items():
                dirp.write('{a}:{b}\n'.format(a=key, b=value))
        dirp.close()

#writes file permissions to firp.txt
def write_file():
        global org_file_dic
        firp = open('/root/Documents/firp.txt', 'a')
        for key,value in org_file_dic.items():
                firp.write('{a}:{b}\n'.format(a=key, b=value))
        firp.close()

#reads the content in dirp.txt
def read_dir():
        global org_dir_dic
        dirp = open('/root/Documents/dirp.txt', 'r')
        dirp_lines = dirp.readlines()
        dirp.close()
        for i in range(len(dirp_lines)):
                if dirp_lines[i]  != '\n':
                        line = dirp_lines[i]
                        tokens = line.split(':')
                        org_dir_dic[tokens[0]]=tokens[1]

#reads the content in firp.txt
def read_file():
        global org_file_dic
        firp = open('/root/Documents/firp.txt', 'r')
        firp_lines = firp.readlines()
        firp.close()
        for i in range(len(firp_lines)):
                if firp_lines[i] != '\n':
                        line = firp_lines[i]
                        tokens = line.split(':')
                        org_file_dic[tokens[0]]=tokens[1]

#Compares the hashes of a single directory
def comp_dir():
        global dirc, dir_hash_dic, org_dir_dic
        new = dir_hash_dic[dirc]
        org = org_dir_dic[dirc].strip()
        if new == org:
                print()
                print('Directory %s permissions are secure.\n' % dirc)
        elif new != org:
                print()
                print('Directory %s permissions have been altered.\n' % dirc)

#Compares the hashes of a single file
def comp_file():
        global file, file_hash_dic, org_file_dic
        new = file_hash_dic[file]
        org = org_file_dic[file].strip()
        if new == org:
                print()
                print('File %s permissions are secure.\n' % file)
        else:
                print()
                print('File %s permissions have been altered.\n' % file)

#compares all of the stored hashes for directories
def comp_all_dir():
        global dir_hash_dic, org_dir_dic
        dirp = open('/root/Documents/dirp.txt', 'r')
        dirp_lines = dirp.readlines()
        print(dirp_lines)
        dirp.close()
        dirlist = []
        for i in range(len(dirp_lines)):
                if dirp_lines[i] != '\n':
                        line = dirp_lines[i]
                        tokens = line.split(':')
                        dirlist.append(tokens[0])
                        org_dir_dic[tokens[0]]=tokens[1]
                        perm = subprocess.check_output(['ls', '-l', tokens[0]])
                        dir_hash = hashlib.sha1(perm).hexdigest()
                        dir_hash_dic[tokens[0]]=dir_hash
        for i in dirlist:
                new = dir_hash_dic[i]
                org = org_dir_dic[i].strip()
                if new == org:
                        print()
                        print('Directory %s permissions are secure.\n' % i)
                else:
                        print()
                        print('Directory %s permissions have been altered.\n' % i)

#compares all of the stored hashes for files
def comp_all_file():
        global file_hash_dic, org_file_dic
        firp = open('/root/Documents/firp.txt', 'r')
        firp_lines = firp.readlines()
        firp.close()
        firlist = []
        for i in range(len(firp_lines)):
                if firp_lines[i] != '\n':
                        line = firp_lines[i]
                        tokens = line.split(':')
                        filelist.append(tokens[0])
                        org_file_dic[tokens[0]]=tokens[1]
                        perm = subprocess.check_output(['ls', '-l', tokens[0]])
                        file_hash = hashlib.sha1(perm).hexdigest()
                        file_hash_dic[tokens[0]]=file_hash
        for i in filelist:
                new = file_hash_dic[i]
                org = org_file_dic[i].strip()
                if new == org:
                        print()
                        print('File %s permissions are secure.\n' % i)
                else:
                        print()
                        print('File %s permissions have been altered.\n' % i)

#This is the key that will be used to encrypt and decrypt throughout the program
"""
def key_gen():
        global key
        contin = 'true'
        while contin == 'true':
                key = input('Create your 16 byte key:\n')
                length = len(key)
                if length == 16:
                        key = bytes(key, 'ascii')
                        contin = 'done'
                        print(type(key))
                        print(key)
                        enc = Dencrypt(key)
                else:
                        print('Key not long enough')
        
"""
key = b'fishcakes!@PARIS'
print(type(key))
print(key)

class Dencrypt():
        def __init__(self, key):
                self.key=key
                #print(type(key))
                #print(key)

        def pad(self, s):
                return s + b'\0' * (AES.block_size - len(s) % AES.block_size)

        def encrypt_setup(self, message, key):
                message = self.pad(message)
                iv = Random.new().read(AES.block_size)
                cipher = AES.new(key, AES.MODE_CBC, iv)
                return iv + cipher.encrypt(message)

        def decrypt_setup(self, ciphertext, key):
                iv = ciphertext[:AES.block_size]
                cipher = AES.new(key, AES.MODE_CBC, iv)
                text = cipher.decrypt(ciphertext[AES.block_size:])
                return text.rstrip(b'\0')

        def encrypt(self, file):
                pi_file = open(file, 'rb')
                text = pi_file.read()
                encryption = self.encrypt_setup(text, self.key)
                pi_file = open(file + ".enc", 'wb')
                pi_file.write(encryption)
                os.remove(file)

        def decrypt(self, file):
                pi_file = open(file, 'rb')
                ciphertext = pi_file.read()
                decryption = self.decrypt_setup(ciphertext, self.key)
                pi_file = open(file[:-4], 'wb')
                pi_file.write(decryption)
                os.remove(file)

enc = Dencrypt(key)              
#main function that connects all of the other functions
def program():
	contin = 'true'
	while contin == 'true':
                print()
                print(
			'd = Add a directory permissions\n'
			'f = Add a file permissions\n'
			'cd = Compare a directory permissions\n'
			'cf = Compare a file permissions\n'
			'cda = Compare all directory permissions\n'
			'cfa = Compare all file permissions\n'
			'k = Create key\n'
                        'en = Encrypt a file\n'
                        'de = Decrypt a file\n'
			'q = End program'
			)
                print()
                option = input('Select an option:\n')
                if option == 'q':
                        contin = 'false'
                elif option == 'd':
                        
                        try:
                                #This part attempts to read the content in the dirp.txt file and stores it into a dictionary
                                read_dir()
                                #This part now deletes the dirp.txt file if it exsist
                                subprocess.check_output(['rm', '-f', '/root/Documents/dirp.txt'])
                        except:
                                print('Making a new file')

                        #The data stored in the dictionary will now be edited
                        org_dirdic()
                        #The newly edited dictionary is now stored back into the dirp.txt file
                        write_dir()
                        
                elif option == 'f':
                        
                        try:
                                #This part attempts to read the content in the firp.txt file and stores it into a dictionary
                                read_file()
                                #This part now deletes the firp.txt file if it exsist
                                subprocess.check_output(['rm', '-f', '/root/Documents/firp.txt'])
                        except:
                                print('Making a new file')
                        #The data stored in the dictionary will now be edited
                        org_filehashdic()
                        #The newly edited dictionary is now stored back into the firp.txt file
                        write_file()
			
                elif option == 'cd':
                        try:
                                input_dir()
                                new_dirhashdic(dirc, dir_hash)
                                read_dir()
                                comp_dir()
                        except:
                                print('You need to decrypt some data first')
			
                elif option == 'cf':
                        try:
                                input_file()
                                new_filehashdic(file, file_hash)
                                read_file()
                                comp_file()
                        except:
                                print('You need to decrypt some data first')
			
                elif option == 'cda':
                        try:
                                comp_all_dir()
                                
                        except:
                                print('You need to decrypt some data first')
                        
                elif option == 'cfa':
                        try:
                                comp_all_file()
                        except:
                                print('You need to decrypt some data first')
                        
                elif option == 'k':
                        key_gen()
                        
                elif option == 'en':
                        choice = input('What do you want to encrypt?\n'
                                       'Directories = d\n'
                                       'Files = f\n'
                                       ).lower()
                        if choice == 'd':
                                enc.encrypt('/root/Documents/dirp.txt')

                        elif choice == 'f':
                                enc.encrypt('/root/Documents/firp.txt')

                        else:
                                print('Not a valid option')

                elif option == 'de':
                        choice = input('What do you want to decrypt?\n'
                                       'Directories = d\n'
                                       'Files = f\n'
                                       ).lower()
                        if choice == 'd':
                                enc.decrypt('/root/Documents/dirp.txt.enc')

                        elif choice == 'f':
                                enc.decrypt('/root/Documents/firp.txt.enc')

                        else:
                                print('Not a valid option')
                                
                else:
                        print('ERROR: Not a valid option\n')
                        print()

program()

