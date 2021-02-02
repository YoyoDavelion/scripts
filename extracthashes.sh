#!/bin/bash
# Give the script execution perms with chmod +x exctracthashes.sh
# Then run it with sudo ./extracthashes.sh or sudo sh extracthashes.sh
if ! [ $(id -u) = 0 ]; then
        echo "Run it with sudo"
        exit 1
fi
$(rm -r extractedhashes 2>/dev/null)
length=0
hash_field=None
for i in $(cat /etc/shadow | cut -d ":" -f 1,2); do 
        hash_field=$(echo "$i" | cut -d ":" -f 2)
        length=${#hash_field}
        if [ $length -gt 20 ]; then 
                echo "Hash extracted: $i"
                $(echo $i >> extractedhashes)
        fi
done
echo "Hashes has been exported to the file extractedhashes"
#Script by YoyoDavelion
