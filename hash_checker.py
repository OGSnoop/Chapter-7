from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join
import time
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
key=''
#system file for directories' permissions is dirp.txt
#system file for file permissions' is franky.txt

def input_file():
	global file, file_hash
	file = input('Give the path of the file:\n')
	try:
		perm = subprocess.check_output(['ls', '-l', file])
		file_hash = hashlib.sha1(perm).hexdigest()
	except:
		print('Improper path')


def input_dir():
	global dirc, dir_hash
	dirc = input('Give the path of the directory:\n')
	try:
		perm = subprocess.check_output(['ls', '-l', dirc])
		dir_hash = hashlib.sha1(perm).hexdigest()
	except:
		print('Improper path')

def new_dirhashdic(dirc, dir_hash):
	global dir_hash_dic
	dir_hash_dic[dirc]=dir_hash

def new_filehashdic(file, file_hash):
	global file_hash_dic
	file_hash_dic[file]=file_hash

def org_dirdic():
        global org_dir_dic, dirc, dir_hash
        contin = 'y'
        while contin == 'y':
                contin = input('Do you wish to continue [y/n]]:\n').lower()
                if contin == 'y':
                    dirc = input('Give the path of the directory:\n')
                    try:
                        perm = subprocess.check_output(['ls', '-l', dirc])
                        dir_hash = hashlib.sha1(perm).hexdigest()
                    except:
                        print('Improper path')
                    org_dir_dic[dirc]=dir_hash
                elif contin == 'n':
                    contin = 'n'
                else:
                    print('Not a valid input')
                    contin = 'y'

def org_filehashdic():
	global org_file_dic, file, file_hash
	contin = 'y'
	while contin == 'y':
                contin = input('Do you wish to continue [y/n]:\n').lower()
                if contin == 'y':
                        file = input('Give the path of the file:\n')
                        try:
                                perm = subprocess.check_output(['ls', '-l', file])
                                file_hash = hashlib.sha1(perm).hexdigest()
                        except:
                                print('Improper path')
                        org_file_dic[file]=file_hash
                elif contin == 'n':
                        contin == 'n'
                else:
                        print('Not a valid input')
                        contin = 'y'
                

def key_gen():
	key = input('Select your key:\n')

def write_dir():
        global org_dir_dic
        dirp = open('/root/Documents/dirp.txt', 'a')
        for key,value in org_dir_dic.items():
                dirp.write('{a}:{b}'.format(a=key, b=value))
                dirp.write('\n')
        dirp.close()

def write_file():
        global org_file_dic
        firp = open('/root/Documents/firp.txt', 'a')
        for key,value in org_file_dic.items():
                firp.write('{a}:{b}\n'.format(a=key, b=value))
        firp.close()

def read_dir():
        global org_dir_dic
        dirp = open('/root/Documents/dirp.txt', 'r')
        dirp_lines = dirp.readlines()
        dirp.close()
        for i in range(len(dirp_lines)):
                line = dirp_lines[i]
                tokens = line.split(':')
                org_dir_dic[tokens[0]]=tokens[1]

def read_file():
        global org_file_dic
        firp = open('/root/Documents/firp.txt', 'r')
        firp_lines = firp.readlines()
        firp.close()
        for i in range(len(firp_lines)):
                line = firp_lines[i]
                tokens = line.split(':')
                org_file_dic[tokens[0]]=tokens[1]

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

def comp_all_dir():
        global dir_hash_dic, org_dir_dic
        dirp = open('/root/Documents/dirp.txt', 'r')
        dirp_lines = dirp.readlines()
        dirp.close()
        dirlist = []
        for i in range(len(dirp_lines)):
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

def comp_all_file():
        global file_hash_dic, org_file_dic
        firp = open('/root/Documents/firp.txt', 'r')
        firp_lines = firp.readlines()
        firp.close()
        firlist = []
        for i in range(len(firp_lines)):
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


def program():
	contin = 'true'
	while contin == 'true':
                print(
			'd = Add a directory permissions\n'
			'f = Add a file  permissions\n'
			'cd = Compare a directory permissions\n'
			'cf = Compare a file permissions\n'
			'cda = Compare all directory permissions\n'
			'cfa = Compare all file permissions\n'
			'k = Create key\n'
			'q = End program'
			)
                print()
                option = input('Select an option:\n')
                if option == 'q':
                        contin = 'false'
                elif option == 'd':
                        try:
                                read_dir()
                                subprocess.check_output(['rm', '-f', '/root/Documents/dirp.txt'])
                        except:
                                print('A new file will be created')
                        org_dirdic()
                        write_dir()
                        
                elif option == 'f':
                        try:
                                read_file()
                                subprocess.check_output(['rm', '-f', '/root/Documents/firp.txt'])
                        except:
                                print('A new file will be created')
                        org_filehashdic()
                        write_file()
			
                elif option == 'cd':
                        input_dir()
                        new_dirhashdic(dirc, dir_hash)
                        read_dir()
                        comp_dir()
			
                elif option == 'cf':
                        input_file()
                        new_filehashdic(file, file_hash)
                        read_file()
                        comp_file()
			
                elif option == 'cda':	
                        comp_all_dir()
                        
                elif option == 'cfa':
                        comp_all_file()
                        
                elif option == 'k':
                        key_gen()
                else:
                        print('ERROR: Not a valid option\n')
                        print()

program()

