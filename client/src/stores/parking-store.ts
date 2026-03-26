import { defineStore } from "pinia";
import { ref } from "vue";
import { getAvailableSpots, makeReservation } from "@/services/parking-service";
import type { ParkingSpot, ParkingSpotResponse } from "@/services/types";

export const useParkingStore = defineStore("parking", () => {
    const currentPrice = ref(20);
    const spots = ref<ParkingSpot[]>([]);
    const selectedSpot = ref<ParkingSpot>();
    const loading = ref(false);
    let pollingInterval: ReturnType<typeof setInterval> | null = null;

    // Called once upon first load to load map onto the UI
    async function loadSpots() {
        try {
            loading.value = true;
            const response = await fetch("/parking-spots.json");
            const data: ParkingSpotResponse = await response.json();
            spots.value = data.spots;
            loading.value = false;
            // TODO: Add call to startPolling here
        } catch (error) {
            console.error("Failed to load parking spots: ", error);
        }
    }

    // Polling functions
    function startPolling(lotId: string) {
        if (pollingInterval) return;
        pollingInterval = setInterval(() => fetchAvailability(lotId), 200);
    }

    function stopPolling() {
        if(pollingInterval) {
            clearInterval(pollingInterval);
            pollingInterval = null;
        }
    }

    // Communicates with gRPC getAvailableSpots() function
    async function fetchAvailability(lotId: string) {
        try {
            const response = await getAvailableSpots(lotId, new Date().toISOString(), 1)

            // TODO: Make new type for the getAvailableSpots response and update type below to match that
            // TODO: And update the is_available checks to reflect the new type as well
            const parsed: ParkingSpotResponse = JSON.parse(response);

            parsed.spots.forEach(updatedSpot => {
                const existing = spots.value.find(s => s.id === updatedSpot.id);
                if(existing) {
                    existing.is_available = (updatedSpot.is_available as unknown as number) === 1;
                }
            })

            setCurrentPrice(parsed);
        } catch (error) {
            console.error("Failed to fetch latest parking spot details: ", error)
        }
    }

    // TODO: Update type of input param to match updated type in fetchAvailability()
    function setCurrentPrice(response: ParkingSpotResponse) {
        // TODO: Replace with actual logic to parse price from getAvailableSpots() response
        currentPrice.value = 30;
    }

    function clearUserBookingData() {
        spots.value.forEach(spot => {
            spot.booked_by_user = false;
        });
    }

    function selectParkingSpot(spotId: number) {
        selectedSpot.value = spots.value.find(s => s.id === spotId);
    }

    function clearSelectedSpot() {
        selectedSpot.value = undefined;
    }

    async function reserveSpot(spotId: number, lotId: string, uid: string, paymentInfo: string, datetime: string, duration: string) {
        clearUserBookingData();

        // TODO: Ensure code below properly connects to the makeReservation call
        try {
            const result = await makeReservation(String(spotId), lotId, uid, paymentInfo, datetime, duration);
            if(result.success) {
                const targetSpot = spots.value.find(s => s.id === spotId);
                if (targetSpot) {
                    targetSpot.booked_by_user = true;
                } else {
                    console.warn(`Spot #${spotId} not found.`);
                }
                clearSelectedSpot();
            }
            else {
                // TODO: Add logic here
            }
        } catch (error) {
            console.error("Failed to make a reservation: ", error);
        }

        
    }

    function lookUpReservation(reserveId: number, name: string) {
        clearUserBookingData();

        // TODO: Add logic to make call to gRPC look up reservation function (when added)
        // TODO: Add logic to update booked_by_user value for the reserved spot if it exists
        // TODO: Add return value to indicate if lookup was successful or not
    }

    return {
        currentPrice,
        spots,
        selectedSpot,
        loadSpots,
        fetchAvailability,
        startPolling,
        stopPolling,
        setCurrentPrice,
        selectParkingSpot,
        clearSelectedSpot,
        clearUserBookingData,
        reserveSpot,
        lookUpReservation,
    };
});