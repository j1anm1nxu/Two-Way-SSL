import os
from quart import Quart, request, session

BASE_DIR = BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Quart(__name__)


@app.route('/')
async def root():
    return 'Hello, World\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8888',
            keyfile=f'{BASE_DIR}/certs/server.key',
            certfile=f'{BASE_DIR}/certs/server.crt',
            )
