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
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {
  },
  mounted () {},
  methods: {},
  beforeCreate () {
    if (sessionStorage.getItem('before_route')) {
      this.$router.push(sessionStorage.getItem('before_route'))
    }
  }
}
</script>
<style>
#app {
  font-family: Huaweisans, Arial, Microsoft YaHei, FZLTXHJW, Microsoft JhengHei, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  min-width: 988px;
  background-size:cover;
  overflow: auto;
}
.cameraview{
  position: relative !important;
}
body {
  overflow: auto;
  background: #f5f5f5;
  max-height: 100vh;
}
.el-tabs--border-card>.el-tabs_header .el-tabs_item {
    border : none !important
}
</style>
