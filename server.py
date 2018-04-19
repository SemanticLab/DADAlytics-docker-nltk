import falcon
from sklearn.externals import joblib

clf = joblib.load('chunker.pkl')

class Resource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }
        
        resp.media = "Send a post request to this port to parse text. For example curl: curl -H \"Content-Type:text/plain\" --data-binary \"We didn't talk about TonWilliams yesterday. You were talking all the - a lot of drummers, but Tony Williams\'s name didn\'t come up. Do you want to talk about Tony now and why you included him?\" http://localhost:5000"

    def on_post(self, req, resp):

        results = ""

        try:
            text = req.stream.read().decode('utf-8')
            results = clf.parse(text)            
        except Exception as e:
            print(e)
            resp.status = falcon.HTTP_500

        if text is None or str(text).strip() == '':
            resp.status = falcon.HTTP_204


        resp.media = results



api = falcon.API()
api.add_route('/', Resource())