class MyOutputStream(object):

    def write(self, data):
        with open('/tmp/webpy.log', 'a') as fd:
                fd.write(data)

import sys
sys.stdout = MyOutputStream()
