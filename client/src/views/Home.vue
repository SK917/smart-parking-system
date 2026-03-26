<script setup lang="ts">
    import { onMounted, onUnmounted } from 'vue';
    import { useParkingStore } from '@/stores/parking-store';
    import ParkingLot from '@/components/ParkingLot.vue';
    import TopPanel from '@/components/TopPanel.vue';

    const parkingStore = useParkingStore();

    onMounted(() => {
        parkingStore.loadSpots();
    });

    onUnmounted(() => {
        parkingStore.stopPolling();
    })

</script>

<template>
    <div class="m-4 flex flex-col items-start">
        <TopPanel/>
        <ParkingLot/>
    </div>
</template>