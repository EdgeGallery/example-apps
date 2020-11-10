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

# Validates if ip is valid
validate_ip()
{
 ip_var="$1"
    # checks if variable is unset
 if [ -z "$ip_var" ] ; then
    echo "ip is not set"
    return 1
 fi

 if ! echo "$ip_var" | grep -qE '^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.)' ; then
   return 1
 fi
 return 0
}

validate_name() {
  hostname="$1"
  len="${#hostname}"
  if [ "${len}" -gt "64" ]; then
    return 1
  fi
  if ! echo "$hostname" | grep -qE '^[a-zA-Z0-9]*$|^[a-zA-Z0-9][a-zA-Z0-9_\-]*[a-zA-Z0-9]$'; then
    return 1
  fi
  return 0
}

# validates whether file exist
validate_file_exists() {
  file_path="$1"

  # checks variable is unset
  if [ -z "$file_path" ]; then
    echo "file path variable is not set"
    return 1
  fi

  # checks if file exists
  if [ ! -f "$file_path" ]; then
    echo "file does not exist"
    return 1
  fi

  return 0
}

validate_ip "$LISTEN_IP"
valid_listen_ip="$?"
if [ ! "$valid_listen_ip" -eq "0" ]; then
  echo "invalid ip address for listen ip"
  exit 1
fi

if [ ! -z "$SERVER_NAME" ]; then
  validate_name "$SERVER_NAME"
  valid_name="$?"
  if [ ! "$valid_name" -eq "0" ]; then
    echo "invalid ssl server name"
    exit 1
  fi
fi

# ssl parameters validation
validate_file_exists "/usr/app/ssl/server_tls.crt"
valid_ssl_server_cert="$?"
if [ ! "$valid_ssl_server_cert" -eq "0" ]; then
  echo "invalid ssl server certificate"
  exit 1
fi

# ssl parameters validation
validate_file_exists "/usr/app/ssl/server_tls.key"
valid_ssl_server_key="$?"
if [ ! "$valid_ssl_server_key" -eq "0" ]; then
  echo "invalid ssl server key"
  exit 1
fi

# ssl parameters validation
validate_file_exists "/usr/app/ssl/ca.crt"
valid_ssl_ca_crt="$?"
if [ ! "$valid_ssl_ca_crt" -eq "0" ]; then
  echo "invalid ssl ca cert"
  exit 1
fi

echo "Running Monitoring Service"
umask 0027
cd /usr/app || exit
python run.py