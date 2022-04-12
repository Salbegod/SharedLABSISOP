import SimpleHTTPServer
import SocketServer
import os.path
import sys

HOST_NAME = '0.0.0.0'
PORT_NUMBER = 8080


class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
 def do_GET(self):
    self.path = '/index.html'
    return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyRequestHandler

datahora = os.popen('date').read()
uptime = os.popen('uptime').read()
#cpu = os.popen('hwinfo --cpu --short').read()
cpu_usage=str(((os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {printusage }' ''').readline()),2))
#name = os.popen('grep '^VERSION' /etc/os-release').read()
#version = os.popen('egrep '^(VERSION|NAME)=' /etc/os-release').read()
mem=str(os.popen('free -t -m').readlines())
T_ind=mem.index('T')
mem_G=mem[T_ind+14:-4]
S1_ind=mem_G.index(' ')
mem_T=mem_G[0:S1_ind]
mem_G1=mem_G[S1_ind+8:]
S2_ind=mem_G1.index(' ')
mem_U=mem_G1[0:S2_ind]
mem_F=mem_G1[S2_ind+8:]






s = open("index.html", "a")

s.write("<html><head><title>INFORMATIONS:</title></head>")
s.write("<p>Data e Hora: %s</p>" % datahora)
s.write("<p>Uptime: %s</p>" % uptime)
#s.write("<p>Modelo do Processador: %s</p>" % cpu)  ###currently not working
s.write("<p>Uso do Processador: %s</p>" % cpu_usage)
s.write("<p>Memoria Total: %s</p>" % mem_T)
s.write("<p>Memoria em Uso: %s</p>" % mem_U)
s.write("<p>Memoria Livre: %s</p>" % mem_F)


s.write("</body></html>")

server = SocketServer.TCPServer(('0.0.0.0', 8080), Handler)
server.serve_forever()


