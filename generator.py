import os
import sys
import hashlib

site_name='google'
s = hashlib.sha256(site_name.encode('utf-8')).hexdigest()
print(s)