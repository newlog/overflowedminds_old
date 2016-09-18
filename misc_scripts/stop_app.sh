#!/bin/sh

process_num=$(ps ax -o pid,args | grep -m 1 "python /usr/share/nginx/www/new_om/src/index.py" | awk '{print $1}')
kill $process_num
