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

const http = require('http');
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const fs = require('fs');
const extract = require('extract-zip');
const app = express();
var multer  = require('multer')
const axios = require('axios');
app.use(cors());
const path = require('path');
const helpers = require('./helpers');
const socket = require("socket.io");

const port = 5000;

app.use('/static', express.static(path.join(__dirname, './public')));
app.use(bodyParser.json());

app.get('/', function(req, res) {
  res.send('connected to server successfully');
})

app.get('/persons', function(req, res)  {
  let host = req.hostname
  deleteFiles();
  axios.get('http://'+host+':32115/v1/monitor/persons')
  .then(function (response) {
    if(res.statusCode == 200) {
      fs.readdir('./public', (err, files) => {
        personData = [];
        files.map( (file, index) => {
          console.log(file);
          let per = {
            id: index,
            name: file,
            file: `http://${host}:32117/static/${file}`
          }
          personData.push(per);
        });
        res.send(JSON.stringify(personData));
      });
   }
  })
  .catch(function (error) {
    console.log(error.message);
  })
  .then(function () {
  });  
})

app.post('/notify', (req, res) => {
  io.sockets.emit('notify', req.body);
  res.send("Notify Successfully.");
})
 
app.post('/uploadFile', (req, res) => {
  let upload = multer({ storage: storage, fileFilter: helpers.imageFilter }).array('file',10)
  upload(req, res, function(err) {
    if (req.fileValidationError) {
        return res.send(req.fileValidationError);
    }
    else if (!req.files) {
        return res.send('Please select an image to upload');
    }
    else if (err instanceof multer.MulterError) {
        return res.send(err);
    }
    else if (err) {
        return res.send(err);
    }
    res.send(`upload successfully.`);
  });
});

const storage = multer.diskStorage({
  destination: function(req, file, cb) {
      cb(null, './public');
  },

  filename: function(req, file, cb) {
    cb(null, file.originalname.replace(file.originalname.match(/\.(jpg|JPG|jpeg|JPEG|png|PNG|gif|GIF)$/)[0],"") + path.extname(file.originalname));
  }
})

async function deleteFiles () {
  fs.readdir('./public', (err, files) => {
    personData = [];
    files.map( (file, index) => {
      fs.unlink('./public/'+file, function(err) {
        if(err) console.log(err.message);
      });
    });
  });
}

const server = app.listen(port, '0.0.0.0', () => {
  console.log(`Server is running on http://monitoring-proxy-service:${port}`)
})

const io = socket(server)