from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
import hashlib
import subprocess


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
                        org_dir_dic[dirc]=dir_hash
                    except:
                        print('Improper path')
                    
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
                                org_file_dic[file]=file_hash
                        except:
                                print('Improper path')
                        
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
#This part of the code would not work properly for odd reasons
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
#This is the default key I set up in the code with some content below for information display
#with the issue I am having
key = b'fishcakes!@PARIS'               #######COMMENT########
print(type(key))                        #######COMMENT########
print(key)                              #######COMMENT########

#Here is my class for this assignment organizing encryption part of the program away from the rest
class Dencrypt():
        def __init__(self, key):
                self.key=key
                #print(type(key))               ##########UNCOMMENT#####
                #print(key)                     ########UNCOMMENT#####

#The pad is what extends blocks of text that are not long enough for proper encryption
#There is a function now for this in Pycryptodome but it was easier for me to understand
#       the encryption process by making my own
        def pad(self, text):
                #b'\0'  basicaly is additional empty byte segments added for encryption
                #AES.block_size is the default 16 byte required block size for encryption
                return text + b'\0' * (AES.block_size - len(text) % AES.block_size)

#This function is the initial creation of the cipher, iv, encryption, and connection
        def encrypt_setup(self, message, key):
                message = self.pad(message)             #this calls pad for additional bytes if needed
                iv = Random.new().read(AES.block_size)  #creates random 16 byte number for the iv
        #MODE_CBC acknowledges Cipher Block Chaining which is the 16 bytes
                cipher = AES.new(key, AES.MODE_CBC, iv) #creates the cipher with the iv and key
                return iv + cipher.encrypt(message)     #encrypts the block with the cipher and adds
                                                        #the iv for complexing the encryption

#This function is the initial creation of the cipher, iv, decryption, and striping
        def decrypt_setup(self, ciphertext, key):
                iv = ciphertext[:AES.block_size]        #recreats random 16 byte number for the iv
                cipher = AES.new(key, AES.MODE_CBC, iv) #recreates the cipher with the iv and key
                text = cipher.decrypt(ciphertext[AES.block_size:])      #decrypts the ciphertext
                return text.rstrip(b'\0')               #strips extra bytes from pad when needed

#The function puts the encryted text into a new document and removes the old documents
        def encrypt(self, file):
                pi_file = open(file, 'rb')      #opens a file in read byte mode
                text = pi_file.read()           #reads
                encryption = self.encrypt_setup(text, self.key) #runs the encrypt_setup function
                pi_file = open(file + ".enc", 'wb')     #open a new file with .enc at the end in write byte mode
                pi_file.write(encryption)       #writes the encrpted text to the file
                os.remove(file)                 #removes the original documents

#The funcition puts the decrypted text into a new doeuments and removes the encrypted documents
        def decrypt(self, file):
                pi_file = open(file, 'rb')      #opens the encrypted file in read byte mode
                ciphertext = pi_file.read()     #reads the encrypted document
                decryption = self.decrypt_setup(ciphertext, self.key)   #runs the decrypt_setup function
                pi_file = open(file[:-4], 'wb') #opens a new without ".enc" in write byte mode
                pi_file.write(decryption)       #writes the decrypted text
                os.remove(file)                 #removes the encrypted document

enc = Dencrypt(key)             ########COMMMENT########
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
                                input_dir()     #choose a directory for comparison
                                new_dirhashdic(dirc, dir_hash)  #create a new dictionary for comparison
                                read_dir()      #reads documents with directory permissions into a dictionary
                                comp_dir()      #compares the dictionaries
                        except:
                                print('You need to decrypt some data first')
			
                elif option == 'cf':
                        try:
                                input_file()    #choose a file for comparison
                                new_filehashdic(file, file_hash)#create a new dictionary for comparison
                                read_file()     #reads documents with file permissions into a dictionary
                                comp_file()     #compares the dictionaries
                        except:
                                print('You need to decrypt some data first')
			
                elif option == 'cda':
                        try:
                                comp_all_dir() #comparies all of the known hashes with new ones

                        except:
                                print('You need to decrypt some data first')
                        
                elif option == 'cfa':
                        try:
                                comp_all_file() #comparies all of the known hashes with new ones
                        except:
                                print('You need to decrypt some data first')
                        
                elif option == 'k':
                        pass                    ##########Commment######
                        key_gen()
                        
                elif option == 'en':
                        #Choose which file to encrypt
                        choice = input('What do you want to encrypt?\n'
                                       'Directories = d\n'
                                       'Files = f\n'
                                       ).lower()
                        if choice == 'd':
                                enc.encrypt('/root/Documents/dirp.txt') #only needs to call encrypt function

                        elif choice == 'f':
                                enc.encrypt('/root/Documents/firp.txt')

                        else:
                                print('Not a valid option')

                elif option == 'de':
                        #Choose which file to decrypt
                        choice = input('What do you want to decrypt?\n'
                                       'Directories = d\n'
                                       'Files = f\n'
                                       ).lower()
                        if choice == 'd':
                                enc.decrypt('/root/Documents/dirp.txt.enc')#only needs to call decrypt function

                        elif choice == 'f':
                                enc.decrypt('/root/Documents/firp.txt.enc')

                        else:
                                print('Not a valid option')
                                
                else:
                        print('ERROR: Not a valid option\n')
                        print()

#Runs the program
program()
	

