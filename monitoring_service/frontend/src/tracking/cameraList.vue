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
  <el-search-table-pagination
    type="local"
    :data="data"
    height="255"
    :page-sizes="[4, 10]"
    :columns="cameracolumns"
  />
</template>
<script lang="js">
import axios from 'axios'
import Vue from 'vue'
import ElSearchTablePagination from 'el-search-table-pagination'
Vue.use(ElSearchTablePagination)
Vue.use(ElSearchTablePagination, {
  axios
})

export default {
  name: 'CameraList',
  props: {
    data:
    {
      required: true,
      type: Array
    }
  },
  data () {
    return {
      cameracolumns: [
        { prop: 'name', label: 'Name', width: 140 },
        { prop: 'location', label: 'Location', width: 140 },
        { prop: 'rtspurl', label: 'RTMPurl', minWidth: 180 }
      ]
    }
  }

}
</script>

<style>
</style>
