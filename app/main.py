import falcon
import json


class IndexResource(object):
    def on_get(self, req, res):
        res.status = falcon.HTTP_200
        res.body = json.dumps({'success': 'my first falcon app'})





application = falcon.API()
application.add_route('/', IndexResource())

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)