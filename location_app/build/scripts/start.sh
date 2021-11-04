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

JRE_DIR=jre1.8.0_281

if [ ! -d "../3rd/$JRE_DIR" ]; then
 echo "Location Application has not already installed yet."
 exit 1
fi

echo "Start Location Appliction"

source /etc/profile

# start location service
PID=`ps -ef | grep location-service.jar | grep -v "grep" | awk '{print $2}'`
if [ -n "$PID" ]; then
  echo "location service is already Running."
else
  echo "start location service..."
  cd ../location-service
  nohup ../3rd/$JRE_DIR/bin/java -jar location-service.jar &
fi

# start mep agent
# PID=`ps -ef | grep mep-agent-main | grep -v "grep" | awk '{print $2}'`
# if [ -n "$PID" ]; then
#   echo "mep agent is already Running."
# else
#   echo "start mep agent..."
#   cd ../mep-agent
#   nohup ./mep-agent-main &
# fi

# start backend
PID=`ps -ef | grep runLocationApp.py | grep -v "grep" | awk '{print $2}'`
if [ -n "$PID" ]; then
  echo "backend is already Running."
else
  echo "start backend..."
  cd ../backend
  nohup python3 runLocationApp.py &
fi

# start frontend
PID=`ps -ef | grep website-gateway-locapp-1.0.0.jar | grep -v "grep" | awk '{print $2}'`
if [ -n "$PID" ]; then
  echo "frontend is already Running."
else
  echo "start frontend..."
  cd ../frontend
  nohup ../3rd/$JRE_DIR/bin/java -jar website-gateway-locapp-1.0.0.jar &
fi

echo "Start Location Application Finished"