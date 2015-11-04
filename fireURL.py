"""
GPL License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from socket import gethostname, gethostbyname
from subprocess import call
from urlparse import urljoin
import cgi, platform

LISTENPORT=8000

class GetHandler(BaseHTTPRequestHandler):
    def fireURL(self, url):
        url = urljoin('http://', url[0])

        system = platform.system()
        commands = []
        if system == 'Darwin':
            commands += ['open']
        elif system == 'Windows':
            commands += ['cmd', '/c', 'start']
        else:
            commands += ['xdg-open']
        return call(commands + [url]) == 0


    def do_POST(self):
        print 'Processing request: %s' % self.path

        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        if ctype == 'multipart/form-data':
            postvars = cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers.getheader('content-length'))
            postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            postvars = {}

        response_code = 500

        if "url" not in postvars:
            response_code = 400
        else:
            response_code = 200 if self.fireURL(postvars['url']) else 500

        self.send_response(response_code)
        self.end_headers()

def log_info(msg):
    print '\033[94m\033[1m' + "INFO: " + '\033[0m\033[94m' + msg + '\033[0m'

def print_info():
    print '\033[1m' + '   )\n  ) \\\n / ) (\n \(_)/' + '\033[0m'
    print '\033[95m\033[1m' + 'FireURL v.0.1 (c) PrankyMat 2015' + '\033[0m'
    log_info('FireURL is listening on '+str(ip)+':'+str(LISTENPORT)+'. POST a url to fire it!')


if __name__ == '__main__':
    ip = gethostbyname(gethostname())

    print_info()

    server = HTTPServer(('0.0.0.0', LISTENPORT), GetHandler)
    server.serve_forever()
