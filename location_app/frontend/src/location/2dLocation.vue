/*
 *  Copyright 2021 Huawei Technologies Co., Ltd.
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
    id="div_d2Img"
    class="d2Img-container"
  >
    <img
      id="myImg"
      class="img"
      :src="bgImg"
    >
    <canvas
      id="mycanvas"
      width="1920px"
      height="1080px"
      class="canvas"
    />
  </div>
</template>
<script lang="js">

export default {
  name: 'D2Location',
  data () {
    return {
      currLocData: {},
      bgImgData: [
        require('../assets/images/locations/location_1.jpg'),
        require('../assets/images/locations/location_2.jpg'),
        require('../assets/images/locations/location_3.jpg'),
        require('../assets/images/locations/location_4.jpg'),
        require('../assets/images/locations/location_5.jpg'),
        require('../assets/images/locations/location_6.jpg'),
        require('../assets/images/locations/location_7.jpg')
      ],
      headerImgData: {
        'header_1': require('../assets/images/headers/header_1.png'),
        'header_2': require('../assets/images/headers/header_2.png'),
        'header_3': require('../assets/images/headers/header_3.png'),
        'header_5_1': require('../assets/images/headers/header_5_1.png'),
        'header_5_2': require('../assets/images/headers/header_5_2.png'),
        'header_5_3': require('../assets/images/headers/header_5_3.png'),
        'header_5_4': require('../assets/images/headers/header_5_4.png'),
        'header_6_1': require('../assets/images/headers/header_6_1.png'),
        'header_7_2': require('../assets/images/headers/header_7_2.png'),
        'header_7_3': require('../assets/images/headers/header_7_3.png'),
        'header_7_4': require('../assets/images/headers/header_7_4.png')
      },

      currMapId: -1,
      currHeaderName: '',

      bgImg: null,
      headerImg: null,
      canvas: null,
      context: null,

      drawCircleInterval: null,
      outterCircleSize: 5
    }
  },
  beforeMount () {
    this.$root.$on('drawLocation', (currLocData) => {
      this.currLocData = currLocData
      this.doDraw(this.currLocData)
    })
  },
  mounted () {
    this.canvas = document.getElementById('mycanvas')
    this.context = this.canvas.getContext('2d')
  },
  methods: {
    doDraw (currLocData) {
      clearInterval(this.drawCircleInterval)
      this.drawCircleInterval = null

      // 1. Draw Scene
      let _isChangeScene = this.currMapId !== -1 && this.currLocData.locationInfo.mapId !== this.currMapId
      this.currMapId = this.currLocData.locationInfo.mapId
      if (!_isChangeScene) {
        if (!this.bgImg) {
          this.bgImg = this.bgImgData[this.currLocData.locationInfo.mapId - 1]
        }
      } else {
        this.switchScene()
      }

      // 2. Draw Header
      let _isChangeHeader = this.currLocData.locationInfo.header !== this.currHeaderName
      this.currHeaderName = this.currLocData.locationInfo.header
      if (_isChangeHeader) {
        this.headerImg = new Image()
        this.headerImg.src = this.headerImgData[this.currHeaderName]

        let _canvas = this.canvas
        let _context = this.context
        let _headerImg = this.headerImg
        this.headerImg.onload = function () {
          _context.clearRect(0, 0, _canvas.width, _canvas.height)
          if (!currLocData.locationInfo.hide) {
            _context.drawImage(_headerImg, currLocData.locationInfo.hx, currLocData.locationInfo.hy,
              _headerImg.width, _headerImg.height)
          }

          let _circleX = currLocData.locationInfo.hx + _headerImg.width / 2
          let _circleY = currLocData.locationInfo.hy - 4

          _context.fillStyle = '#FFFFE0'
          _context.fillRect(_circleX - 60, _circleY - 10 - 18, 120, 20)
          let _locText = '位置:(' + currLocData.locationInfo.x + ', ' + currLocData.locationInfo.y + ', ' + currLocData.locationInfo.z + ')'
          _context.font = '12px "微软雅黑"'
          _context.fillStyle = 'blue'
          _context.textAlign = 'center'
          _context.textBaseline = 'bottom'
          _context.fillText(_locText, _circleX, _circleY - 10)

          let _outterCircleSize = 15
          _context.beginPath()
          _context.fillStyle = 'RGBA(130, 255, 130, 0.5)'
          _context.arc(_circleX, _circleY, _outterCircleSize, 0, Math.PI * 2, false)
          _context.fill()

          _context.beginPath()
          _context.fillStyle = 'green'
          _context.arc(_circleX, _circleY, 4, 0, Math.PI * 2, false)
          _context.fill()
        }
      } else {
        this.drawHeader()
      }
    },
    switchScene () {
      const loading = this.$loading({
        lock: true,
        text: '请稍候...',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)'
      })
      setTimeout(() => {
        loading.close()
        this.bgImg = this.bgImgData[this.currLocData.locationInfo.mapId - 1]
      }, 200)
    },
    drawHeader () {
      this.outterCircleSize = 6
      this.drawCircleInterval = setInterval(() => {
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height)
        if (!this.currLocData.locationInfo.hide) {
          this.context.drawImage(this.headerImg, this.currLocData.locationInfo.hx, this.currLocData.locationInfo.hy,
            this.headerImg.width, this.headerImg.height)
        }

        let _circleX = this.currLocData.locationInfo.hx + this.headerImg.width / 2
        let _circleY = this.currLocData.locationInfo.hy - 4

        this.context.fillStyle = '#FFFFE0'
        this.context.fillRect(_circleX - 60, _circleY - 10 - 18, 120, 20)
        this.context.font = '12px "微软雅黑"'
        this.context.fillStyle = 'blue'
        this.context.textAlign = 'center'
        this.context.textBaseline = 'bottom'
        this.context.fillText(this.buildLocationText(this.currLocData), _circleX, _circleY - 10)

        this.context.beginPath()
        this.context.fillStyle = 'RGBA(130, 255, 130, 0.5)'
        this.context.arc(_circleX, _circleY, this.outterCircleSize, 0, Math.PI * 2, false)
        this.context.fill()

        this.context.beginPath()
        this.context.fillStyle = 'green'
        this.context.arc(_circleX, _circleY, 4, 0, Math.PI * 2, false)
        this.context.fill()

        this.outterCircleSize = this.outterCircleSize + 3
        if (this.outterCircleSize > 12) {
          clearInterval(this.drawCircleInterval)
          this.drawCircleInterval = null
        }
      }, 200)
    },
    buildLocationText (currLocData) {
      return '位置:(' + currLocData.locationInfo.x + ', ' + currLocData.locationInfo.y + ', ' + currLocData.locationInfo.z + ')'
    }
  }
}
</script>

<style scoped lang="less">
 .d2Img-container {
  border:0px solid red;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  overflow: auto;

  .img{
    border:0px solid green;
  }

  .canvas{
    border: 0px solid blue;
    position: absolute;
    top: 0;
    left: 0;
  }
}
</style>
