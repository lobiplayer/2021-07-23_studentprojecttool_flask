import os

app = Flask('GARDONE', root_path=web_dir)

web_dir = os.path.join(os.path.dirname(
    os.path.abspath(file)), 'api')