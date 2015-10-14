#encoding:utf-8

def separar(cadena, caracter):
    l = list(cadena)
    s = caracter.join(l) 
    print s
      
def reemplazar(cadena, caracter):
    res = cadena.replace(' ',caracter)
    print res    

def reemplazaDigitos(cadena):
    res=''
    for e in cadena:
        if e.isdigit():
            e='X'
            res+=e
        else: res+=e 
    print res    
      
      
      
        
     
if __name__=='__main__':
    separar('separar', ',')  
    
if __name__=='__main__':
    reemplazar('reemplazar por guiones', '_') 
    
if __name__=='__main__':
    reemplazaDigitos('su clave es: 1540')               