<script setup lang="ts">
    import { RouterView } from 'vue-router';
    import SidePanel from './components/SidePanel.vue';
</script>

<template>
    <div class="bg-gray-100 min-h-screen flex flex-row">
        <SidePanel class="basis-md"/>
        <main class="flex-1">
          <RouterView />
        </main>
    </div>
</template>

<style scoped></style>
