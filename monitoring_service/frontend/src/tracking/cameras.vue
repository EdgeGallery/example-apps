<template>
  <div class="camera-display">
    <div class="padding-1">
      <span class=" font-size-20x">
        Live Streaming
      </span>
      <el-button
        type="primary"
        @click="dialogFormVisible = true"
        class="add-cam"
      >
        Add Camera
      </el-button>
    </div>
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
          label="Zones"
          prop="location"
          :label-width="formLabelWidth"
        >
          <el-select
            v-model="formData.location"
            placeholder="Please select a zone"
          >
            <el-option
              label="shanghai-lab"
              value="shanghai-lab"
            />
            <el-option
              label="beijing-lab"
              value="beijing-lab"
            />
          </el-select>
        </el-form-item>
        <el-form-item
          label="RTSPurl"
          prop="rtspurl"
          :label-width="formLabelWidth"
        >
          <el-input
            v-model="formData.rtspurl"
            autocomplete="off"
          />
        </el-form-item>
        <el-form-item style="margin-left: 53px;">
          <el-checkbox v-model="checked">
            Click here to UploadVideo
          </el-checkbox>
        </el-form-item>
        <el-form-item
          v-if="checked"
          label="UploadVideo"
          :label-width="formLabelWidth"
        >
          <div>
            <input
              type="file"
              ref="videoFile"
              accept="mp4"
              @change="referenceUpload($event)"
              v-if="uploadReady"
              autocomplete="off"
              aria-label="File browser example"
            >
          </div>
        </el-form-item>
      </el-form>
      <span
        slot="footer"
        class="dialog-footer"
      >
        <el-button @click="hideAddCamera">Cancel</el-button>
        <el-button
          type="primary"
          @click="addCamera('formData') ; uploadPersonsVideo()"
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
          this.formData.name = `${this.formData.name}-${new Date().getTime()}`
          axios.post(URL, this.formData, cameraConfig).then(
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
    uploadPersonsVideo () {
      if (this.checked === true) {
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
      }
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
      const URL = baseUrl.baseUrl + 'cameras'
      axios.get(URL)
        .then(response => {
          if (response.status === 200) {
            this.cameraList = response.data
            this.$root.$emit('updateCamera', this.cameraList)
            for (let i = 0; i <= this.cameraList.length; i++) {
              this.cameraList[i]['stramedUrl'] = `http://localhost:3000/v1/monitor/cameras/${this.cameraList[i].name}/${this.cameraList[i].rtspurl}/${this.cameraList[i].location}`
            }
          }
        })
        .catch(error => {
          this.errorMessage = error.message
          this.$notify.error({
            title: 'Error',
            message: 'Error in Getting Camera Details'
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
.video-cards{
    width: 400px;
    height: 250px;
}
.cams-container{
    padding: 1%;
}
.camera-id{
  font-size: 20px;
  padding-top: 2%;
}
.add-cam{
  float: right;
  margin-bottom: 20px;
}
.camera_pannel{
    width: 100%;
    display: flex;
    flex-wrap: wrap;
}
.padding-1{
  padding: 1% 0% 1% 0%;
}
.font-size-20x {
  font-size: 20px;
  font-weight: bold
}
</style>
