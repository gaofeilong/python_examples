#!/usr/bin/python

# def encodeChinese(msg):
#     type = sys.getfilesystemencoding()
#     return msg.decode('UTF-8').encode(type)

import json,sys

def LookupAdfsMpList():
    print("LookupAdfsMpList")
    print("0x000400A0")
    send = { 
        "agentIp": "192.168.2.88",
    }
    recv = {
        "adfsList": [
            {
                "mp": "/mnt/adfs/sdb1/mp",
                "capacity": "1073741824",
                "total": "1048576",
                "real": "699050",
                "ratio": "1.5",
                "left": "1073042774",
                "state": "mounted",
                "firstDataPath": "/mnt/adfs/sdb1",
                "otherDataPath": [
                    "/mnt/adfs/sdb2",
                    "/mnt/adfs/sdb3",
                ],
            },
            {
                "mp": "/mnt/adfs/sdc1/mp",
                "capacity": "1073741824",
                "total": "1048576",
                "real": "699050",
                "ratio": "1.5",
                "left": "1073042774",
                "state": "umounted",
                "firstDataPath": "/mnt/adfs/sdc1",
                "otherDataPath": [
                    "/mnt/adfs/sdc2",
                    "/mnt/adfs/sdc3",
                ],
            }
        ],
    }
    return (send, recv)

def CreateAdfsMp():
    print("CreateAdfsMp")
    print("0x000400B0")
    send = { 
        "agentIp": "192.168.2.88",
        "firstDataPath": "/mnt/adfs/sdc1",
        "otherDataPath": [
            "/mnt/adfs/sdc2",
            "/mnt/adfs/sdc3",
        ],
    }
    recv = {}
    return (send, recv)

def RemoveAdfsMp():
    print("RemoveAdfsMp")
    print("0x000400C0")
    send = { 
        "agentIp": "192.168.2.88",
        "firstDataPath": "/mnt/sdb1",
    }
    recv = {}
    return (send, recv)

def ModifyAdfsMp():
    print("ModifyAdfsMp")
    print("0x000400D0")
    send = { 
        "agentIp": "192.168.2.88",
        "firstDataPath": "/mnt/sdb1",
        "newDataPath": [
            "/mnt/adfs/sdc2",
            "/mnt/adfs/sdc3",
        ],
    }
    recv = {}
    return (send, recv)

def MountAdfsMp():
    print("MountAdfsMp")
    print("0x000400E0")
    send = { 
        "agentIp": "192.168.2.88",
        "firstDataPath": "/mnt/sdb1",
    }
    recv = {}
    return (send, recv)

def UmountAdfsMp():
    print("UmountAdfsMp")
    print("0x000400F0")
    send = { 
        "agentIp": "192.168.2.88",
        "firstDataPath": "/mnt/sdb1",
    }
    recv = {}
    return (send, recv)

############################################################
def main():
    if len(sys.argv) != 2:
        print("invalid argument, exit")
        return -1
    elif sys.argv[1] == "list":
        packet = LookupAdfsMpList()
    elif sys.argv[1] == "create":
        packet = CreateAdfsMp()
    elif sys.argv[1] == "remove":
        packet = RemoveAdfsMp()
    elif sys.argv[1] == "modify":
        packet = ModifyAdfsMp()
    elif sys.argv[1] == "mount":
        packet = MountAdfsMp()
    elif sys.argv[1] == "umount":
        packet = UmountAdfsMp()
    else:
        print("invalid argument, exit")
        return -1


    print("REQUEST PACKET:")
    print(json.dumps(packet[0], sort_keys=True, indent=4),"\n")
    print("RESPOND PACKET: ok")
    print(json.dumps(packet[1], sort_keys=True, indent=4),"\n")

main()
