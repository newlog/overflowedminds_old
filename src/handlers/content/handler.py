from shared_imports import BaseHandler, web, db


class ContentHandler(BaseHandler):

    def GET(self):
        path = web.ctx.path
        if path in ['/papers', '/tools', '/exploits']:
            users_c = db.users
            users = users_c.find({}, {'_id': 0, 'username': 1})
            items_c = db[path[1:]]
            d = {}
            for user in users:
                items_cursor = items_c.find({'username': user['username']})
                items_list = []
                for i in items_cursor:
                    items_list.append(i)
                if items_list:
                    d[user['username']] = items_list
            return self.render_template('content.html', items=d)
        else:
            return self.render_template('/index.html')
