# -*- coding: utf-8 -*-


import os
import hashlib


with open('envs.py') as fd:
    code = fd.read()
dh = hashlib.sha256(code).hexdigest()
print(dh)