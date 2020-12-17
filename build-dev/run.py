import logging 
import http.server
import socketserver
import getpass

class MyHTTPHandler(http.server.simpleHTTPRequestHandler):
    def log_message(self, format, *args):
        logging.info("%s - -[%s] %s/n"(
            self.client_address[0],
            self.log
        ))

logging.basicConfig(
    filename='/log/http-server.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logging.getLogger().addHandler(logging.StreamHandler())
logging.info('inicializando...')
PORT = 800

http = socketserver.TCPServer(("", PORT), MyHTTPHandler)
logging.info('Escutando a porta : %s', PORT)
logging.info('usuario: %s', getpass.getuser())
http.server_forever()
