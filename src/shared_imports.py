import web
from views import BaseHandler
import pymongo


con = pymongo.Connection("mongodb://localhost", safe=True)
db = con.om