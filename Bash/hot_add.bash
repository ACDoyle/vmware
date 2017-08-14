#!/bin/bash
# William Lam
# http://engineering.ucsb.edu/~duonglt/vmware/
# hot-add cpu to LINUX system using vSphere ESX(i) 4.0
# 08/09/2009

for CPU in $(ls /sys/devices/system/cpu/ | grep cpu | grep -v idle)
do
        CPU_DIR="/sys/devices/system/cpu/${CPU}"
        echo "Found cpu: \"${CPU_DIR}\" ..."
        CPU_STATE_FILE="${CPU_DIR}/online"
	if [ -f "${CPU_STATE_FILE}" ]; then
		STATE=$(cat "${CPU_STATE_FILE}" | grep 1)
		if [ "${STATE}" == "1" ]; then	
			echo -e "\t${CPU} already online"
		else
			 echo -e "\t${CPU} is new cpu, onlining cpu ..."
			 echo 1 > "${CPU_STATE_FILE}"
		fi
	else 
		echo -e "\t${CPU} already configured prior to hot-add"
	fi
echo $CPU
done



!/bin/bash
# William Lam
# http://engineering.ucsb.edu/~duonglt/vmware/
# hot-add memory to LINUX system using vSphere ESX(i) 4.0
# 08/09/2009

if [ "$UID" -ne "0" ]
 then
 echo -e "You must be root to run this script.\nYou can 'sudo' to get root access"
 exit 1
fi

for MEMORY in $(ls /sys/devices/system/memory/ | grep memory)
do
 SPARSEMEM_DIR="/sys/devices/system/memory/${MEMORY}"
 echo "Found sparsemem: \"${SPARSEMEM_DIR}\" ..."
 SPARSEMEM_STATE_FILE="${SPARSEMEM_DIR}/state"
 STATE=$(cat "${SPARSEMEM_STATE_FILE}" | grep -i online)
 if [ "${STATE}" == "online" ]; then
 echo -e "\t${MEMORY} already online"
 else
 echo -e "\t${MEMORY} is new memory, onlining memory ..."
 echo online > "${SPARSEMEM_STATE_FILE}"
 fi
done

