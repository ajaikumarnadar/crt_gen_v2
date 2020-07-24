import os

pwd  = os.getcwd();

for i in next(os.walk('.'))[1]:
    fpath = pwd+'\\'+i+'\\Certificate'

    os.chdir(fpath)

    crt = open('crt_file.crt','a');

    server = open('server.txt', 'r');
    root = open('root.txt', 'r');
    intermediate = open('intermediate.txt', 'r')

    crt.write(server.read())
    crt.write(intermediate.read())
    crt.write(root.read())
    
    crt.close()
    server.close()
    root.close()
    intermediate.close()