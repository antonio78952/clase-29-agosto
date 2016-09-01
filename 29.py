import socket
import os
import sys
import platform
import time
s = socket.socket()
s.bind(("127.0.0.1",2015))
s.listen(5)
sc, addr = s.accept()
while True:
    recibido = sc.recv(1024)
    print recibido.fid("quit")
    recibido = recibido[:-2]
    if (recibido == "quit"):
        print "salir por favor"
        break
    elif (recibido == "time"):
        time.strftime("%H:%M:%S")
    elif (recibido == "ayuda"):
        print "los comandos a introducir son :"
        print "tiempo-->Muestra la hora local servidor"
        print "version--->muestra la version del programa"
        print "os--->Muestra elsistema operativo"
        print"ip -----> muestra la ip actual"
        print"ruta---->ruta actual de trabajo"
        print""
        print""
        print""
        print"quit ----> sale del programa"
    elif (recibido == "version"):
        print (sys.version)
    elif (recibido == "os"):
        platform.system()
    elif (recibido == "ip"):
        socket.gethostbyname_ex(socket.gethostname())
    elif (recibido == "ruta"):
        os.getcwd()
    elif (recibido == "ruta"):
    print "llego:[",recibido,"]"
    sc.send(recibido)
print "adios"
sc.close()
s.close()
