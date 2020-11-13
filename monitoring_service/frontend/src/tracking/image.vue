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
  <div
    class="cameraview"
  >
    <span
      class="delete-icon"
    >
      <el-button
        type="danger"
        style="padding: 0px"
        icon="el-icon-close"
        @click="beforeDeleteCamera (data.name)"
      />
    </span>
    <img
      class="video-cards"
      :id="data.name"
      :src="data.stramedUrl"
    ><br>
    <br>
    <label class="camera-id">{{ data.name.split('-')[0] }} is at {{ data.location }}</label>
  </div>
</template>

<script>
export default {
  name: 'Camerapannel',
  props: {
    delcamera:
    {
      type: Function,
      required: true
    },
    data:
    {
      type: Object,
      required: true
    }
  },
  data () {
    return {
      value: 'I am the child.',
      isCameraPanel: false
    }
  },
  methods: {
    // Before Delete camera
    beforeDeleteCamera (name) {
      this.$confirm('This will permanently delete the file. Continue?', 'Warning', {
        confirmButtonText: 'OK',
        cancelButtonText: 'Cancel',
        type: 'Are you Sure'
      }).then(() => {
        this.delcamera(name)
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
    }
  }
}
</script>

<style scoped lang="less">
.video-cards{
    width: 400px;
    height: 250px;
    border: 2px solid;
}
.delete-icon{
    position: absolute;
    right: -3px;
    top: 0;
    font-size: 20px;
    color: #606266;
}
.cameraview{
    padding: 1%;
}

</style>
