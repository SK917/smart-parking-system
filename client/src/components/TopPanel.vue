<script setup lang="ts">
    import { computed } from 'vue';
    import { useParkingStore } from '@/stores/parking-store';
    import LegendItem from './LegendItem.vue';

    const parkingStore = useParkingStore();

    const formattedPrice = computed(() => {
        return parkingStore.currentPrice ? parkingStore.currentPrice.toFixed(2) : '0.00';
    });

</script>

<template>
    <div class="p-4 bg-white font-chakra flex flex-row justify-between w-full">
        <div class="flex flex-row items-center gap-2">
            <div class="font-bold text-gray-600 text-lg">
                Current Price: 
            </div>
            <div class="font-bold text-3xl">
                <span class="text-gray-400">
                    $
                </span>
                <span class="text-red-600">
                    {{ formattedPrice }}
                </span>
            </div>
            <div class="text-md text-gray-400">
                for <span class="text-gray-600 font-bold">{{ parkingStore.duration }}</span> hour(s)
            </div>
            
        </div>
        <div class="flex flex-row gap-6 ">
            <LegendItem :colour-select="0" label="Available"/>
            <LegendItem :colour-select="3" label="Selected"/>
            <LegendItem :colour-select="2" label="Reserved"/>
            <LegendItem :colour-select="1" label="Reserved By You"/>
        </div>
    </div>
</template>