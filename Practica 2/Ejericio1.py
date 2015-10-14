#encoding:utf-8
import urllib, urllib2 



def escritura():    
    
    try:
        f = urllib2.urlopen('http://www.us.es/rss/feed/portada')
           
    except urllib2.HTTPError, e:
        
        print 'Ocurrió un error'
        print e.code
    
    except urllib2.URLError, e:
        
        print 'Ocurrió un error'
        print e.reason
    
    outdata = open('pratica2.txt', 'a')
    
    outdata.write(f.read())
    
    outdata.close()


def lectura():
    
    
    outdata = open('pratica2.txt', 'r')
    lineas = outdata.readlines()
    
    title ='<title>'
    link ='<link>'
    date ='<pubDate>'
    
    
    for i in lineas:
        if title in i:
            i.replace('<title>', 'Título: ')
#             i.replace('</title>', '')
            print i
#         elif link in i:
#             i.replace('<link>', 'Link: ')                
#             i.replace('</link>', '')
#             print i
#         elif date in i:
#             i.replace('<pubDate>', 'Fecha: ')
#             i.replace('</pubDate>', '')
#             print i
                
            
            

    outdata.close()        

if __name__=='__main__':
    escritura()
    lectura()
    
    