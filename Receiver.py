#!/usr/bin/env python
'''
Created on Oct 20, 2016

@author: nwangsa
'''

import stomp
import time

class MyListener(object):
    def on_error(self, headers, message):
        print('(ERROR): ' + message)
    def on_message(self, headers, message):
        print(message)

dest='/topic/topic_python'
conn=stomp.Connection([('vm517.cii.c.apcoe2.boeing.com', 61613)])

print('set up Connection')
conn.set_listener('python_test_listener', MyListener())
print('Set up listener')

name = input('Enter a Client ID: ')

conn.start()
print('started connection')

conn.connect(wait=True, headers={'client-id': name});
print('connected')
conn.subscribe(destination=dest, id=1, ack='auto', headers={'transformation' : 'jms-xml'} )
print('subscribed')

print("Listening...")
listening = True
while(listening is True):
    time.sleep(120)
    print("Listening...")
# 
# time.sleep(500)

conn.disconnect()
print('disconnected')
