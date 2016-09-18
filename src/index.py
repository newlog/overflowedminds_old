#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shared_imports import web

urls = ('/', 'handlers.main.handler.MainHandler',
        '/papers', 'handlers.content.handler.ContentHandler',
        '/tools', 'handlers.content.handler.ContentHandler',
        '/exploits', 'handlers.content.handler.ContentHandler',
        '/newlog', 'handlers.about_user.handler.AboutUserHandler',
        '/vlan7', 'handlers.about_user.handler.AboutUserHandler',
        '/om', 'handlers.about_om.handler.AboutOMHandler',
        '/search', 'handlers.search.handler.SearchHandler',
        '/(.*)', 'handlers.default.handler.DefaultHandler',
        )


if __name__ == "__main__":
    # web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app = web.application(urls, globals())
    app.run()
