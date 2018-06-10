#!/usr/bin/env python3.6

import sys
import random
import string

# from user import User
# from credential import Credential

def passlen(l):
    _all = string.ascii_letters+ string.punctuation+string.digits
    return "".join(random.sample(_all,l))