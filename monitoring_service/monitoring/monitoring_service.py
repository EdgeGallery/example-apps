#
# Copyright 2020 Huawei Technologies Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from flask import Flask, Response
import config
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)

@app.route('/', methods=['GET'])
def hello_world():
    return Response("Hello MEC Developer")

def start_server(handler):
    app.logger.addHandler(handler)
    if config.ssl_enabled:
        context = (config.ssl_certfilepath, config.ssl_keyfilepath)
        app.run(host=config.server_address, debug=True, ssl_context=context, threaded=True, port=config.server_port)
    else:
        app.run(host=config.server_address, debug=True, threaded=True, port=config.server_port)