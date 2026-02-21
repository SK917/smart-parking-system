<script setup lang="ts">
import { ref, computed } from 'vue';
import ReservationForm from './ReservationForm.vue';

const showReservationForm = ref(false);
const reserveName = ref('');
const reserveNum = ref('');

const toggleReservationForm = () => {
    showReservationForm.value = !showReservationForm.value;
}

const isFormInvalid = computed(() => {
  return reserveName.value.trim() === '' || reserveNum.value.trim() === ''
})

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
                v-if="showReservationForm"
            >
                <ReservationForm/>
            </div>
            <div class="pt-2 text-xs text-gray-500">
                <p>Note: By reserving a spot, you agree that you will show up within 20 minutes of booking.</p>
                <p>
                    Failure to do so will have your reservation 
                    <span class="text-red-400 font-bold">revoked</span>.
                </p>
            </div>
        </div>
        <div class="flex flex-col p-4 gap-4">
            <div class="text-md text-red-600 font-semibold">
                <p>Need to check your reservation?</p>
                <p>Enter your name and reservation number below.</p>
            </div>
            <input
                v-model="reserveName"
                class="border bg-gray-100 outline-0 border-gray-700 p-1 rounded-md focus:outline-red-500 focus:outline-2 hover:outline-red-300 hover:outline-2"
                placeholder="Name"
            />
            <input
                v-model="reserveNum"
                class="border bg-gray-100 outline-0 border-gray-700 p-1 rounded-md focus:outline-red-500 focus:outline-2 hover:outline-red-300 hover:outline-2"
                placeholder="Reservation Number"
            />
            <button
                :disabled="isFormInvalid" 
                class="cursor-pointer text-center w-full bg-gray-700 text-white rounded-md p-1 hover:outline-red-300 hover:outline-2 focus:outline-red-500 focus:outline-2 disabled:opacity-50 disabled:cursor-not-allowed"
            >
                Submit
            </button>
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