import re

def AFD():

	#Atributos de un AFD de acuerdo asu definición


	#Carga un AFD desde un archivo nombre.af
	def cargar_desde(nombre):

	#Guarda el AFD en el archivo nombre.af
	def guardar_en(nombre):

	#Agrega una transición al autómata, recibe como parámetros el número del estado inicial y el final, así como el símbolo de la transición
	def agregar_transicion(inicio, fin, simbolo):

	#Elimina una transición dentro del AFD, recibe como parámetros el número de estado inicial y final de la transición, así como el símbolo para poder encontrarla
	def eliminar_transicion(inicio, fin, simbolo):

	#Regresa el número del estado inicial del AFD
	def obtener_inicial():

	#Regresa los números de los estados finales en un vector
	def obtener_finales():

	#Establece el estado que recibe como parámetro como el inicial del AFD
	def establecer_inicial(estado):

	#Establece un estado final del AFN recibido como parámetro
	def establecer_final(estado):

	#Verifica si el autómata es un AFN o no
	def esAFN():

	#Verifica si el autómata es un AFD o no
	def esAFD():

	#Verifica si una cadena es válida o no para el autómata
	def acepta(cadena):

	#Genera una cadena aleatoría para el autómata 
	def generar_cadena():

