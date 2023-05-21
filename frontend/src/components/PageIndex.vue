<script setup>
import { defineProps, defineEmits } from 'vue';
defineProps(['curIndex'])
defineEmits(['changeIndex'])

</script>
<script>
import { ref } from 'vue';
const indexs = ref([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
function ChangeIndex(index) {
    let arr = [];
    if (index <= 5) {
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    else {
        for (let i = index - 4; i < index + 6; i++) {
            arr.push(i)
        }
    }
    indexs.value = arr;
}
</script>
<template>
    <div class="index">
        <button v-for="i in indexs" :key="i" :class="['cell', { 'curIndex': curIndex == i }]"
            @click="ChangeIndex(i); $emit('changeIndex', i)">{{ i }}</button>
    </div>
</template>
<style scoped>
div.index {
    position: fixed;
    left: 40%;
    bottom: 5%;
}

button.cell {
    display: inline;
    width: 2em;
    height: 2em;
    margin: 0.1em;
}

button.cell.curIndex {
    background-color: pink;
    border-width: 1px;
}
</style>