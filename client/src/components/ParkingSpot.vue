<script setup lang="ts">
    import { ref, computed, watch } from "vue";
    import type { ParkingSpot } from "@/services/types";
    import { useParkingStore } from "@/stores/parking-store";
    
    const parkingStore = useParkingStore();
    const isSelected = ref(false);

    const props = defineProps<{
        spot: ParkingSpot;
    }>();

    const gridPosition = computed(() => ({
        gridColumn: props.spot.col,
        gridRow: props.spot.row
    }));

    const orientationClasses = computed(() => {
        switch (props.spot.orientation) {
            case "N":
                return "h-22 w-22 border-t-0";
            case "S":
                return "h-22 w-22 border-b-0";
            case "E":
                return "h-22 w-22 border-r-0";
            case "W":
                return "h-22 w-22 border-l-0";
            default:
                return "";
        }
    });

    const colourClasses = computed(() => {
        if (props.spot.booked_by_user) return "border-slate-500 text-slate-500";
        if (!props.spot.is_available) return "border-gray-300 text-gray-300 cursor-not-allowed";
        if(isSelected.value) return "border-blue-600 text-blue-600 hover:border-blue-600 cursor-pointer";
        return "border-lime-500 text-lime-500 hover:border-blue-400 hover:text-blue-400 cursor-pointer";
    });

    // update selectedSpot when new spot is selected
    watch(
        () => parkingStore.selectedSpot,
        (newSelectedSpot) => {
            isSelected.value = newSelectedSpot?.id === props.spot.id;
        }
    );

    const selectSpot = () => {
        if (isSelected.value) {
            parkingStore.clearSelectedSpot();
        } else {
            parkingStore.selectParkingSpot(props.spot.id);
        }
    }
</script>

<template>
    <button
        :style="gridPosition"
        @click="selectSpot"
        class="relative m-3 ml-0.5 flex items-center justify-center font-bold text-xl font-chakra border-4"
        :class="[orientationClasses, colourClasses]"
    >
        {{ spot.id }}

        <div 
            v-if="props.spot.booked_by_user" 
            class="absolute bottom-0 w-full text-center text-xs tracking-tighter leading-none p-2 text-slate-400"
        >
            You are here
        </div>
    </button>
</template>