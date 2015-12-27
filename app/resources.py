from flask_restful import Resource
import quotes as q

class Picture(Resource):
    def get(self, keyword):
        pass


class Quote(Resource):
    def get(self):
        info = q.random_sentence()
        if info:
            info['length'] = len(info['quote'])
            return info, 200
        else:
            return None, 404
