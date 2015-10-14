#encoding:utf-8

def votos(tupla):
    for elem in tupla:
        print elem + ', vote por mi.'
    
    
    
tupla = ('Antonio','Manolo','Pepe')    
if __name__=='__main__':
    votos(tupla)  