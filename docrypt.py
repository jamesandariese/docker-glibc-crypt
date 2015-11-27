from __future__ import print_function
import crypt
import getpass
import random
import string
import sys

saltset = string.ascii_letters + string.digits + './'

if len(sys.argv) > 1 and sys.argv[1] == '-d':
    salt = random.choice(saltset) + random.choice(saltset)
else:
    salt = '$6$' + ''.join(map(lambda _: random.choice(saltset), range(16)))

print(crypt.crypt(getpass.getpass("Password: "), salt))
