class AFN():

	#Constructor y atributos de un AFN de acuerdo a su definición
	def __init__(self):
		#Alfabeto de entrada representado en una lista
		self.sigma = []
		
		#Conjunto finito no vacío de estados representado en una lista
		self.Q = []

		#Función de transición representado en una matriz
		self.d = []

		#Estado inicial
		self.q0 = -1;

		#Conjunto finito no vacío de estados finales representado en una lista
		self.F = []	

	#Funciones de un AFN

	#Carga un AFN desde un archivo nombre.af
	def cargar_desde(self, nombre):
		#Abre el archivo para lectura
		AFN_archivo = open(nombre, 'r')
		
		#Obtiene el estado inicial partiendo la cadena a partir de que encuentra ':' y al final lo convierte a entero
		self.q0 = int( AFN_archivo.readline().split(':')[1] )
		
		#Obtiene los estados finales partiendo la cadena a partir de que encuentra ':', despues los separa de las comas y al final guarda en la lista
		self.F = ( AFN_archivo.readline().split(':')[1] ).split(',')	
		for i in range( len(self.F) ) :
			self.F[i] = int(self.F[i])

		aux = AFN_archivo.readlines()
		estados = []
		for i in aux:
			#Se quitan los simbolos de salto de linea
			estados.append(i.split('\n')[0])
			simbolo = (i.split(',')[1]).split('\n')[0]
			if( esta_en_alfabeto(self.sigma, simbolo) == False):
				self.sigma.append(simbolo)

		self.Q = estados

		AFN_archivo.close()
		
		return True

	#Guarda el AFN en el archivo nombre.af
	def guardar_en(self, nombre):
		#Abre el archivo para escritura
		AFN_archivo = open(nombre, 'w')

		AFN_archivo.write("inicial:"+str(self.q0)+"\n")
		for i in self.F:
			AFN_archivo.write("final:"+str(i)+"\n")
		
		for i in self.Q:
			AFN_archivo.write(str(i)+"\n")

		return True

	#Agrega una transición al autómata, recibe como parámetros el número del estado inicial y el final, así como el símbolo de la transición
	def agregar_transicion(self, inicio, fin, simbolo):
		self.Q.append(str(inicio)+"->"+str(fin)+","+str(simbolo))
		return True

	#Elimina una transición dentro del AFN, recibe como parámetros el número de estado inicial y final de la transición, así como el símbolo para poder encontrarla
	def eliminar_transicion(self, inicio, fin, simbolo):
		return True

	#Regresa el número del estado inicial del AFN
	def obtener_inicial(self):
		return q0

	#Regresa los números de los estados finales en un vector
	def obtener_finales(self):
		return self.F

	#Establece el estado que recibe como parámetro como el inicial del AFN
	def establecer_inicial(self, estado):
		self.q0 = estado
		return True

	#Establece un estado final del AFN recibido como parámetro
	def establecer_final(self, estado):
		self.F.append(estado)
		return True

	#Verifica si el autómata es un AFN o no
	def esAFN(self):
		return True

	#Verifica si el autómata es un AFD o no
	def esAFD(self):
		return True

	#Verifica si una cadena es válida o no para el autómata
	def acepta(self, cadena):
		return True

	#Genera una cadena aleatoría para el autómata 
	def generar_cadena(self):
		return True

#Funciones auxiliares

def esta_en_alfabeto(alfabeto, simbolo):
	for i in range( len(alfabeto) ):
		if (alfabeto[i] == simbolo):
			return True
	return False
	