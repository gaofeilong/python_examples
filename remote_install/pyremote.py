#!/usr/bin/python2
import pexpect,sys

mypassword = sys.argv[1]
child = pexpect.spawn('ssh root@192.168.1.92 mkdir -p /tmp/tmp.dir')
child.expect('password:')
child.sendline (mypassword)
