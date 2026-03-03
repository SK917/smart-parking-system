<script setup lang="ts">
    import { onMounted } from "vue";
    import { useParkingStore } from "@/stores/parking-store";
    import ParkingSpot from "./ParkingSpot.vue";

    const parkingStore = useParkingStore();

    onMounted(() => {
        parkingStore.loadSpots();
    });
</script>

<template>
    <div
        class="grid gap-6 p-8"
        :style="{
            gridTemplateColumns: 'repeat(10, 80px)',
            gridTemplateRows: 'repeat(6, 100px)'
        }"
    >
        <ParkingSpot
            v-for="spot in parkingStore.spots"
            :key="spot.id"
            :spot="spot"
        />
    </div>
</template>