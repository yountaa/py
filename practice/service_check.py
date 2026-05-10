import socket
import argparse

parser = argparse.ArgumentParser(description='service_checker [--host , --port]')
parser.add_argument("--host",default="localhost", help="Hostname для проврки")
parser.add_argument("--port",type=int,default=22, help="Порт для проверки")
args = parser.parse_args()

host = args.host
port = args.port

sock = socket.socket()
sock.settimeout(3)
result = sock.connect_ex((host, port))

if result == 0:
  print(f"{host}:{port} - Порт открыт")
else:
  print(f"{host}:{port} - Порт закрыт")
