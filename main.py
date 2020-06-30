from StringIO import StringIO
from flask import Flask, request, send_file, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/media/get/<username>', methods=['GET'])
def get_image(username):
	data = 'x'
	buff = StringIO()
	buff.write(data)
	buff.seek(0)
	return send_file(buff, mimetype="image/jpeg")

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8083, debug=True, threaded=True)
