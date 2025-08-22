from socket import *
from datetime import datetime

from Clientes.clienteTCP import ClienteTCP
from Clientes.clienteUDP import ClienteUDP
from Clientes.clienteHTTP import ClienteHTTP
from Servidores.servidorTCP import ServidorTCP
from Servidores.servidorUDP import ServidorUDP

#Servidores

servidor = []
cliente = []

servidor.append(ServidorTCP('127.0.0.1', 65431, "Servicio 1"))
servidor.append(ServidorTCP('127.0.0.2', 65432, "Servicio 2"))
servidor.append(ServidorUDP('127.0.0.3', 65433, "Servicio 3"))

''' 
# Incluir cuando servidor y cliente HTTP esten implementados

servidor.append(ServidorHTTP('127.0.0.4', 65433, "Servicio 4")) 

cliente.append(ClienteTCP("Servicio 1"))
cliente.append(ClienteUDP("Servicio 2"))
cliente.append(ClienteHTTP("Servicio 3"))
cliente.append(ClienteTCP("Servicio 4"))
'''
           
cliente.append(ClienteTCP("Servicio 1"))
cliente.append(ClienteUDP("Servicio 2"))
cliente.append(ClienteTCP("Servicio 3"))

largo_final = input("Ingresa el largo mínimo del mensaje final: ")
mensaje = input("Mensaje inicial: ")
current_dt = datetime.now()

# [Timestamp]-[LargoMinimo]-[LargoActual]-[Mensaje]
final = str(f"[{current_dt}]-[{largo_final}]-[{len(mensaje)}]-[{mensaje}]")

#Servicio 1 edita el mensaje
cliente[0].actualizar_mensaje(mensaje, largo_final)    

#Enviar mensaje del servicio 1 al servicio 2 por TCP
cliente[0].enviar_por_TCP(servidor[1].host,servidor[1].port)

'''---------------------------------------------------------------'''

#Mensaje recibido y enviar al cliente 2 TCP
servidor[1].recibir_mensaje_cliente()
cliente[1].recibir_por_TCP()
servidor[1].enviar_mensaje_cliente()

#Servicio 2 edita el mensaje
cliente[1].actualizar_mensaje(mensaje, largo_final)    

#Enviar mensaje del servicio 2 al servicio 3 por UDP
cliente[1].enviar_por_UDP(servidor[2].host,servidor[2].port)

'''---------------------------------------------------------------'''

#Mientras el servidor y cliente HTTP no este implementado

#Mensaje recibido y enviar al cliente 3 TCP
servidor[2].recibir_mensaje_cliente()
cliente[2].recibir_por_UDP()
servidor[2].enviar_mensaje_cliente()

#Servicio 3 edita el mensaje
cliente[2].actualizar_mensaje(mensaje, largo_final)    

#Enviar mensaje del servicio 3 al servicio 1 por TCP
cliente[2].enviar_por_TCP(servidor[0].host,servidor[0].port)
