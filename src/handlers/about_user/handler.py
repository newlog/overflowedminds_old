from shared_imports import BaseHandler, web, db


class AboutUserHandler(BaseHandler):
    def GET(self):
        path = web.ctx.path
        if path in ['/newlog', '/vlan7']:
            users_c = db.users
            users_cursor = users_c.find({"username": path[1:]}, {'_id': 0})
            records = [item for item in users_cursor]
            return self.render_template('user.html', items=records[0])
        else:
            return self.render_template('/index.html')
