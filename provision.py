"""
Provision device after ZTP enabled SSH
Workflow based
"""

from __future__ import print_function
import time
import re
import sys
import os

import lxml.etree as ET
from argparse import ArgumentParser
from ncclient import manager
from ncclient.operations import RPCError
import xmltodict
import json
import ztpcli
import spark

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
