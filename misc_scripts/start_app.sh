#!/bin/sh

su www-data -c 'spawn-fcgi -d /usr/share/nginx/www/new_om -f /usr/share/nginx/www/new_om/src/index.py -a 127.0.0.1 -p 9002'
