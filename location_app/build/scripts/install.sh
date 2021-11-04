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

JRE_DIR=jre1.8.0_281

if [ -d "../3rd/$JRE_DIR" ]; then
  echo "Location Application has already installed."
  exit 1
fi

echo "Install Location Appliction"

function installTools() {
  echo "install python3"
  PYTHON3_RESULT=`python3 --version`
  if [ -z $PYTHON3_RESULT ]; then
    apt update
    apt install python3 -y
  else
    echo "python3 is already installed, no need to install aggain."
  fi
  
  echo "install python3-pip"
  PIP3_RESULT=`pip3 --version`
  if [ -z $PIP3_RESULT ]; then
    apt update
    apt install python3-pip -y
  else
    echo "python3-pip is already installed, no need to install aggain."
  fi

  echo "install zip"
  ZIP_RESULT=`zip --version`
  if [ -z $ZIP_RESULT ]; then
    apt update
    apt install zip -y
  else
    echo "zip is already installed, no need to install aggain."
  fi
}

function installLocationApp() {
#  echo "install mep-agent"
#  cd ../mep-agent
#  unzip mep-agent.zip
#  mv main mep-agent-main
#  rm mep-agent.zip

  echo "install backend"
  cd ../backend
  pip3 install -r requirements.txt
		        
  echo "install frontend"
  cd ../3rd
  tar -zxvf jre.tar.gz 

  cd ../scripts
}

function configFilePermission() {
  echo "config file permission"
}

function configEnv() {
  sed -i '/MEP_IP=/d' /etc/profile
  sed -i '/MEP_APIGW_PORT=/d' /etc/profile
  sed -i '/AK=/d' /etc/profile
  sed -i '/SK=/d' /etc/profile
  sed -i '/APPINSTID=/d' /etc/profile
  sed -i '/CA_CERT_DOMAIN_NAME=/d' /etc/profile

  cat env.properties | while read line
  do
    echo "export $line" >> /etc/profile
  done
  source /etc/profile
}

function configOther() {
  mkdir -p /usr/app/log
}

function main() {
  echo "install tools"
  installTools
			     
  echo "install location application"
  installLocationApp

  echo "config file permission"
  configFilePermission

  echo "config env"
  configEnv

  echo "config other"
  configOther
}

main

echo "Install OK"