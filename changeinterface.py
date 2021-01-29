#/usr/bin/python3
import os, sys, subprocess
# Ejecutar con sudo python3 changeinterface.py
if os.getuid() != 0:
  print("Ejecutalo con sudo")
  sys.exit(1)
else:
    address = "{address}"
    net = '"net"'
    add = '"add"'
    cambiar_mac = None
    output = ""
    a = 0
    mac = ""
    interfaz = ""
    lista_macs = []
    lista_ifaces= []
    iface = subprocess.check_output("ip a | grep ': ' | cut -d ':' -f 2", shell=True)
    iface = str(iface)
    iface = iface.replace("b'", "").replace("n", "").replace("'", "").replace("\\", "").replace(" l", "l")
    iface = iface + " "
    macs = subprocess.check_output("ip a | grep link/ | cut -d ' ' -f 6", shell=True)
    macs = str(macs)
    macs = macs.replace("b", "").replace("n", "").replace("\\", " ").replace("'", "")
    for i in macs:
            mac = mac + i
            if i == " ":
                    lista_macs.append(mac)
                    mac = " "
    for i in iface:
            interfaz = interfaz + i
            if i == " ":
                    lista_ifaces.append(interfaz)
                    interfaz = " "
    for i in range(0, len(lista_macs)):
            output = output + "Interfaz ({}): {}     MAC: {}\n".format(a, lista_ifaces[a], lista_macs[a])
            a += 1
    print(output.replace("  ", " "))
    numero_interfaz = int(input("Introduce el numero de interfaz a la que quieres cambiar el nombre: "))
    for i in range (0, numero_interfaz+1):
            cambiar_mac = lista_macs[i].replace(" ", "")
    cambiar_mac = '"{}"'.format(cambiar_mac)
    new_name = input("Introduce el nuevo nombre para la interfaz: ")
    new_name = '"{}"'.format(new_name)
    command = "echo 'SUBSYSTEM=={}, ACTION=={}, ATTR{}=={}, NAME={}' > /etc/udev/rules.d/10-network.rules".format(net, add, address, cambiar_mac, new_name)
    os.system(command)
    print("Tu interfaz se ha cambiado correctamente solo haz un reboot y ya estaria")
    print("Script by yoyo")
