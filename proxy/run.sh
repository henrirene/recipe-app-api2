#!/bin/sh
\n
set -e\n
\n
envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf\n
nginx -g 'daemon off;'\n
\n