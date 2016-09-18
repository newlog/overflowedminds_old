from shared_imports import BaseHandler


class AboutOMHandler(BaseHandler):

    def GET(self):
        return self.render_template('/om.html')