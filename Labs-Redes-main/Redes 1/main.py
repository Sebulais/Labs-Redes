from socket import *
from datetime import datetime
import re

from ClienteTCP import ClienteTCP
from ClienteUDP import ClienteUDP
from ClienteHTTP import ClienteHTTP

#Servidores

servidor = []
cliente = []

# Incluir cuando servidor y cliente HTTP esten implementados

cliente.append(ClienteTCP("Servicio 1"))
cliente.append(ClienteUDP("Servicio 2"))
cliente.append(ClienteHTTP("Servicio 3"))
cliente.append(ClienteTCP("Servicio 4")) 

largo_final = input("Ingresa el largo mínimo del mensaje final: ")
while not largo_final.isdigit() or (largo_final.isdigit() and int(largo_final) <= 0):
    largo_final = input("Largo mínimo debe ser un entero positivo: ")

mensaje = input("Mensaje inicial: ")
while not re.match(r'^[a-zA-Z]+$', mensaje):
    mensaje = input("El mensaje solo puede tener letras mayúsculas o minúsculas: ")

current_dt = datetime.now()

# [Timestamp]-[LargoMinimo]-[LargoActual]-[Mensaje]
final = str(f"[{current_dt}]-[{largo_final}]-[{len(mensaje)}]-[{mensaje}]")

#Servicio 1 edita el mensaje
i = 0
while True:
    if i == 0:
        cliente[0].ingresar_mensaje(mensaje, largo_final)
    else:
        cliente[0].actualizar_mensaje(largo_final)
    #Enviar mensaje del servicio 1 al servicio 2 por TCP
    cliente[0].enviar_por_TCP("127.0.0.1", 65433)

    '''---------------------------------------------------------------'''

    #Mensaje recibido y cliente 2 recibe mensaje del servidor 2 por TCP
    cliente[1].recibir_por_TCP("127.0.0.1", 65433)

    #Servicio 2 edita el mensaje
    cliente[1].actualizar_mensaje(largo_final)    

    #Enviar mensaje del servicio 2 al servicio 3 por UDP
    cliente[1].enviar_por_UDP("127.0.0.1", 65432)

    '''---------------------------------------------------------------'''


    #Mensaje recibido y cliente 3 recibe mensaje del servidor 2 por UDP

    cliente[2].recibir_por_UDP("127.0.0.1",65432)

    #Servicio 3 edita el mensaje
    cliente[2].actualizar_mensaje(largo_final)

    #Enviar mensaje del servicio 3 al servicio 4 por HTTP
    cliente[2].enviar_por_HTTP("127.0.0.1", 8000)
    
    
    #servidor 4
    #     continuar el loop
    #     mensaje = Close
    #     terminar 
    
    '''---------------------------------------------------------------'''

    #Mensaje recibido y cliente 4 recibe mensaje del servidor 3 por HTTP
    cliente[3].recibir_por_HTTP("127.0.0.1", 5000)

    #Servicio 4 edita el mensaje
    if (cliente[3].get_mensaje() == "Close"):
            cliente[3].enviar_por_TCP("127.0.0.1", 65432)
            cliente[0].recibir_por_TCP("127.0.0.1", 65432)
            cliente[0].enviar_por_TCP("127.0.0.1", 65433)
            cliente[1].recibir_por_TCP("127.0.0.1", 65433)
            cliente[1].enviar_por_UDP("127.0.0.1", 65432)
            cliente[2].recibir_por_UDP("127.0.0.1",65432)
            cliente[2].enviar_por_HTTP("127.0.0.1", 8000)
            print("Cierre total")
            break   

    #Enviar mensaje del servicio 4 al servicio 1 por TCP
    else:
        cliente[3].actualizar_mensaje(largo_final)
        cliente[3].enviar_por_TCP("127.0.0.1", 65432)
        i += 1