import os
import sys
import hashlib
import argparse


def read_from_file(file_name, folder_name):
    file_path = os.path.join(os.getcwd(), folder_name, file_name)
    file_open = open(file_path, 'r', encoding='utf-8')
    return file_open.readlines()


def parser_salt_website_argument():
    parser = argparse.ArgumentParser(description='need write here')
    parser.add_argument('-salt', '-s', type=str, help='Add salt to mess up the encryption result.', default='')
    parser.add_argument('-url', '-u', type=str, help='Treat the destination URL as an encrypted seed.', default='')
    return parser


if __name__ == "__main__":
    pw_source_folder = 'pw-source'
    website_pw_list = []
    salt_each_lines = []
    website_each_lines = []

    parser = parser_salt_website_argument()
    args = parser.parse_args()
    if args.salt == '':
        salt_each_lines = read_from_file('salt.txt', pw_source_folder)
    else:
        salt_each_lines.append('1:{}'.format(args.salt))

    if args.url == '':
        website_each_lines = read_from_file('web-site.txt', pw_source_folder)
    else:
        website_each_lines.append('{}:{}'.format(args.url, args.url))


    f_output = open(os.path.join(os.getcwd(), pw_source_folder, 'output.txt'), 'w')
    for website_line in website_each_lines:
        website = website_line.split(":")[0].strip()
        url = website_line.split(':')[1].strip()
        salt = salt_each_lines[0].split(':')[1].strip()
        hash_pw = hashlib.sha256(salt.encode('utf-8') + url.encode('utf-8')).hexdigest()
        init_hash_pw = hash_pw[:4] + hash_pw[60:]
        website_pw_list.append(website)
        website_pw_list.append(init_hash_pw)
    for i in range(0, len(website_pw_list), 2):
        print('{} : {}'.format(website_pw_list[i], website_pw_list[i + 1]), file=f_output)
    f_output.close()
