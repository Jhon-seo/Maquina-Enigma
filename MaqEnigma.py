
abc = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

def cifrar(texto,clave):
  longitud = len(texto);
  for i in range (0,longitud):
    for pos in range (0,53):
      if texto[i] == abc[pos]:
        pos_abc = pos + clave 
        if pos_abc <52:
           print(abc[pos_abc],end='*')
        if pos_abc >52 : 
           print(abc[pos_abc%52],end='*')
    else:
      print(end='')
  return
 

def descifrar(texto,clave):
  longitud = len(texto);
  for i in range (0,longitud):
    for pos in range (0,53):
      if texto[i] == abc[pos]:
        pos_abc = pos-(clave)
        if pos_abc >-1:
           print(abc[pos_abc],end='*')
        if pos_abc <0 :
           print(abc[pos_abc%52],end='*')
    else:
      print(end='')
  return

def iniciar_programa():
	print("hola bienvenido a mi programa\nesta basado en el cifrado Cesar fue construido \npara cifrar y descifrar cadenas de texto.")

	texto = input('ingrese su cadena de texto aqui: ')

	clave = int( input('ingrese su clave aqui: '))

	opcion = int (input('«1.-cifrar—————————————«\n«2.-Descifrar—————————————«\nElija una opción: '))

	if opcion == 1:
		print("Cifrando el texto...")
		cifrar(texto,clave)
	elif opcion == 2:
		print("Descifrando el texto...")
		descifrar(texto,clave)

	repetir_programa()

def repetir_programa():

	repetir = input('\nQuieres continuar usando el programa...?')

	if repetir == 'si':
		iniciar_programa()

	elif repetir == 'no' :
		print('respuesta valida...')
		print('programa terminado.')

	elif repetir != 'si':
		print('respuesta invalida...')
		print('programa terminado.')
	
	else:
		print('programa terminado.')

iniciar_programa()
