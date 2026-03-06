<script setup lang="ts">
    import { computed } from "vue";
    import type { ParkingSpot } from "@/services/types";

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
        if (!props.spot.is_available) return "border-gray-300 text-gray-300";
        return "border-lime-500 text-lime-500";
    });
</script>

<template>
    <div
        :style="gridPosition"
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
    </div>
</template>