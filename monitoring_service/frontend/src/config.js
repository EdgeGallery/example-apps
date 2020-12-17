/*
 *  Copyright 2020 Huawei Technologies Co., Ltd.
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */

var host = window.location.hostname
var port = window.location.port
var port1 = port - 1
var port2 = port + 1
export default {

  baseUrl: 'http://' + host + ':' + port1 + '/v1/monitor/',

  baseUrl_NodeProxy: 'http://' + host + ':' + port2 + '/'
}
