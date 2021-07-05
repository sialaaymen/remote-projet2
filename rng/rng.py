from flask import Flask, Responseimport osimport socketimport tim
app = Flask(__name__)hostname = socket.gethostname()urandom = os.open("/dev/urandom", os.O_RDONLY
        @app.route("/")def index():return "RNG running on {}\n".format(hostname))e
@app.route("/<int:how_many_bytes>")def rng(how_many_bytes):time.sleep(0.1)return Response(os.read(urandom, how_many_bytes),content_type="application/octet-stream")
