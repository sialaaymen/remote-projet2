from flask import Flask, Responseimport osimport socketimport tim
app = Flask(__name__)hostname = socket.gethostname()urandom = os.open("/dev/urandom", os.O_RDONLY)e
