<script setup>
import { defineProps } from 'vue';
defineProps(['imgPool']);
</script>
<script>
function Redirect(url) {
    window.location.href = url;
}
</script>

<template>
    <div class="frame">
        <img v-for="(img, index) in imgPool" :key="index" :src="img" @click="Redirect(img)">
    </div>
</template>

<style scoped>
/* div.frame {
    overflow-y: scroll;
} */

img {
    max-width: 50em;
    max-height: 50em;
    min-width: 10em;
    min-height: 10em;
    float: left;
    position: relative;
    margin: 2em;
}
</style>