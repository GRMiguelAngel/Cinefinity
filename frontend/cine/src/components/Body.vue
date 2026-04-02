<template>
    <form action="127.0.0.1/8000/Movies/add" method="POST">
        <p>Título</p>
        <input type="text" v-model="title">
        <p>Género</p>
        <input type="text" v-model="genre">
        <p>Duración</p>
        <input type="time" v-model="duration">
        <input type="submit" value="Submit">
    </form>
</template>
<script setup>
</script>

<style scoped>
</style>