from flask import Flask, jsonify, request
application = Flask(__name__)


def html(content):  # Also allows you to set your own <head></head> etc
   return '<html><head></head><body>' + content + '</body></html>'


@application.route('/', methods=['GET'])
def get_tasks():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return html(request.environ['REMOTE_ADDR'])
    else:
        return html(request.environ['HTTP_X_FORWARDED_FOR'])

if __name__ == '__main__':
    application.run(host='0.0.0.0')