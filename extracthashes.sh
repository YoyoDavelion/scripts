#!/bin/bash
# Give the script execution perms with chmod +x exctracthashes.sh
# Then run it with sudo ./extracthashes.sh or sudo sh extracthashes.sh

# Color pallette
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"


if ! [ $(id -u) = 0 ]; then
        echo "Run it with sudo"
        exit 1
fi
$(rm -r extractedhashes 2>/dev/null)
length=0
hash_field=None
echo ""
echo -e "${yellowColour}Extracting hashes....${endColour}\n"
sleep 1
for i in $(cat /etc/shadow | cut -d ":" -f 1,2); do 
        hash_field=$(echo "$i" | cut -d ":" -f 2)
        length=${#hash_field}
        if [ $length -gt 20 ]; then 
                echo -e "${greenColour}[*] Hash extracted [*] : ${endColour}${grayColour}$i ${endColour}"
                sleep 0.2
                $(echo $i >> extractedhashes)
        fi
done
echo -e "\n${turquoiseColour}Hashes has been exported to the file extractedhashes${endColour}"
echo "

  _____   __  ____   ____  ____  ______      ____   __ __      __ __   ___   __ __   ___   ___     ____  __ __    ___  _      ____  ___   ____  
 / ___/  /  ]|    \ |    ||    \|      |    |    \ |  |  |    |  |  | /   \ |  |  | /   \ |   \   /    ||  |  |  /  _]| |    |    |/   \ |    \ 
(   \_  /  / |  D  ) |  | |  o  )      |    |  o  )|  |  |    |  |  ||     ||  |  ||     ||    \ |  o  ||  |  | /  [_ | |     |  ||     ||  _  |
 \__  |/  /  |    /  |  | |   _/|_|  |_|    |     ||  ~  |    |  ~  ||  O  ||  ~  ||  O  ||  D  ||     ||  |  ||    _]| |___  |  ||  O  ||  |  |
 /  \ /   \_ |    \  |  | |  |    |  |      |  O  ||___, |    |___, ||     ||___, ||     ||     ||  _  ||  :  ||   [_ |     | |  ||     ||  |  |
 \    \     ||  .  \ |  | |  |    |  |      |     ||     |    |     ||     ||     ||     ||     ||  |  | \   / |     ||     | |  ||     ||  |  |
  \___|\____||__|\_||____||__|    |__|      |_____||____/     |____/  \___/ |____/  \___/ |_____||__|__|  \_/  |_____||_____||____|\___/ |__|__|


"
#Script by YoyoDavelion

