<template>
  <div
    id="app"
    class="track-container"
  >
    <persons />
    <cameras />
  </div>
</template>
<script lang="js">
import persons from './persons.vue'
import cameras from './cameras.vue'

export default {
  name: 'Track',
  props: [],
  components: {
    'persons': persons,
    'cameras': cameras
  },
  data () {
    return {
    }
  },
  methods: {

  }
}
</script>

<style scoped lang="less">
 .track-container {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  margin-top: 70px;
  padding: 0 30px;
}
</style>
