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
  <el-card :body-style="{ padding: '0px' }">
    <div class="video-cards">
      <div
        class="video-player vjs-custom-skin"
        v-if="data.subType == 'image'"
      >
      <img
        :id="data.name"
        class="video-cards"
        :src="data.src"
      >

      </div>
      <div
        class="video-player vjs-custom-skin"
        v-if="data.subType == 'video'"
      >
        <video
          muted
          id="videoElement"
          width="100%"
          height="100%"
        />
      </div>
    </div>
    <div style="padding: 14px;">
      <div class="camera-details-con">
        <div class="bottom clearfix cd-text">
          <label class="camera-id">{{ data.name.split('-')[0] }} is at {{ data.location }}</label>
        </div>
        <el-button
          type="primary"
          icon="el-icon-delete"
          @click="beforeDeleteCamera (data.name)"
          style="padding: 5px"
        />
      </div>
    </div>
  </el-card>
</template>

<script>
import flvjs from 'flv.js'
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
      flvPlayer: null
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
  },
  computed: {
    vidId: function () {
      return this.data.name + 'videoElement'
    }
  },
  mounted () {
    if (flvjs.isSupported()) {
      var videoElement = document.getElementById(this.vidId)
      this.flvPlayer = flvjs.createPlayer({
        type: 'mp4',
        isLive: true,
        url: this.data.src
      }, {
        enableWorker: false,
        enableStashBuffer: false,
        isLive: true,
        lazyLoad: false,
        stashInitialSize: 0,
        autoCleanupSourceBuffer: true
      })
      this.flvPlayer.attachMediaElement(videoElement)
      this.flvPlayer.load()
      let playPromise = this.flvPlayer.play()
      if (playPromise !== undefined) {
        playPromise.then(() => {
          this.flvPlayer.play()
        }).catch((e) => { console.log(e) })
      }
    }
  }
}
</script>

<style scoped lang="less">
.video-cards{
    width: 100%;
    height: 500px;
}
.camera-details-con {
    display: flex;
    justify-content: space-between;
}
.cd-text{
    font-size: 22px;
    font-weight: bold;
}
</style>
