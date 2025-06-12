from flask import Flask, request, render_template
from robot_sim import Robot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_code():
    code = request.json['code']
    global_namespace = {'robot': Robot()}
    try:
        exec(code, global_namespace)
    except Exception as e:
        print(f"[ERROR] {e}")
    return {"status": "ok"}
