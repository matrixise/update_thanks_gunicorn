#!/usr/bin/env python
from __future__ import print_function
import os
import sys
#import collections
from pprint import pprint as pp
from validate_email import validate_email
from email.utils import parseaddr
import DNS.Base

addresses = set()
bad_addresses = set()
collection = []

lines = sys.stdin.readlines()

lines = list(reversed(lines))

pp(lines)

#sys.exit(0)

for author in map(str.strip, lines):
    realname, email_address = parseaddr(author)
    print("Author: %r" % (author,))


    if email_address not in addresses:
        if email_address in bad_addresses:
            continue
        else:
            try:
                value = validate_email(email_address) #, check_mx=True, verify=False)
                if value:
                    addresses.add(email_address)
                    collection.append(author)
                else:
                    bad_addresses.add(email_address)
            except DNS.Base.TimeoutError:
                bad_addresses.add(email_address)


open('result.txt', 'w').write('\n'.join(collection))
