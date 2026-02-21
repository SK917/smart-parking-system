<script setup lang="ts">
import { ref, computed } from 'vue';

const reserveName = ref('');

const isFormInvalid = computed(() => {
  return reserveName.value.trim() === ''
})
</script>

<template>
    <div class="font-chakra flex flex-col gap-4">
        <input
            v-model="reserveName"
            class="border bg-gray-100 outline-0 border-gray-700 p-1 rounded-md focus:outline-red-500 focus:outline-2 hover:outline-red-300 hover:outline-2"
            placeholder="Name"
        />
        <div class="font-md">
            Current price: $<span class="font-bold">30</span>
            <div class="pt-1 text-xs text-gray-500">
                <p>Reserving a spot now locks in the above price. Click "Submit" to proceed with the reservation.</p>
            </div>
        </div>
        <button
            :disabled="isFormInvalid" 
            class="cursor-pointer text-center w-full bg-gray-700 text-white rounded-md p-1 hover:outline-red-300 hover:outline-2 focus:outline-red-500 focus:outline-2 disabled:opacity-50 disabled:cursor-not-allowed"
        >
            Submit
        </button>
    </div>
</template>