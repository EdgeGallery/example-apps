<template>
  <div
    class="cameraview"
  >
    <span
      class="delete-icon"
    >
      <el-button
        type="danger"
        style="padding: 0px"
        icon="el-icon-close"
        @click="beforeDeleteCamera (data.name)"
      />
    </span>
    <img
      class="video-cards"
      :id="data.name"
      :src="data.stramedUrl"
    ><br>
    <br>
    <label class="camera-id">{{ data.name.split('-')[0] }} is at {{ data.location }}</label>
  </div>
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
      isCameraPanel: false
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
  }
}
</script>

<style scoped lang="less">
.video-cards{
    width: 400px;
    height: 250px;
    border: 2px solid;
}
.delete-icon{
    position: absolute;
    right: -3px;
    top: 0;
    font-size: 20px;
    color: #606266;
}
.cameraview{
    padding: 1%;
}

</style>
