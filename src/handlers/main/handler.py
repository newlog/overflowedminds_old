from shared_imports import BaseHandler, db
import random


class MainHandler(BaseHandler):

    def GET(self):
        quotes_c = db.quotes
        quotes = quotes_c.find()
        if quotes:
            n = quotes.count()
            if n > 0:
                item = quotes[random.randint(0, n-1)]
                if item.get('quote') and item.get('author'):
                    return self.render_template('/index.html', author=item['author'], quote=item['quote'])
        return self.render_template('/index.html')