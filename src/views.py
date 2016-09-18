#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
##import webapp2
import jinja2
# Mine
# from utils import Utils


#class BaseHandler(webapp2.RequestHandler):
class BaseHandler(object):

    template_dir = os.path.join(os.path.dirname(__file__), '../templates/')
    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                                   autoescape=False)

    def render_template(self, template_name, **context):
        return self.jinja_env.get_template(template_name).render(context)
'''
    # Add this function to be used inside a jinja template
    jinja_env.filters['cnv_time_to_str_date'] = Utils.cnv_time_to_str_date

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = self.jinja_env.get_template(template)
        print t
        return t.render(params)

    def render(self, template, **kw):
        #self.write(self.render_str(template, **kw))
        self.render_str(template, **kw)

    def set_standard_headers(self):
        self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
'''
