buntu@ip-172-26-6-96:~/tracking_pixel$ 
ubuntu@ip-172-26-6-96:~/tracking_pixel$ cat main.py 
from StringIO import StringIO
from flask import Flask, request, send_file, redirect, render_template
import base64
import io
from datetime import datetime

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/tp/<username>', methods=['GET'])
def get_image(username):
    f = file('log.txt', 'at')
    f.write(datetime.now().isoformat())
    f.write(' ')
    f.write(username)
    f.write('\n')
    f.close()
    print 'wrote %s to log.txt' % username

    gif = 'R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=='
    gif_str = base64.b64decode(gif)
    return send_file(io.BytesIO(gif_str), mimetype='image/gif')

if __name__ == "__main__":
    cer = '/var/discourse/shared/standalone/letsencrypt/forum.506investorgroup.com/forum.506investorgroup.com.cer'
    key = '/var/discourse/shared/standalone/letsencrypt/forum.506investorgroup.com/forum.506investorgroup.com.key'
    context = (cer, key)
    app.run(host="0.0.0.0", port=8083, debug=True, threaded=False, ssl_context=context)
