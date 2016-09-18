from shared_imports import BaseHandler


class DefaultHandler(BaseHandler):

    def GET(self, url):
        return self.render_template('index.html')
