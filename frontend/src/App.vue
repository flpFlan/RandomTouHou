<script setup>
import Page from './components/PageTemplate.vue'
import Index from './components/PageIndex.vue'
import { ref } from 'vue'
import axios from 'axios'

const imgPool = ref(["http://flpflan.top/a.jpg"])
const currentIndex = ref(1)

function get() {
  axios.get('http://127.0.0.1:5000/arts').then(res => {
    imgPool.value = res.data
  }).catch(err => {
    console.log(err)
    document.write(err)
  })
}
</script>
<template>
  <Page v-bind:imgPool="imgPool.slice(4 * (currentIndex - 1), 4 * currentIndex)" />
  <Index :curIndex=currentIndex @changeIndex="i => currentIndex = i" />
  <button @click="get">请求</button>
</template>
<style>
body {
  background-color: aquamarine;
}
</style>