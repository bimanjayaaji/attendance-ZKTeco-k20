# -*- coding: utf-8 -*-

'''
to take fingerprint
'''

from ctypes import sizeof
import os
import sys

CWD = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(CWD)
sys.path.append(ROOT_DIR)

from zk import ZK, const


conn = None
zk = ZK('192.168.0.119', port=4370)
try:
    conn = zk.connect()
    print ('Disabling device ...')
    conn.disable_device()
    zk.enroll_user(uid = 4,user_id='4')

    print ('Enabling device ...')
    conn.enable_device()
except Exception as e:
    print ("Process terminate : {}".format(e))
finally:
    if conn:
        conn.disconnect()
