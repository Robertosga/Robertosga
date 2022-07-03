import urllib.request
pagina=('https://www.infoescola.com/cristianismo/cinco-solas/')

while True:
    
    nno='admin'
    senha='12345'
    
    nn=input('login: ')
    ss=input('senha: ')
    
    if (nn==nno)and(ss==senha):
        print('Seja Bem Vindo!',nn,'\n'
       'liberado o acesso', pagina)
        break

    elif (nn!=nno)and(ss==senha):
        print ('login nao cadastrado,'
'procure o administrador')

    elif (nn==nno)and(ss!=senha):
        print ('senha incorreta,'
'procure o administrador ')

    else:
        print ('sai fora intruso')
    
quit()
