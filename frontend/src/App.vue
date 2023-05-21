<script setup>
import Page from './components/PageTemplate.vue'
import Index from './components/PageIndex.vue'
import { ref } from 'vue'
const imgPool = ref([
  'http://flpflan.top/a.jpg',
  'http://flpflan.top/a.jpg',
  'http://flpflan.top/test.jpg',
  'http://flpflan.top/a.jpg',
  'http://flpflan.top/test.jpg',
  'http://flpflan.top/a.jpg',
  'http://flpflan.top/a.jpg',
  'http://flpflan.top/a.jpg',
  'http://flpflan.top/test.jpg',
  'http://flpflan.top/a.jpg',
  'http://flpflan.top/a.jpg',
  'http://flpflan.top/test.jpg',
  'http://flpflan.top/a.jpg'
])
const currentIndex = ref(1)
</script>
<template>
  <Page v-bind:imgPool="imgPool.slice(4 * (currentIndex - 1), 4 * currentIndex)" />
  <Index :curIndex=currentIndex @changeIndex="i => currentIndex = i" />
</template>
<style>
body {
  background-color: aquamarine;
}
</style>