#!/usr/bin/python3
# Ejecutar script con sudo python3 changeinterface.py
import os
address = "{address}"
net = '"net"'
add = '"add"'
mac = input("Introduce la mac de la interfaz que quieres cambiar: ")
mac = '"{}"'.format(mac)
new_name = input("Introduce el nuevo nombre para la interfaz: ")
new_name = '"{}"'.format(new_name)
command = "echo 'SUBSYSTEM=={}, ACTION=={}, ATTR{}=={}, NAME={}' > /etc/udev/rules.d/10-network.rules".format(net, add, address, mac, new_name)
os.system(command)
print("Tu interfaz se ha cambiado correctamente solo haz un reboot y ya estaria")
print("Si te sale permission denied ejecutalo con sudo")
print("Script by yoyo")
