#!/bin/bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
mv cert.pem public.pem
mv key.pem private.key
