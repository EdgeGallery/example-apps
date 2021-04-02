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
  <div class="top-container xs-height-100">
    <div class="width-47 display-none">
      <el-tabs type="border-card">
        <el-tab-pane
          style="height:300px; overflow: auto;"
          class="tabs-border"
        >
          <span slot="label"><em class="el-icon-user" /> Persons</span>
          <ul
            class="el-upload-list el-upload-list--picture-card"
            v-for="(item, index) in personsList"
            :key="index"
          >
            <li
              tabindex="0"
              class="el-upload-list__item is-ready"
            >
              <div
                data-v-2ed5c93f=""
              >
                <img
                  data-v-2ed5c93f=""
                  :src="item.file"
                  alt=""
                  accept="image/jpeg"
                  class="el-upload-list__item-thumbnail"
                ><span
                  data-v-2ed5c93f=""
                  class="el-upload-list__item-actions"
                ><span
                  data-v-2ed5c93f=""
                  class="el-upload-list__item-preview"
                  @click="handlePictureCardPreview(item.file)"
                ><em
                  data-v-2ed5c93f=""
                  class="el-icon-zoom-in"
                /></span><span
                  data-v-2ed5c93f=""
                  class="el-upload-list__item-delete"
                  @click="beforeDeletePerson(item.name)"
                ><em
                  data-v-2ed5c93f=""
                  class="el-icon-delete"
                /></span></span>
              </div>
            </li>
          </ul>
          <el-upload
            class="el-upload-list el-upload-list--picture-card"
            :action="baseURL"
            list-type="picture-card"
            :on-success="getPersons"
            :show-file-list="false"
            multiple
          >
            <em
              slot="default"
              class="el-icon-plus"
            />
            <div
              slot="file"
              slot-scope="{file}"
            >
              <img
                class="el-upload-list__item-thumbnail"
                :src="file.url"
                alt=""
              >
            </div>
          </el-upload>
        </el-tab-pane>
      </el-tabs>
      <el-dialog :visible.sync="dialogVisible">
        <img
          width="100%"
          :src="dialogImageUrl"
          alt=""
        >
      </el-dialog>
    </div>
    <!--******************MobileView************************-->
    <div
      class="web-display-none mobile-display-block xs-height-100"
      style="width:100%"
    >
      <el-tabs type="border-card">
        <el-tab-pane
          style="overflow: auto;"
          class="tabs-border"
        >
          <span slot="label"><em class="el-icon-user" /> Persons</span>
          <h3 class="h3-lable">
            PersonName
          </h3>
          <el-input
            placeholder="Please Add PersonName"
            v-model="person_name"
          />
          <h3 class="h3-lable">
            AddPicture
          </h3>
          <div class="file-input-wrapper">
            <button class="btn-file-input">
              Click to add Picture
            </button>
            <input
              type="file"
              ref="personPic"
              accept="jpg"
              @change="referenceUpload($event)"
              v-if="uploadReady"
              autocomplete="off"
              aria-label="File browser example"
            >
          </div>
          <span id="img_text" />
          <el-button
            style="width: 50%; margin-left: 25%; margin-top:40px;"
            size="small"
            type="success"
            @click="uploadPerson()"
          >
            Submit
          </el-button>
          <h3 class="xs-list">
            PersonsList
          </h3>
          <ul
            class="el-upload-list el-upload-list--picture"
            v-for="(item, index) in personsList"
            :key="index"
          >
            <li
              tabindex="0"
              class="el-upload-list__item is-success"
            >
              <img
                :src="item.file"
                alt=""
                class="el-upload-list__item-thumbnail"
              ><a class="el-upload-list__item-name"><em class="el-icon-document" />{{ item.name }}
              </a><label class="el-upload-list__item-status-label"><em class="el-icon-upload-success el-icon-check" /></label><em
                class="el-icon-close"
                @click="beforeDeletePerson(item.name)"
              /><em class="el-icon-close-tip">按 delete 键可删除</em>
            </li>
          </ul>
        </el-tab-pane>
      </el-tabs>
      <el-dialog :visible.sync="dialogVisible">
        <img
          width="100%"
          :src="dialogImageUrl"
          alt=""
        >
      </el-dialog>
    </div>
    <!--**************************************-->
    <div class="width-47 display-none">
      <el-tabs
        type="border-card"
        @tab-click="handleClick"
      >
        <el-tab-pane class="tabs-border">
          <span slot="label"><em class="el-icon-camera" /> Cameras</span>
          <updatedCameraList
            :data="upDatedCameralist"
          />
        </el-tab-pane>
        <el-tab-pane class="tabs-border">
          <span slot="label"><em class="el-icon-message" /> Messages</span>
          <el-table
            :data="queryMeassages"
            height="300"
            :row-class-name="tableRowClassName"
          >
            <el-table-column
              v-for="column in columns"
              :key="column.prop"
              :prop="column.prop"
              :label="column.label"
              :width="column.width"
            />
          </el-table>
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>

<script lang="js">

import axios from 'axios'
import baseUrl from '@/config'
import io from 'socket.io-client'
import updatedCameraList from './cameraList.vue'

export default {
  name: 'Persons',
  data () {
    return {
    // showUpload: true,
      person_name: '',
      videos: '',
      dialogImageUrl: '',
      pictureFile: '',
      baseURL: baseUrl.baseUrl + 'persons',
      dialogVisible: false,
      disabled: false,
      personsList: [],
      queryperson: [],
      queryMeassages: [],
      querySinglePerson: [],
      getPersonDetails: {},
      cameraList: [],
      upDatedCameralist: [],
      uploadReady: true,
      formOptions: {
        inline: true,
        submitBtnText: 'Search',
        forms: [
          { prop: 'relatedObj', label: 'Name' },
          { prop: 'msg', label: 'Arrived At' },
          { prop: 'msgid', label: 'MsgID' },
          { prop: 'time', label: 'Time' }
        ]
      },
      columns: [
        { prop: 'relatedObj', label: 'Name', width: 120 },
        { prop: 'msg', label: 'Arrived At', minWidth: 260 },
        { prop: 'msgid', label: 'MsgID', width: 80 },
        { prop: 'time', label: 'Time', width: 180 }
      ],
      isPersonsClicked: false
    }
  },
  components: {
    updatedCameraList
  },
  beforeMount () {
    this.$root.$on('updateCamera', (data) => {
      this.cameraList = data
      this.upDatedCameralist = this.cameraList.map(item => {
        const container = {}
        container.name = item.name.split('-')[0]
        container.location = item.location
        container.rtspurl = item.rtspurl
        return container
      })
    })
    this.$root.$on('updateMessages', (data) => {
      this.queryMeassages = data
    })
  },
  created () {
    // Client receives the message:
    const socket = io.connect(baseUrl.baseUrl_NodeProxy)
    socket.on('notify', (data) => {
      this.getMessages()
    })
  },
  mounted () {
    this.getPersons()
  },
  methods: {
    notify () {
      const dd = { 'msgId': '1', 'time': '2020-09-19 10:25', 'relatedObj': 'zhanghailong', 'msg': 'zhanghailong appears at Shenzhen Lab door.' }
      const URL = baseUrl.baseUrl_NodeProxy + 'notify'
      axios.post(
        URL,
        dd
      ).then(response => {
      }).catch(error => {
        this.errorMessage = error.message
      })
    },
    getPersons () {
      const URL = baseUrl.baseUrl_NodeProxy + 'persons'
      axios.get(URL)
        .then(response => {
          this.personsList = response.data
        })
        .catch(error => {
          this.errorMessage = error.message
        })
    },
    // Mobile Upload
    // Check the picture file size
    referenceUpload (e) {
      if (e.currentTarget.files[0].size > 1024 * 1024 * 100) {
        alert('File too big (> 100MB) please make sure video file should be lessThen 100mb')
        this.clearUpload()
      } else {
        this.pictureFile = e.currentTarget.files[0]
      }
    },
    // Clear upload for Mobile App
    clearUpload () {
      this.uploadReady = false
      this.$nextTick(() => {
        this.uploadReady = true
      })
    },
    // Upload person for Mobile APP
    uploadPerson () {
      const URL = baseUrl.baseUrl + 'persons'
      let data = new FormData()
      data.append('person_name', this.person_name)
      data.append('file', this.pictureFile)

      let config = {
        header: {
          'Content-Type': 'multipart/form-data'
        }
      }
      axios.post(URL, data, config).then(
        response => {
          this.clearUpload()
          this.person_name = ''
          this.getPersons()
          this.$notify({
            title: 'Success',
            message: 'Person added successfully',
            type: 'success'
          })
        }
      )
        .catch(error => {
          this.errorMessage = error.message
          this.$notify.error({
            title: 'Error',
            message: 'Error in Upload Picture'
          })
          this.clearUpload()
        })
    },

    // view person image
    handlePictureCardPreview (file) {
      this.dialogImageUrl = file
      this.dialogVisible = true
    },
    // Query Messages
    getMessages () {
      const URL = baseUrl.baseUrl + 'messages'
      axios.get(URL)
        .then(response => {
          this.queryMeassages = response.data
          setTimeout(function () {
            this.getMessages()
          }.bind(this),
          15000)
        })
        .catch(error => {
          this.errorMessage = error.message
          this.$notify.error({
            title: 'Error',
            message: 'Error In Getting Messages'
          })
        })
    },
    // Remove person from system
    handleRemove (personname) {
      const URL = baseUrl.baseUrl + 'persons/' + personname
      axios.delete(URL)
        .then(response => {
          if (response.status === 200) {
            this.getPersons()
            this.getMessages()
          }
        })
        .catch(error => {
          this.errorMessage = error.message
          this.$notify.error({
            title: 'Error',
            message: 'Error In Deleting Person'
          })
        })
    },
    // Before Delete person
    beforeDeletePerson (name) {
      this.$confirm('This will permanently delete the file. Continue?', 'Warning', {
        confirmButtonText: 'OK',
        cancelButtonText: 'Cancel',
        type: 'Are you Sure'
      }).then(() => {
        this.handleRemove(name)
        this.$message({
          type: 'success',
          message: 'Delete completed'
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: 'Delete canceled'
        })
      })
    },
    tableRowClassName ({ row, rowIndex }) {
      if (row.highlight === 'True') {
        return 'warning-row'
      } else if (row.highlight === 'False') {
        return 'success-row'
      }
    },
    // Tabs
    handleClick (tab, event) {
      if (event.target.textContent.includes('Messages')) {
        this.getMessages()
      }
    },
    // Query only one persons Messages
    getSinglePerson (person) {
      const URL = baseUrl.baseUrl + person
      axios.get(URL)
        .then(response => {
          this.querySinglePerson = response.data
        })
        .catch(error => {
          this.errorMessage = error.message
        })
    }
  }

}
</script>

<style scoped lang="less">
.width-47{
  width: 47%
}
.top-container{
   display: flex;
   height: 380px;
   justify-content: space-around;
   padding-top: 1%;
}
.el-upload {
   .el-upload--picture-card {
    width: 148px !important;
  }
}
.upload {
  display: contents;
}
#file-input {
   opacity: 0;
   position: absolute;
   z-index: -1;
}
.user-icon{
    text-align: center;
    vertical-align: middle;
    display: table-cell;
}
.user-icon-prop{
  font-size: 40px;
  cursor: pointer;
}
.web-display-none{
  display: none;
}
@media(max-width:767.98px) {
  .display-none {
    display: none;
  }
  .mobile-display-block {
    display: block
  }
  .h3-lable{
    padding: 1%;
    font-size: 17px;
  }
  .xs-height-100{
    height: 100%;
  }
  .xs-list{
    text-align: left;
    margin-top: 30px;
  }
  .xs-fileupload{
    width: 97%;
    background: #409eff;
    height: 30px;
    color: #fff;

    border-color: #409eff;
    border-radius: 4px;
    padding-top: 7px;
    border: 1px solid #dcdfe6;
    padding-left: 8px;
  }
  .pad-lef{
    padding-left: 10px;
  }
  .file-input-wrapper {
    height: 30px;
    background-color: #fff;
    cursor: pointer;
    width: 100%;
    position: relative;
}
.file-input-wrapper>input[type="file"] {
  font-size: 40px;
  position: absolute;
  top: 0;
  right: 0;
  opacity: 0;
  cursor: pointer;
}

.file-input-wrapper>.btn-file-input {
  width: 100%;
  background-color: #409eff;
  border-radius: 4px;
  color: #fff;
  display: inline-block;
  height: 40px;
  margin: 0 0 0 -1px;
  cursor: pointer;
  border: 1px solid gainsboro;
}
}
</style>
