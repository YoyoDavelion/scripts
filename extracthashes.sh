#!/bin/bash
if ! [ $(id -u) = 0 ]; then
	echo "Ejecutalo con sudo"
	exit 1
fi
$(rm -r extractedhashes 2>/dev/null)
longitud=0
for i in $(cat /etc/shadow | cut -d ":" -f 1,2); do 
	longitud=${#i}
	if [ $longitud -gt 20 ]; then 
		echo "Hash extraido: $i"
		$(echo $i >> extractedhashes)
	fi
done
echo "Los hashes han sido exportados al fichero extractedhashes"
#Script by YoyoDavelion
