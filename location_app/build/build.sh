#!/bin/bash
# Copyright 2021 Huawei Technologies Co., Ltd.
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

echo "Build Location Appliction Package"

HELPER_DIR=location-app

mkdir $HELPER_DIR
mkdir $HELPER_DIR/frontend
mkdir $HELPER_DIR/location-service

cp -r ../backend $HELPER_DIR
cp -r ../frontend/website-gateway-locapp-1.0.0.jar $HELPER_DIR/frontend
cp -r ../location-service/location-service.jar $HELPER_DIR/location-service
# cp -r ../mep-agent $HELPER_DIR
cp -r ../3rd $HELPER_DIR
cp -r scripts $HELPER_DIR

tar -cvf location-app-1.0.tar $HELPER_DIR

rm -rf $HELPER_DIR

echo "Build Location Appliction Package Succeed"