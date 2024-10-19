from flask import Flask, render_template_string
import subprocess
import getpass
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Harsh Tiwari"
    
    username = getpass.getuser()
    
    ist_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S %Z')
    
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>HTOP Information</title>
    </head>
    <body>
        <h1>HTOP Information</h1>
        <p><strong>Name:</strong> {{ full_name }}</p>
        <p><strong>Username:</strong> {{ username }}</p>
        <p><strong>Server Time (IST):</strong> {{ ist_time }}</p>
        <h2>Top Output:</h2>
        <pre>{{ top_output }}</pre>
    </body>
    </html>
    """
    
    return render_template_string(html_template, full_name=full_name, username=username, ist_time=ist_time, top_output=top_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
