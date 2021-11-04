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
    Starting the location application server
"""
import logging
from logging.handlers import RotatingFileHandler

from location.location import start_server

if __name__ == '__main__':
    handler = RotatingFileHandler('/usr/app/log/location_application_server.log',
                                  maxBytes=10000000, backupCount=10)
    handler.setLevel(logging.INFO)
    start_server(handler)
