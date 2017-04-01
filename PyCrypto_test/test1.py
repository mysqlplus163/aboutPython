#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2017/3/1

# from Crypto import Random
# from Crypto.Hash import SHA
# from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
# from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
# from Crypto.PublicKey import RSA
import base64

s = "X11MAMaqnpPJjU6mMx7UbdIzFnpVFSfQA5XEfgYKq8junOg9ghchFpI0vIO/emGIEpwqfBgmT6qwt0td/P3pwi5CVVIwBx4dwXF9eXrqrnGDOfUSnSAJtkUEroSbVV7WL10CROrP9g4o+NH7A0LjWvewfrcOCRweOFN7ieg6GVqoaxtg3mQgUQEStsFUYjZMw5Qbyhmhdk3sPEtfnJrKSZtZ6bhDfC648utYU7MRijGnZkqPd50SfSWp5fUmxl01wdNZrwZQWE4birnXXfwhBeSokV8xHJTNUx7gFo0BfYqfIxgw6Itj5UPX1jJONhuNTPS1x6IxMg+tod22fsMOQw=="

ss = base64.b64decode(s)
# print(str(ss))

# random_generator = Random.new().read

# with open("public.pem", "rb") as f:
#     key = f.read()
# rsakey = RSA.importKey(key)
# text = rsakey.encrypt()
# cipher = Cipher_pkcs1_v1_5.new(rsakey)
# text = cipher.decrypt(ss)
    # text = cipher.decrypt(ss, random_generator)
# print(text)
