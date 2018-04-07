"""
Provision device after ZTP enabled SSH
Workflow based
"""

from __future__ import print_function
import time
import sys
import os
import ztpcli

def ztp(device):
    """ Output to a file """
    sys.stdout = open('output.txt', 'w')
    wait_sec = 30
    print("Found new ZTP device: %s" % device)
    print("Wait %s seconds (Running ZTP script on device)" % wait_sec)
    time.sleep(wait_sec)
    """ Exec Post Script config """
    ztpcli.postScript(device)
    print("")
    print("You're done!")
    print("")
