import sys, os

fin = open (sys.argv[1])
fout = open (sys.argv[2],"w")
for x in fin.readlines():
    tokens = x.split(';')
    fout.write(tokens[0] + '.0\t' + ";".join(map(str,tokens[1:])))

fout.close()
