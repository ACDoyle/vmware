#!/usr/bin/env python

import pyVim
from pyVim import connect
my_cluster = connect.Connect("vcenter", 443, "vcap\Administrator", "7oWczaR1ek")
print("Successfully connect to vCenter")
searcher = my_cluster.content.searchIndex
vm = searcher.FindByIp(ip="10.10.10.196", vmSearch=True)
print vm.config.name
print vm.summary
connect.Disconnect(my_cluster)
