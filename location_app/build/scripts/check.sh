#!/bin/bash
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

echo "Check Location Appliction Status"

#PID=`ps -ef | grep mep-agent-main | grep -v "grep" | awk '{print $2}'`
#echo "mepagent: $PID"
#if [ -n "$PID" ]; then
#  echo "mep agent is Running."
#else
#  echo "mep agent is not Running."
#fi

PID=`ps -ef | grep website-gateway-locapp-1.0.0.jar | grep -v "grep" | awk '{print $2}'`
echo "frontend: $PID"
if [ -n "$PID" ]; then
  echo "frontend is Running."
else
  echo "frontend is not Running."
fi

PID=`ps -ef | grep runLocationApp.py | grep -v "grep" | awk '{print $2}'`
echo "backend: $PID"
if [ -n "$PID" ]; then
  echo "backend is Running."
else
  echo "backend is not Running."
fi

PID=`ps -ef | grep location-service.jar | grep -v "grep" | awk '{print $2}'`
echo "locationService: $PID"
if [ -n "$PID" ]; then
  echo "locationService is Running."
else
  echo "locationService is not Running."
fi
