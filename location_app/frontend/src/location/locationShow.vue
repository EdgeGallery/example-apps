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
    id="div_locationShow"
    class="location-show-container"
  >
    <D2Location
      v-if="locating && is2D"
    />
    <div
      v-show="!locating"
      class="startLocate-container"
    >
      <el-row>
        <el-col :span="24">
          <span style="font-size:12px">定位目标的UE IMSI号码（<font color="blue">当前不支持修改为其它目标</font>）：</span>
        </el-col>
      </el-row>
      <el-row style="margin-top:10px">
        <el-col :span="24">
          <el-form
            :model="formData"
            :rules="rules"
            ref="formData"
          >
            <el-form-item prop="ueId">
              <el-input
                disabled
                id="input_ueId"
                v-model="formData.ueId"
                clearable
                placeholder="imsi:"
              />
            </el-form-item>
          </el-form>
        </el-col>
      </el-row>
      <el-row style="text-align:center">
        <el-col :span="24">
          <el-button
            type="primary"
            size="large"
            @click="startLocate('formData')"
          >
            开始定位
          </el-button>
        </el-col>
      </el-row>
    </div>
  </div>
</template>
<script lang="js">

import axios from 'axios'
import baseUrl from '@/config'
import D2Location from './2dLocation.vue'

export default {
  name: 'LocationShow',
  components: {
    D2Location
  },
  data () {
    var validateUeIdBlank = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('IMSI号码不能为空'))
      } else {
        callback()
      }
    }
    var validateUeIdRule = (rule, value, callback) => {
      let pattern = /^imsi:\d{15,15}$/
      if (value.match(pattern) === null) {
        callback(new Error('IMSI号码格式无效'))
      } else {
        callback()
      }
    }
    return {
      locating: false,
      loading: null,
      is2D: true,
      formData: {
        ueId: 'imsi:460000000000013'
      },
      rules: {
        ueId: [
          { validator: validateUeIdBlank, trigger: 'blur' },
          { validator: validateUeIdRule }
        ]
      },
      getLocTimer: null,

      currX: 0,
      currLocData: {}
    }
  },
  beforeMount () {
    this.$root.$on('stopLocation', () => {
      this.stopLocation()
    })
  },
  mounted () {
  },
  beforeDestroy () {
    this.clearTimer()
  },
  methods: {
    startLocate (formName) {
      this.$refs[formName].validate((valid) => {
        if (!valid) {
          return
        }

        this.doStartLocate()
      })
    },
    doStartLocate () {
      this.loading = this.$loading({
        lock: true,
        text: '开始定位，请稍候...',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)'
      })
      setTimeout(() => {
        this.loading.close()
      }, 2000)
      this.getLocTimer = setInterval(() => {
        this.refreshLocation()
      }, 1200)
    },
    refreshLocation () {
      const URL = baseUrl.baseUrl + 'v1/location/users?ueId=' + this.formData.ueId
      axios.get(URL).then(response => {
        this.currLocData = response.data

        this.$root.$emit('locateSuccess')
        this.locating = true
        this.is2D = this.judgeIs2D(this.currLocData.locationInfo.mapId)
        this.$root.$emit('drawLocation', this.currLocData)
      }).catch(error => {
        this.errorMessage = error.message
        this.clearTimer()
        this.currLocData = {}
        this.$alert('位置定位失败！', '提示', {
          confirmButtonText: '确定',
          callback: action => {
            this.locating = false
            this.$root.$emit('locateFailed')
          }
        })
      })
    },
    judgeIs2D (mapId) {
      return mapId <= 10
    },
    stopLocation () {
      this.locating = false
      this.clearTimer()
    },
    clearTimer () {
      clearTimeout(this.getLocTimer)
      this.getLocTimer = null
    }
  }
}
</script>

<style scoped lang="less">
 .location-show-container {
  border: 0px solid red;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  margin-top: 64px;
  max-height: 100vh;
  overflow: auto;
  background-color: #FFFFFF;

  .startLocate-container{
    border: 0px solid green;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    max-height: 100vh;
    margin-top: 200px;
    margin-left: 35%;
    margin-right: 35%;
  }
}
</style>
