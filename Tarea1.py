from datetime import datetime

def main():

  log = open("log_prueba_tarea1_inf331.txt", 'a')
  ahora = datetime.now()
  dataLog = '{ ' + 'fecha : "{}" , '.format(ahora)

  string1 = ''
  string2 = ''
  resultado = ''

  while (len(string1) == 0):
    print('ingrese string 1 :')
    string1 = input()
  
  while (len(string2) == 0):
    print('ingrese string 2 :')
    string2 = input()


  resultado = compareStrings(string1, string2)

  print(resultado)
  
  
  string1 = string1.encode('utf-8')
  string2 = string2.encode('utf-8')

  dataLog = dataLog + 'stringA : "{}" , stringB : "{}" , resultado : "{}" '.format(string1, string2, resultado) + ' }\n'

  log.write(dataLog)
  log.close()

  print('Para finalizar el programa presione la tecla Enter')
  input()


def compareStrings(StringA, StringB):

  largoStringA = len(StringA)
  largoStringB = len(StringB)

  if(largoStringA < largoStringB):
    return 'String 2 es el más largo'
  elif (largoStringA == largoStringB):
    return 'Los Strings tienen el mismo largo'
  else:
    return 'String 1 es el más largo'

main()