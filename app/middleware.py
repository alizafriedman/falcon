import json

class jsonTranslator(object):
    def process_request(self, req, res):
        if req.content_length in (None, 0):
            return
    
            body = req.stream.read()

            if not body:
                raise falcon.HTTPBadRequest('empty request json body', 'a valid json is required')

            try:
                req.context['doc'] = json.loads(body.decode('utf-8'))

            
            except(ValueError, UnicodeDecodeError):
                raise falcon.HTTPError(falcon.HTTP_753, 'malformed json', 'cannot decode the req body')


    def process_response(self, req, res):
        if 'result' not in resp.context:
            return

        resp.body = json.dumps(resp.context['result'])