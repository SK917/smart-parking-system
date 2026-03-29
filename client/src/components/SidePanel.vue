<script setup lang="ts">
    import { ref, computed, watch } from 'vue';
    import ReservationForm from './ReservationForm.vue';
    import { useParkingStore } from '@/stores/parking-store';
    import { ChevronDown, ChevronUp } from 'lucide-vue-next';

    const parkingStore = useParkingStore();
    const showReservationForm = ref(false);
    const reservePlateNum = ref('');
    const reserveId = ref<number | null>(null);
    const durationInput = ref(parkingStore.duration);

    const toggleReservationForm = () => {
        showReservationForm.value = !showReservationForm.value;
    }

    const lookUpReservation = () => {
        if (reserveId.value === null || isNaN(reserveId.value)) {
            reserveId.value = null;
            return;
        }
        parkingStore.lookUpReservation(reserveId.value ?? 0, reservePlateNum.value);
        reservePlateNum.value = '';
        reserveId.value = null;
    }

    const isFormInvalid = computed(() => {
        return reservePlateNum.value.trim() === '' || reserveId.value === null
    })

    watch(durationInput, (newDuration) => {
        if (newDuration) {
            if(newDuration < 1) {
                durationInput.value = 1;
            }
            else if(newDuration > 24) {
                durationInput.value = 24;
            }
            else {
                parkingStore.setDuration(newDuration);
            }
        }
    });

</script>

<template>
    <div class="bg-gray-200 font-chakra flex flex-col gap-15 h-screen overflow-y-auto side-scroll">
        <div>
            <div class="text-md pr-4 pl-4 pt-4 pb-2 text-red-600 font-semibold">
                Welcome to
            </div>
            <div class="text-3xl pr-4 pl-4 pb-3 font-bold">
                Smart Parking Management
            </div>
            <div class="w-full h-1 bg-gray-500">
            </div>
        </div>
            
        <div class="flex flex-col p-4 gap-4">
            <div class="text-md text-red-600 font-semibold">
                <p>The price represents the number of 1-hour blocks below.</p>
            </div>
            <div class="flex flex-row gap-2 items-end">
                <div class="relative flex items-center bg-gray-200 border border-gray-700 rounded-sm min-h-9 group w-20 outline-2 outline-transparent
                    has-[:focus]:outline-red-500 hover:not-has-[:focus]:outline-red-300 focus-within:outline-yellow-600 transition-all">
                    <input 
                        type="number" 
                        v-model.number="durationInput"
                        min="1" 
                        max="24" 
                        step="1"
                        class="bg-transparent text-gray-700 h-full w-16 focus:outline-none font-orbit no-spinner pl-2 text-md"
                    />
                    <div class="flex flex-col border-0 h-full w-6">
                        <button 
                            @click="durationInput = Math.min(24, +(durationInput + 1))"
                            class="flex items-center justify-center flex-1 hover:bg-gray-300 text-gray-400 hover:text-red-500"
                        >
                            <ChevronUp :size="16"/>
                        </button>
                        <button 
                            @click="durationInput = Math.max(1, +(durationInput - 1))"
                            class="flex items-center justify-center flex-1 hover:bg-gray-300 text-gray-400 hover:text-red-500"
                        >
                            <ChevronDown :size="16"/>
                        </button>
                    </div>
                </div>
                <div class="text-md text-gray-700 font-semibold">
                    hour blocks
                </div>
            </div>
            <div class="text-md text-red-600 font-semibold pt-4">
                <p>Want to reserve a spot?</p>
                <p>Click the button below to get started.</p>
            </div>
            <button 
                @click="toggleReservationForm"
                class="cursor-pointer text-center w-full bg-gray-700 text-white rounded-md p-1 hover:outline-red-300 hover:outline-2 focus:outline-red-500 focus:outline-2"
            >
                {{ showReservationForm ? 'Cancel' : 'Reserve a Spot'}}
            </button>
            <div
                v-show="showReservationForm"
            >
                <ReservationForm/>
            </div>
            <div class="pt-2 text-xs text-gray-500">
                <p>Note: By reserving a spot, you agree that you will show up right away.</p>
                <p>
                    Failure to do so will have your reservation 
                    <span class="text-red-400 font-bold">revoked</span>.
                </p>
            </div>
        </div>
        <div class="flex flex-col p-4 gap-4">
            <div class="text-md text-red-600 font-semibold">
                <p>Need to check your reservation?</p>
                <p>Enter your license plate number and reservation ID below.</p>
            </div>
            <input
                v-model="reservePlateNum"
                class="border bg-gray-100 outline-0 border-gray-700 p-1 rounded-md focus:outline-red-500 focus:outline-2 hover:outline-red-300 hover:outline-2"
                placeholder="License Plate"
            />
            <input
                v-model="reserveId"
                class="border bg-gray-100 outline-0 border-gray-700 p-1 rounded-md focus:outline-red-500 focus:outline-2 hover:outline-red-300 hover:outline-2"
                placeholder="Reservation ID"
            />
            <button
                :disabled="isFormInvalid" 
                @click="lookUpReservation"
                class="cursor-pointer text-center w-full bg-gray-700 text-white rounded-md p-1 hover:outline-red-300 hover:outline-2 focus:outline-red-500 focus:outline-2 disabled:opacity-50 disabled:cursor-not-allowed"
            >
                Submit
            </button>
            <div v-if="parkingStore.reservationSearchStatus">
                <div class="text-md text-red-600 font-semibold">
                    Welcome back! You have a spot booked with license plate #{{ parkingStore.reservationSearchResult?.plateNum }}.
                </div>
                <div class="text-xs text-gray-500">
                    <p>Your reservation details are below.</p>
                </div>
                <div class="text=lg text-gray-700 pt-2">
                    Spot Number: <span class="font-bold">{{ parkingStore.reservationSearchResult?.reservations[0]?.spotID }}</span>
                </div>
                <div class="text=lg text-gray-700">
                    Price Paid: $<span class="font-bold">{{ parkingStore.reservationSearchResult?.reservations[0]?.totalPayment }}</span>
                </div>
                <div class="text=lg text-gray-700">
                    Reservation Made For: <span class="font-bold">{{ parkingStore.reservationSearchResult?.reservations[0]?.startDateTime }}</span>
                </div>
                <div class="text=lg text-red-600">
                    Duration: <span class="font-bold">{{ parkingStore.reservationSearchResult?.reservations[0]?.duration }}</span> minutes.
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
    /* Chrome, Edge, Safari */
    .side-scroll::-webkit-scrollbar {
        width: 8px;
    }

    .side-scroll::-webkit-scrollbar-track {
        background: #d1d5db; /* gray-300 */
    }

    .side-scroll::-webkit-scrollbar-thumb {
        background-color: #9ca3af; /* gray-400 */
        border-radius: 6px;
        border: 2px solid #d1d5db; 
    }

    .side-scroll::-webkit-scrollbar-thumb:hover {
        background-color: #6b7280; /* gray-500 */
    }

    /* Firefox */
    .side-scroll {
        scrollbar-width: thin;
        /* thumb color | track color */
        scrollbar-color: #9ca3af #d1d5db;
    }
</style>