from shared_imports import BaseHandler


class SearchHandler(BaseHandler):

    def GET(self):
        return self.render_template('/search.html')