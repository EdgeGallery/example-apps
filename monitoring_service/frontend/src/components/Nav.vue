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
    <div
      class="logo lt"
      @click="jumpLogoTo"
    >
      <img
        src="../assets/images/logo.png"
        alt=""
      >
    </div>
    <span class="logo-header">Monitoring Service</span>
  </div>
</template>

<script>
export default {
  name: 'Navgation',
  components: {
  },
  data () {
    return {
      language: 'English'
    }
  },
  watch: {
  },
  mounted () {
  },
  methods: {
    jumpLogoTo () {
      this.$router.push('/')
    }
  }
}
</script>

<style lang='less' scoped>
.navgation{
  background: #282B33;
  height: 65px;
  top: 0px;
  width: 100%;
  position: fixed;
  z-index: 2;
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
    line-height: 60px;
  }
}
</style>
