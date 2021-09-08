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

"""
    Defined monitoring service configuration.
"""
import os

# [Server Configurations]
SERVER_PORT = 9997
SERVER_ADDRESS = os.environ.get('LISTEN_IP', "127.0.0.1")
MONITORING_SERVICE_BE_PORT = 32120

# [SSL Configurations]
SSL_ENABLED = False
SSL_PROTOCOL = "TLSv1.2"
SSL_CIPHERS = ["TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256", "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
          "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384"]
SSL_CERTFILEPATH = "/usr/app/ssl/server_tls.crt"
SSL_KEYFILEPATH = "/usr/app/ssl/server_tls.key"
SSL_CACERTPATH = "/home/root1/mec-deploy/certs/ca.crt"
SSL_SERVER_NAME = os.environ.get('SERVER_NAME', "edgegallery")

# [Service Configurations]
API_GATEWAY = os.environ.get("API_GATEWAY", "face-recognition:9999")
FACE_RECOGNITION = os.environ.get("FACE_RECOGNITION", "facerecognition")
MEP_AGENT = os.environ.get("MEP_AGENT", "edgegallery.org")
FE_SERVICE = os.environ.get("FE_SERVICE", "monitoring-proxy-service:5000")
APP_INST_ID = os.environ.get("APPINSTID", "5abe4782-2c70-4e47-9a4e-0ee3a1a0fd1f")
MEP_IP = os.environ.get("MEP_IP", "mep-mm5.mep")
MEP_PORT = os.environ.get("MEP_PORT", "80")
