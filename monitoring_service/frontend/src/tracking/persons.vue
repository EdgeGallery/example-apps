<template>
  <div class="top-container">
    <div class="width-47">
      <el-tabs type="border-card">
        <el-tab-pane style="height:300px; overflow: auto;">
          <span slot="label"><i class="el-icon-user" /> Persons</span>
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
                ><i
                  data-v-2ed5c93f=""
                  class="el-icon-zoom-in"
                /></span><span
                  data-v-2ed5c93f=""
                  class="el-upload-list__item-delete"
                  @click="beforeDeletePerson(item.name)"
                ><i
                  data-v-2ed5c93f=""
                  class="el-icon-delete"
                /></span></span>
              </div>
            </li>
          </ul>
          <el-upload
            class="el-upload-list el-upload-list--picture-card"
            action="https://localhost:3000/v1/monitor/persons"
            list-type="picture-card"
            :on-success="getPersons"
            :show-file-list="false"
            multiple
          >
            <i
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
    <div class="width-50">
      <el-tabs
        type="border-card"
        @tab-click="handleClick"
      >
        <el-tab-pane>
          <span slot="label"><i class="el-icon-camera" /> Cameras</span>
          <updatedCameraList
            :data="cameraList"
          />
        </el-tab-pane>
        <el-tab-pane>
          <span slot="label"><i class="el-icon-message" /> Messages</span>
          <el-table
            :data="queryMeassages"
            height="300"
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
import { Notification } from 'element-ui'
import updatedCameraList from './cameraList.vue'

export default {
  name: 'Persons',
  data () {
    return {
    // showUpload: true,
      videos: '',
      dialogImageUrl: '',
      dialogVisible: false,
      disabled: false,
      personsList: [],
      queryperson: [],
      queryMeassages: [],
      querySinglePerson: [],
      getPersonDetails: {},
      cameraList: [],
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
        { prop: 'relatedObj', label: 'Name', width: 100 },
        { prop: 'msg', label: 'Arrived At', minWidth: 180 },
        { prop: 'msgid', label: 'MsgID', minWidth: 180 },
        { prop: 'time', label: 'Time', width: 140 }
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
    })
  },
  created () {
    // Client receives the message:
    const socket = io.connect(baseUrl.baseUrl_NodeProxy)
    socket.on('notify', (data) => {
      Notification.error({
        title: data.relatedObj,
        position: 'bottom-right',
        duration: 3000,
        message: `${data.msg} \n  on ${data.time}`
      })
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
          this.$notify.error({
            title: 'Error',
            message: 'Error In Getting Persons'
          })
        })
    },
    // Clear upload
    clearUpload () {
      this.uploadReady = false
      this.$nextTick(() => {
        this.uploadReady = true
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
    // Tabs
    handleClick (tab, event) {
      if (event.target.textContent.includes('Messages')) {
        this.getMessages()
      }
      if (event.target.textContent.includes('Cameras')) {
        this.getCamerasList()
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
.photo-pannel{
    background: white;
    height: 316px;
    padding: 1%;
    overflow: auto;
}
.width-47{
  width: 47%
}
.width-50{
  width: 50%
}
.top-container{
   display: flex;
   height: 380px;
   justify-content: space-between;
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
.padding-1{
  padding: 1% 0% 1% 0%;
}
.font-size-20x {
  font-size: 20px;
}

</style>
