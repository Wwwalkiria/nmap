


import nmap
import socket

eq =socket.gethostname()
dir_eq=socket.gethostbyname(eq)
print("""Buenas!, vamos a averiguar su direccion  IP..
        Listo.. su ip es:""", dir_eq)
scan = nmap.PortScanner()
type(dir_eq)
opciones=input("""\n A continuacion, ingrese una opcion: 
                1. Escaneo Simple
                2. Escaneo sistema Operativo \n""")
print("Su seleccion fue:", opciones)

if opciones == "1":
                print("Escaneo Simple:")
                scan.scan(dir_eq,'1-1024', '-v' )
                print(scan.scaninfo())
                print("puertos abiertos:",scan[dir_eq]['tcp'].keys())
elif opciones =='2':
                 print("""\n Escaneo sistema operativo: \n""")
                 host = socket.gethostbyname(eq)
                 r = scan.scan(host, arguments=" -O ")
                 print(scan[host]['osmatch'])



