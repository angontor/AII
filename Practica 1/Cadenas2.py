#encoding:utf-8

def subcadena(cadena, sub):
    if cadena.count(sub)> 0:
        print sub + ' es una subcadena de ' + cadena
    else:
        print sub + ' no es subcadena de ' + cadena


def ordenAlf(palabra1, palabra2):
    l = [palabra1, palabra2]
    l.sort(cmp=None, key=None, reverse=False)
    print l[0]
  




if __name__=='__main__':
    subcadena('cumpleaños', 'años')   
    
if __name__=='__main__':
    ordenAlf('hola', 'fiesta')                 