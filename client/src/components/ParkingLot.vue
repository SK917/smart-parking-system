<script setup lang="ts">
    import { useParkingStore } from "@/stores/parking-store";
    import ParkingSpot from "./ParkingSpot.vue";

    const parkingStore = useParkingStore();

</script>

<template>
    <div
        class="grid gap-0 p-2 grid-rows-6 grid-cols-12"
    >
        <ParkingSpot
            v-for="spot in parkingStore.spots"
            :key="spot.id"
            :spot="spot"
        />
    </div>
</template>