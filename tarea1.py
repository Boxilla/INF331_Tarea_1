from datetime import datetime

def main():

  log = open("log.txt", 'a')
  ahora = datetime.now()
  dataLog = '{ ' + 'fecha : "{}" , '.format(ahora)

  string1 = ''
  string2 = ''
  resultado = ''

  print('ingrese string 1 :')
  string1 = input()

  print('ingrese string 2 :')
  string2 = input()

  resultado = compareStrings(string1, string2)

  print(resultado)
  dataLog = dataLog + 'stringA : "{}" , stringB : "{}" , resultado : "{}" '.format(string1, string2, resultado) + ' }\n'

  log.write(dataLog)
  log.close()


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
