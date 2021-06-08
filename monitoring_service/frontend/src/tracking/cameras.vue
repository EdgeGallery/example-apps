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
<template>
  <div class="camera-display display-none">
    <!--add video-->
    <el-dialog
      title="Add video"
      :visible.sync="dialogvideoFrom"
    >
      <div class="upload-video-con">
        <span class="upload-video ">UploadVideo:</span>
        <input
          type="file"
          ref="videoFile"
          accept="mp4"
          @change="referenceUpload($event)"
          v-if="uploadReady"
          autocomplete="off"
          aria-label="File browser example"
          class="video-input "
        >
      </div>
      <span
        slot="footer"
        class="dialog-footer"
      >
        <el-button @click="dialogvideoFrom = false">Cancel</el-button>
        <el-button
          type="primary"
          @click="uploadVideoFile() ; dialogvideoFrom = false"
        >Add</el-button>
      </span>
    </el-dialog>

    <el-dialog
      title="Add Camera"
      :visible.sync="dialogFormVisible"
    >
      <el-form
        :model="formData"
        :rules="rules"
        ref="formData"
      >
        <el-form-item
          label="Name"
          prop="name"
          :label-width="formLabelWidth"
        >
          <el-input
            v-model="formData.name"
            autocomplete="off"
          />
        </el-form-item>
        <el-form-item
          label="Location"
          prop="location"
          :label-width="formLabelWidth"
        >
          <el-input
            v-model="formData.location"
            autocomplete="off"
          />
        </el-form-item>
        <el-form-item
          label="RTMP/VIDEO"
          prop="rtspurl"
          :label-width="formLabelWidth"
        >
          <el-input
            v-model="formData.rtspurl"
            autocomplete="off"
          />
        </el-form-item>
      </el-form>
      <span
        slot="footer"
        class="dialog-footer"
      >
        <el-button @click="hideAddCamera">Cancel</el-button>
        <el-button
          type="primary"
          @click="addCamera('formData')"
        >Add</el-button>
      </span>
    </el-dialog>
    <div class="camera_pannel">
      <div
        class="cams-container"
        v-for="(item, index) in cameraList"
        :key="index"
      >
        <camerapannel
          :delcamera="deleteCamera"
          :data="item"
          :index="index"
        />
      </div>
    </div>
  </div>
</template>

<script lang="js">
import axios from 'axios'
import camerapannel from './image.vue'
import baseUrl from '@/config'

export default {
  name: 'Cameras',
  data () {
    return {
      dialogFormVisible: false,
      dialogvideoFrom: false,
      formData: {
        name: '',
        location: '',
        rtspurl: ''
      },
      rules: {
        name: [
          { required: true, message: 'Please input name', trigger: 'blur' },
          { min: 3, max: 10, message: 'Length should be 3 to 10', trigger: 'blur' }

        ],
        location: [
          { required: true, message: 'Please select  zone', trigger: 'change' }
        ],
        rtspurl: [
          { required: true, message: 'Please input rtspurl', trigger: 'blur' }
        ]
      },
      formLabelWidth: '120px',
      cameraList: [],
      queryMeassages: [],
      checked: false,
      uploadReady: true
    }
  },
  components: {
    camerapannel
  },
  mounted () {
    this.getCameras()
  },
  beforeMount () {
    this.$root.$on('addVideoEnable', (data) => {
      this.dialogvideoFrom = data
    })
    this.$root.$on('addCameraEnable', (data) => {
      this.dialogFormVisible = data
    })
  },
  methods: {
    // add camera details
    hideAddCamera () {
      this.dialogFormVisible = false
      this.formData = {
        name: '',
        location: '',
        rtspurl: ''
      }
    },
    // add camera details
    addCamera (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          const URL = baseUrl.baseUrl + 'cameras'
          let cameraConfig = {
            header: {
              'Content-Type': 'application/json'
            }
          }
          let newData = JSON.stringify(this.formData)
          let data1 = JSON.parse(newData)
          data1.name = data1.name + `-${new Date().getTime()}`
          axios.post(URL, data1, cameraConfig).then(
            response => {
              this.getCameras()
              this.$root.$emit('updateCamera', this.cameraList)
              this.clearUpload()
              this.hideAddCamera()
            }
          )
            .catch(error => {
              this.errorMessage = error.message
              console.error('Error from server', error)
              this.clearUpload()
              this.hideAddCamera()
            })
        } else {
          this.$notify({
            title: 'Error',
            message: 'Need to Fill The Required Feilds',
            type: 'error'
          })
          return false
        }
      })
    },
    // Check the video file size
    referenceUpload (e) {
      if (e.currentTarget.files[0].size > 1024 * 1024 * 100) {
        alert('File too big (> 100MB) please make sure video file should be lessThen 100mb')
        this.clearUpload()
      } else {
        this.videoFile = e.currentTarget.files[0]
      }
    },
    // Upload video
    uploadVideoFile () {
      const URL = baseUrl.baseUrl + 'video'
      let data = new FormData()
      data.append('file', this.videoFile)
      let config = {
        header: {
          'Content-Type': 'multipart/form-data'
        }
      }
      axios.post(URL, data, config).then(
        response => {
          this.hideAddCamera()
          this.clearUpload()
          this.$notify({
            title: 'Success',
            message: 'Video uploaded successfully',
            type: 'success'
          })
        }
      )
        .catch(error => {
          this.errorMessage = error.message
          this.$notify.error({
            title: 'Error',
            message: 'Error in Upload Video'
          })
          this.hideAddCamera()
          this.clearUpload()
        })
    },
    // clear Upload
    clearUpload () {
      this.uploadReady = false
      this.$nextTick(() => {
        this.uploadReady = true
      })
    },
    // Get CameraList
    getCameras () {
      this.cameraList = []
      const URL = baseUrl.baseUrl + 'cameras'
      axios.get(URL)
        .then(response => {
          if (response.status === 200) {
            response.data.forEach(el => {
              let rtspurl = el.rtspurl
              let subType = rtspurl.indexOf('.flv')>-1 ? 'video' : 'image'
              let obj = {
                name: el.name,
                type: el.rtspurl.indexOf('mp4') > -1 ? 'video/mp4' : 'rtmp/hls',
                subType: subType,
                location: el.location,
                // src: el.rtspurl.indexOf('mp4') > -1 ? baseUrl.baseUrl + `cameras/${el.name}` : el.rtspurl,
                src: subType == 'image' ? baseUrl.baseUrl + `cameras/${el.name}` : el.rtspurl,
                rtspurl: el.rtspurl
              }
              this.cameraList.push(obj)
            })
            this.$root.$emit('updateCamera', this.cameraList)
            console.log(this.cameraList)
          }
        })
        .catch(error => {
          this.errorMessage = error.message
        })
    },
    // Query Messages
    getMessages () {
      const URL = baseUrl.baseUrl + 'messages'
      axios.get(URL)
        .then(response => {
          this.queryMeassages = response.data
          this.$root.$emit('updateMessages', this.queryMeassages)
        })
        .catch(error => {
          this.errorMessage = error.message
          this.$notify.error({
            title: 'Error',
            message: 'Error In Getting Messages'
          })
        })
    },
    // Delete Camera
    deleteCamera (cameraname) {
      const URL = baseUrl.baseUrl + 'cameras/' + cameraname
      axios.delete(URL)
        .then(response => {
          if (response.status === 200) {
            this.getCameras()
            this.getMessages()
          }
        })
        .catch(error => {
          this.errorMessage = error.message
          this.$notify.error({
            title: 'Error',
            message: 'Error in Deleting Camera Details'
          })
        })
    }
  }

}
</script>

<style scoped lang="less">
.cams-container{
    width: 47%;
    padding: 1%;
}
.camera_pannel{
    width: 100%;
    display: flex;
    justify-content: space-around;
    margin-top: 15px;
    flex-wrap: wrap
}
.upload-video {
    font-size: 16px;
    font-weight: bold;
}
.upload-video-con {
    text-align: center;
    position: relative;
    top: 15px;
}
.video-input {
  padding: 1%;
  border: 1px solid #9e9e9e33;
}
@media(max-width:767.98px) {
  .display-none {
    display: none;
  }
}
</style>
