# -*- coding: utf-8 -*-
import pythoncom
import pyHook
import pyscreenshot as ImageGrab
import os
from time import gmtime, strftime
from pyHook import HookConstants
from os.path import expanduser

counter = 0
home = expanduser("~")
path = home + "/GJ/img/" + (strftime("%Y_%m_%d", gmtime()))

def mkdir(path):
    print("checking...")
    if not os.path.exists(path):
        print("gonna create")
        os.makedirs(path)
        print("created")
    else:
        print(path + " already exists")


def KeyStroke(event):

    if event.KeyID == HookConstants.VKeyToID('VK_SNAPSHOT'):
        global counter
        counter += 1
        fpath = path + '/shot_' + str(counter) + '.jpg'
        # grab fullscreen
        im = ImageGrab.grab()
        # save image file
        im.save(fpath)
        print("Screenshot done. Name: "+ fpath)
    # pass execution to next hook registered
    return True


if __name__ == "__main__":

    mkdir(path)

    # create and register a hook manager
    kl = pyHook.HookManager()
    kl.KeyDown = KeyStroke

    # register the hook and execute forever
    kl.HookKeyboard()
    pythoncom.PumpMessages()


