<template>
  <el-table
    :data="data"
    height="300"
  >
    <el-table-column
      v-for="column in cameracolumns"
      :key="column.prop"
      :prop="column.prop"
      :label="column.label"
      :width="column.width"
    />
  </el-table>
</template>
<script lang="js">
export default {
  name: 'CameraList',
  props: {
    data:
    {
      type: Array
    }
  },
  data () {
    return {
      cameracolumns: [
        { prop: 'name', label: 'Name', width: 140 },
        { prop: 'location', label: 'Location', width: 140 },
        { prop: 'rtspurl', label: 'RTSPurl', minWidth: 180 }
      ]
    }
  }

}
</script>

<style>

</style>
