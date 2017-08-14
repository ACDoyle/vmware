#!/usr/bin/env python

from pyVim.connect import SmartConnect, Disconnect
import ssl

s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s.verify_mode = ssl.CERT_NONE

try:
  c = SmartConnect(host="vcenter", user="vcap\Administrator",pwd="7oWczaR1ek")
  print('Valid certificate')
except:
  c = SmartConnect(host="vcenter", user="vcap\Administrator",pwd="7oWczaR1ek", sslContext=s)
  print('Invalid or untrusted certificate')

print(c.CurrentTime())
datacenter = c.content.rootFolder.childEntity[0]
vms = datacenter.vmFolder.childEntity

#datastore = datacenter.

#searcher = c.content.searchIndex
#vm = searcher.FindByIp(ip="10.10.10.196", vmSearch=True)
#print vm.summary



for i in vms:
  print(i.name)

print(c.CurrentTime())

Disconnect(c)
