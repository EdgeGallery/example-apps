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
      <video-player
        class="video-player vjs-custom-skin"
        ref="videoPlayer"
        v-if="!local"
        :playsinline="true"
        :options="playerOptions"
      />
      <video
        controls
        height="100%"
        width="100%"
        v-if="local"
      >
        <source
          src="../assets/test.mp4"
          type="video/mp4"
        >
      </video>
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
      isCameraPanel: false,
      local: false,
      // 视频播放
      playerOptions: {
        playbackRates: [0.7, 1.0, 1.5, 2.0],
        autoplay: true,
        muted: false,
        loop: false,
        preload: 'auto',
        language: 'zh-CN',
        aspectRatio: '16:9',
        techOrder: ['flash', 'html5'],
        hls: { withCredentials: false },
        html5: { hls: { withCredentials: false } },
        sources: [{
          type: 'rtmp/hls',
          src: 'rtmp://58.200.131.2:1935/livetv/hunantv'
        }],
        poster: '',
        width: document.documentElement.clientWidth,
        notSupportedMessage: '此视频暂无法播放，请稍后再试',
        controlBar: {
          timeDivider: true,
          durationDisplay: true,
          remainingTimeDisplay: false,
          fullscreenToggle: true
        }
      }
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
  mounted () {

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
