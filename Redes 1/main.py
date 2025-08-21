import asyncio, socket, os, re, http.server
from datetime import datetime


#Primero tomar el mensaje para enviarlo a un servidor TCP con cliente TCP

#Este servidor 1 tiene un cliente TCP que debe usar UDP para pasarlo a un Cliente UDP

#Se envia a un servidor UDP

#Enviar mediante HTTP a servidor HTTP con cliente TCP


largo_final = input()

mensaje = str("Hola")


current_dt = datetime.now()

print(f"Timestamp (float): {current_dt}")
final = str(f"[{current_dt}]-[{largo_final}]-[{len(mensaje)}]-[{mensaje}]")

print(final)

#Hay que implementar la logica de ver el largo en el http 