import { defineStore } from "pinia";
import { ref } from "vue";
import type { ParkingSpot, ParkingSpotResponse } from "@/services/types";

export const useParkingStore = defineStore("parking", () => {
    const currentPrice = ref(20);
    const spots = ref<ParkingSpot[]>([]);

    async function loadSpots() {
        try {
            const response = await fetch("/parking-spots.json");
            const data: ParkingSpotResponse = await response.json();
            spots.value = data.spots;
        } catch (error) {
            console.error("Failed to load parking spots:", error);
        }
    }

    function getCurrentPrice() {
        currentPrice.value = 30;
    }

    function clearUserBookingData() {
        spots.value.forEach(spot => {
            spot.booked_by_user = false;
        });
    }

    function reserveSpot(spotId: number) {
        clearUserBookingData();

        const targetSpot = spots.value.find(s => s.id === spotId);
        if (targetSpot) {
            targetSpot.booked_by_user = true;
        } else {
            console.warn(`Spot #${spotId} not found.`);
        }
    }

    return {
        currentPrice,
        spots,
        loadSpots,
        getCurrentPrice,
        clearUserBookingData,
        reserveSpot,
    };
});