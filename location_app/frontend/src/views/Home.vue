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
  <div class="home">
    <Navbar />
    <div class="home-container">
      <router-view id="container" />
    </div>
  </div>
</template>

<script>
import Navbar from '../components/Nav.vue'
export default {
  name: 'Home',
  components: {
    Navbar
  },
  data () {
    return {
      keepAlive: true
    }
  },
  beforeMount () {

  },
  methods: {

  },
  watch: {
  },
  mounted () {
    let userAgent = navigator.userAgent
    if (userAgent.indexOf('Chrome') > -1) {
      // ok
    } else {
      this.$notify.warning({
        title: 'warning',
        message: this.$t('tip.browserAdvise'),
        showClose: false,
        duration: 0,
        offset: 60
      })
    }
  }
}
</script>
