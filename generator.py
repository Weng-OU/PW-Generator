import os
import sys
import hashlib
import argparse

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

if __name__ == "__main__":
    # salt = '123'  # sys.argv[1]
    # website = '456'  # sys.argv[2]
    # hash_website = hashlib.sha256(salt.encode('utf-8') + website.encode('utf-8')).hexdigest()
    # print(hash_website)

    pw_source_folder = 'pw-source'
    website_pw_list = []
    salt_path = os.path.join(os.getcwd(), pw_source_folder, 'salt.txt')
    website_path = os.path.join(os.getcwd(), pw_source_folder, 'web-site.txt')
    f_salt = open(salt_path, 'r', encoding='utf-8')
    salt_each_lines = f_salt.readlines()
    f_salt.close()
    f_website = open(website_path, 'r', encoding='utf-8')
    website_each_lines = f_website.readlines()
    f_website.close()
    f_output = open(os.path.join(os.getcwd(), pw_source_folder, 'output.txt'), 'w')
    for website_line in website_each_lines:
        website = website_line.split(":")[0].strip()
        url = website_line.split(':')[1].strip()
        salt = salt_each_lines[0].split(':')[1].strip()
        # print('websiite:'+website)
        # print('url:' + url)
        hash_pw = hashlib.sha256(salt.encode('utf-8') + url.encode('utf-8')).hexdigest()
        init_hash_pw = hash_pw[:4] + hash_pw[60:]
        # print('{} : {}'.format(website, hash_pw))
        # print(init_hash_pw)
        website_pw_list.append(website)
        website_pw_list.append(init_hash_pw)
        # print(website_pw_list)
    for i in range(0, len(website_pw_list), 2):
        print('{} : {}'.format(website_pw_list[i], website_pw_list[i + 1]), file=f_output)
        # print(website_pw_list[i])
    f_output.close()
