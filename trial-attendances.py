# -*- coding: utf-8 -*-
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
    print ('--- Get User ---')
    att = conn.get_attendance()

    # print(att[0].user_id, type(att[0].user_id))
    # print(att[0].timestamp, type(att[0].timestamp))
    # print(att[0].status, type(att[0].status))
    # print(att[0].punch, type(att[0].punch))

    for atten in att:
        print(atten)

    print ('Enabling device ...')
    conn.enable_device()
except Exception as e:
    print ("Process terminate : {}".format(e))
finally:
    if conn:
        conn.disconnect()
