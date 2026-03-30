<script setup lang="ts">
    import { ref, computed } from 'vue';
    import { useParkingStore } from '@/stores/parking-store';
    import ReservationPopup from './ReservationPopup.vue';

    const reservePlateNum = ref('');
    const parkingStore = useParkingStore();
    const showPopup = ref(false);

    const handleSubmit = () => {
        parkingStore.reserveSpot(parkingStore.selectedSpot?.id ?? 0, 1, reservePlateNum.value, "Paid", formatDateTime(new Date()), parkingStore.duration, parkingStore.currentPrice);
        showPopup.value = true;
    };

    const handleConfirm = () => {
        showPopup.value = false;
        parkingStore.clearSelectedSpot();
        reservePlateNum.value = '';
    };

    const isFormInvalid = computed(() => {
        return reservePlateNum.value.trim() === '' || parkingStore.selectedSpot === undefined;
    });

    const formattedPrice = computed(() => {
        return parkingStore.currentPrice ? parkingStore.currentPrice.toFixed(2) : '0.00';
    });

    const formatDateTime = (date: Date): string => {
        const dd = String(date.getDate()).padStart(2, '0');
        const mm = String(date.getMonth() + 1).padStart(2, '0');
        const yyyy = date.getFullYear();
        const hh = String(date.getHours()).padStart(2, '0');
        const min = String(date.getMinutes()).padStart(2, '0');
        const ss = String(date.getSeconds()).padStart(2, '0');
        return `${yyyy}-${mm}-${dd} ${hh}:${min}:${ss}`;
    };
</script>

<template>
    <div class="font-chakra flex flex-col gap-4">
        <input
            v-model="reservePlateNum"
            class="border bg-gray-100 outline-0 border-gray-700 p-1 rounded-md focus:outline-red-500 focus:outline-2 hover:outline-red-300 hover:outline-2"
            placeholder="License Plate"
        />
        <div class="font-md">
            <div class="text-xs text-gray-500">
                <p>Click on a parking spot from the map to select it.</p>
            </div>
            <div>
                Selected Spot: <span class="font-bold">{{ parkingStore.selectedSpot?.id ?? 'None' }}</span>
            </div>
            <div class="pt-2">
                Selected Stay: <span class="font-bold">{{ parkingStore.duration }}</span> hour(s)
            </div>
            <div class="pt-2">
                Current price: $<span class="font-bold">{{ formattedPrice }}</span>
            </div>
            <div class="text-xs text-gray-500">
                <p>Reserving a spot starts right away. You will have 2 minutes to get there before it is released.</p>
            </div>
        </div>
        <button
            :disabled="isFormInvalid" 
            @click="handleSubmit"
            class="cursor-pointer text-center w-full bg-gray-700 text-white rounded-md p-1 hover:outline-red-300 hover:outline-2 focus:outline-red-500 focus:outline-2 disabled:opacity-50 disabled:cursor-not-allowed"
        >
            Submit
        </button>
        <ReservationPopup
            :is-open="showPopup"
            :reservation-id="parkingStore.reservationStatus.resID"
            :spot-num="parkingStore.selectedSpot?.id ?? 0"
            @confirm="handleConfirm"
        />
    </div>
</template>