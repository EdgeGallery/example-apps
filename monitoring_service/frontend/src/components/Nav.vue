<!--
  -  Copyright 2020 Huawei Technologies Co., Ltd.
  -
  -  Licensed under the Apache License, Version 2.0 (the "License");
  -  you may not use this file except in compliance with the License.
  -  You may obtain a copy of the License at
  -
  -      http://www.apache.org/licenses/LICENSE-2.0
  -
  -  Unless required by applicable law or agreed to in writing, software
  -  distributed under the License is distributed on an "AS IS" BASIS,
  -  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  -  See the License for the specific language governing permissions and
  -  limitations under the License.
  -->

<template>
  <div class="navgation">
    <div style="width: 50%;">
      <div
        class="logo lt"
        @click="jumpLogoTo"
      >
        <img
          src="../assets/images/logo.png"
          alt=""
        >
      </div>
      <div class="logo-header">
        <span>Monitoring Service</span>
      </div>
    </div>
    <div class="AddDetais">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <span @click="addVideoEnable()">
            Add Video
          </span>
        </el-breadcrumb-item>
        <el-breadcrumb-item>
          <span @click="addCameraEnable()">
            Add Camera
          </span>
        </el-breadcrumb-item>
      </el-breadcrumb>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Navgation',
  components: {
  },
  data () {
    return {
      language: 'English',
      isaddVideo: true,
      isaddCamera: true
    }
  },
  watch: {
  },
  mounted () {
  },
  methods: {
    jumpLogoTo () {
      this.$router.push('/')
    },
    addVideoEnable () {
      this.$root.$emit('addVideoEnable', this.isaddVideo)
    },
    addCameraEnable () {
      this.$root.$emit('addCameraEnable', this.isaddCamera)
    }
  }
}
</script>

<style lang='less' scoped>
.navgation{
  background-image: linear-gradient(to right, #404b5f, #587cb9, #F0F3FA);
  // background-image: linear-gradient(to right, #650675, #115286, #F0F3FA);
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  height: 65px;
  top: 0px;
  width: 100%;
  position: fixed;
  z-index: 2;
  display: flex;
  .logo{
    height:65px;
    width:200px;
    line-height: 65px;
    margin-left:17px;
    img{
      position: relative;
      top: 0px;
      width:150px;
      cursor: pointer;
    }
  }
  .logo-header{
    font-size: 23px;
    color: white;
    font-weight: bold;
    display: flex;
    flex-direction: column;
    height: 65px;
    width: 223px;
    justify-content: center;
        margin-left: 17px;
  }
  .AddDetais{
    display: flex;
    height:65px;
    width:50%;
    justify-content: flex-end;
    align-items: center
  }
}
</style>
