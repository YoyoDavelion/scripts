#!/bin/bash
if [ $1 ]; then
for i in $(seq 2 254); do
        timeout 1 bash -c "ping -c 1 $1$i > /dev/null 2>&1" && echo "Host $1$i active"  &

done; wait
else
echo "Usage: ./hostDiscovery.sh <ip address without host ip: ex 192.168.1.>"
fi
