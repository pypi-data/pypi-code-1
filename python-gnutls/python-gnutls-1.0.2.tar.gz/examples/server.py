#!/usr/bin/python

"""Synchronous server using python-gnutls"""

import sys
import os
import socket

from gnutls.crypto import *
from gnutls.connection import *

script_path = os.path.realpath(os.path.dirname(sys.argv[0]))
certs_path = os.path.join(script_path, 'certs')

cert = X509Certificate(open(certs_path + '/valid.crt').read())
key = X509PrivateKey(open(certs_path + '/valid.key').read())
ca = X509Certificate(open(certs_path + '/ca.pem').read())
crl = X509CRL(open(certs_path + '/crl.pem').read())
cred = X509Credentials(cert, key, [ca], [crl])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ssf = ServerSessionFactory(sock, cred)
ssf.bind(('0.0.0.0', 10000))
ssf.listen(100)

while True:
    session, address = ssf.accept()
    try:
        session.handshake()
        peer_cert = session.peer_certificate
        try:
            peer_name = peer_cert.subject
        except AttributeError:
            peer_name = 'Unknown'
        print '\nNew connection from:', peer_name
        print 'Protocol:     ', session.protocol
        print 'KX algorithm: ', session.kx_algorithm
        print 'Cipher:       ', session.cipher
        print 'MAC algorithm:', session.mac_algorithm
        print 'Compression:  ', session.compression
        session.verify_peer()
        cred.check_certificate(peer_cert)
    except Exception, e:
        print 'Handshake failed:', e
        session.bye()
    else:
        while True:
            try:
                buf = session.recv(1024)
                if buf == 0 or buf == '':
                    print "Peer has closed the session"
                    break
                else:
                    if buf.strip().lower() == 'quit':
                        print "Got quit command, closing connection"
                        session.bye()
                        break
                session.send(buf)
            except Exception, e:
                print "Error in reception: ", e
                break
    session.shutdown()
    session.close()
