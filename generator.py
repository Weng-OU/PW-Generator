import os
import sys
import hashlib
'''
keep one short password in mind (ex. "Nj/ ")
Randomly pick up a salt (input first)
choose website (input second)
combine salt and website to generator hash, choose a few numbers as the initial password (ex. first five yards and last five yards)
combine password in mind and initial password to finial password (output)
use txt to input second?
use txt to save output?
default is read from file
if no file, output error message
option is by manual input
'''
# site_name='google'
# s = hashlib.sha256(site_name.encode('utf-8')).hexdigest()
# print(s)

if __name__=="__main__":
    salt = '123' #sys.argv[1]
    website = '456' #sys.argv[2]

    hash_website = hashlib.sha256(salt.encode('utf-8') + website.encode('utf-8')).hexdigest()
    print(hash_website)