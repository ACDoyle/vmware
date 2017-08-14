#!/usr/bin/env python 

#Guest reboot vm

import atexit

#from pyVim import connect
#from pyVmomi import vmodl
from pyVmomi import vim

import pyVim
from pyVim.connect import SmartConnect, Disconnect
import ssl

s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s.verify_mode = ssl.CERT_NONE




def main():
    """
    Simple command-line program for listing the virtual machines on a system.
    """

    try:
        service_instance = SmartConnect(host="vcenter", user="vcap\Administrator",pwd="7oWczaR1ek")
        print('Valid certificate')


        atexit.register(Disconnect, service_instance)

        content = service_instance.RetrieveContent()
        uuid='5029b044-e307-e561-c430-cfc950cd030a'
        vm = content.searchIndex.FindByUuid(None, uuid, True, True)
        if not vm:
            print("Not found")
            return 1

        print("Found: {0}".format(vm.name))
        print("The current powerState is: {0}".format(vm.runtime.powerState))
        # This does not guarantee a reboot.
        # It issues a command to the guest
        # operating system asking it to perform a reboot.
        # Returns immediately and does not wait for the guest
        # operating system to complete the operation.
        vm.RebootGuest()
        print("A request to reboot the guest has been sent.")
        

    except:
        c = SmartConnect(host="vcenter", user="vcap\Administrator",pwd="7oWczaR1ek", sslContext=s)
        print('Invalid or untrusted certificate')
        return -1
 #   except vmodl.MethodFault as error:
 #      print("Caught vmodl fault : " + error.msg)
 #      return -1

    return 0

# Start program
if __name__ == "__main__":
    main()


