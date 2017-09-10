#!/usr/bin/python

# def encodeChinese(msg):
#     type = sys.getfilesystemencoding()
#     return msg.decode('UTF-8').encode(type)

import json,sys

def LookupNfsList():
    print("LookupNfsList")
    print("0x00090010")
    send = {
        "agentIp": "192.168.2.88",
    }
    recv = {
        "nfsList": [
            {
                "name": "share1",
                "path": "/mnt/server_dir1",
                "parameter": "rw,sync,no_root_squash,fsid=0",
                "mp": "/mnt/client_dir1",
                "mpState": "mounted",
                "state": "running",
                "client": [
                    {
                        "ip": "192.168.2.92",
                        "state": "mounted",
                    },
                    {
                        "ip": "192.168.2.93",
                        "state": "mounted",
                    },
                ],
            },
            # {
            #     "name": "share2",
            #     "path": "/mnt/server_dir2",
            #     "parameter": "rw,sync,all_squash,fsid=0",
            #     "mp": "/mnt/client_dir1",
            #     "mpState": "umounted",
            #     "state": "running",
            #     "client": [
            #         {
            #             "ip": "192.168.2.92",
            #             "state": "mounted",
            #         },
            #         {
            #             "ip": "192.168.2.93",
            #             "state": "mounted",
            #         },
            #     ],
            # },
        ]
    }
    return (send, recv)

def CreateNfs():
    print("CreateNfs")
    print("0x00090020")
    send = {
        "agentIp": "192.168.2.88",
        "name": "share2",
        "path": "/mnt/server_dir2",
        "parameter": "rw,sync,all_squash,fsid=0",
        "mp": "/mnt/client_dir1",
        "client": [
            {
                "ip": "192.168.2.92",
                "password": "111111",
            },
            {
                "ip": "192.168.2.93",
                "password": "111111",
            },
        ],
    }
    recv = {
        "info": "add 192.168.2.92,192.168.2.93 error"
    }
    return (send, recv)

def EditNfs():
    print("EditNfs")
    print("0x00090040")
    send = {
        "agentIp": "192.168.2.88",
        "name": "share2",
        "path": "/mnt/server_dir2",
        "parameter": "rw,sync,all_squash,fsid=0",
        "mp": "/mnt/client_dir1",
        "newClient": [
           {
               "ip": "192.168.2.94",
               "password": "111111",
           },
           {
               "ip": "192.168.2.95",
               "password": "111111",
           },
        ],
    }
    recv = {
        "info": "add 192.168.2.95 error"
    }
    return (send, recv)

def RemoveNfs():
    print("RemoveNfs")
    print("0x00090030")
    send = { 
        "agentIp": "192.168.2.88",
        "name": [
            "share1", 
            "share2", 
        ],
    }
    recv = {}
    return (send, recv)

def StartNfs():
    print("StartNfs")
    print("0x00090050")
    send = {}
    recv = {}
    return (send, recv)

def StopNfs():
    print("StopNfs")
    print("0x00090060")
    send = {}
    recv = {}
    return (send, recv)

def MountNfsClient():
    print("MountNfsClient")
    print("0x00090070")
    send = { 
        "agentIp": "192.168.2.88",
        "client": "192.168.2.92", 
    }
    recv = {}
    return (send, recv)

def MountNfsAllClient():
    print("MountNfsAllClient")
    print("0x000900A0")
    send = { 
        "agentIp": "192.168.2.88",
        "name": "share1",
        "client": [
            "192.168.2.94",
            "192.168.2.95",
        ],
    }
    recv = {}
    return (send, recv)

def UmountNfsClient():
    print("UmountNfsClient")
    print("0x00090080")
    send = { 
        "agentIp": "192.168.2.88",
        "client": "192.168.2.92", 
    }
    recv = {}
    return (send, recv)

def UmountNfsAllClient():
    print("UmountNfsAllClient")
    print("0x000900B0")
    send = { 
        "agentIp": "192.168.2.88",
        "name": "share1",
        "client": [
            "192.168.2.94",
            "192.168.2.95",
        ],
    }
    recv = {}
    return (send, recv)
def RemoveNfsClient():
    print("RemoveNfsAllClient")
    print("0x00090090")
    send = { 
        "agentIp": "192.168.2.88",
        "name": "share1",
        "client": "192.168.2.94",
    }
    recv = {}
    return (send, recv)


def main():
    if len(sys.argv) != 2:
        print("invalid argument, exit")
        return -1
    elif sys.argv[1] == "list":
        packet = LookupNfsList()
    elif sys.argv[1] == "create":
        packet = CreateNfs()
    elif sys.argv[1] == "remove":
        packet = RemoveNfs()
    elif sys.argv[1] == "edit":
        packet = EditNfs()
    elif sys.argv[1] == "start":
        packet = StartNfs()
    elif sys.argv[1] == "stop":
        packet = StopNfs()
    elif sys.argv[1] == "mountclient":
        packet = MountNfsClient()
    elif sys.argv[1] == "mountall":
        packet = MountNfsAllClient()
    elif sys.argv[1] == "umountclient":
        packet = UmountNfsClient()
    elif sys.argv[1] == "umountall":
        packet = UmountNfsAllClient()
    elif sys.argv[1] == "removeclient":
        packet = RemoveNfsClient()
    else:
        print("invalid argument, exit")
        return -1


    print("REQUEST PACKET:")
    print(json.dumps(packet[0], sort_keys=True, indent=4),"\n")
    print("RESPOND PACKET: ok")
    print(json.dumps(packet[1], sort_keys=True, indent=4),"\n")

main()
