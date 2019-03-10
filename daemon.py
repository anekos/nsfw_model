
from nsfw_detector import NSFWDetector
detector = NSFWDetector('./nsfw.299x299.h5')

import json
import numpy
from bottle import route, run, template
from bottle import get, post, request


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.integer):
            return int(obj)
        elif isinstance(obj, numpy.floating):
            return float(obj)
        elif isinstance(obj, numpy.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)

@route('/detect')
def index():
    path = request.params.path
    result = detector.predict(path).get(path)
    return template(json.dumps(result, cls=MyEncoder))

print('started')
run(host='localhost', port=8181)
