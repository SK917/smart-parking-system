import { defineStore } from "pinia";
import { ref } from "vue";
import { getAvailableSpots, makeReservation, getReservations } from "@/services/parking-service";
import type { ParkingSpot, ParkingSpotResponse, ParkingSpotAvailability, MapResponse, Reservation, ReservationMakeResponse, ReservationSearchResponse } from "@/services/types";

export const useParkingStore = defineStore("parking", () => {
    const currentPrice = ref(20);
    const duration = ref(120);
    const reservationStatus = ref<ReservationMakeResponse>({ success: true, resID: Math.floor(100000 + Math.random() * 900000) });
    const reservationSearchResult = ref<ReservationSearchResponse>();
    const reservationSearchStatus = ref(false);
    const spots = ref<ParkingSpot[]>([]);
    const selectedSpot = ref<ParkingSpot>();
    const loading = ref(false);
    let pollingInterval: ReturnType<typeof setInterval> | null = null;

    // Called once upon first load to load map onto the UI
    async function loadSpots() {
        try {
            loading.value = true;
            const response = await fetch("/parking-spots.json");
            const data: MapResponse = await response.json();
            spots.value = data.spots;
            loading.value = false;
            startPolling(1)
        } catch (error) {
            console.error("Failed to load parking spots: ", error);
        }
    }

    // Polling functions
    function startPolling(lotId: number) {
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
    async function fetchAvailability(lotId: number) {
        try {
            const response = await getAvailableSpots(lotId, formatDateTime(new Date()), duration.value)
            const parsed: ParkingSpotResponse = JSON.parse(response);

            parsed.spots.forEach(updatedSpot => {
                const existing = spots.value.find(s => s.id === updatedSpot.spotID);
                if(existing) {
                    existing.is_available = !updatedSpot.occupied;
                }
            })

            setCurrentPrice(parsed);
        } catch (error) {
            console.error("Failed to fetch latest parking spot details: ", error)
        }
    }

    function formatDateTime(date: Date): string {
        const dd = String(date.getDate()).padStart(2, '0');
        const mm = String(date.getMonth() + 1).padStart(2, '0');
        const yyyy = date.getFullYear();
        const hh = String(date.getHours()).padStart(2, '0');
        const min = String(date.getMinutes()).padStart(2, '0');
        const ss = String(date.getSeconds()).padStart(2, '0');
        return `${yyyy}-${mm}-${dd} ${hh}:${min}:${ss}`;
    }

    function setCurrentPrice(response: ParkingSpotResponse) {
        currentPrice.value = response.price;
    }

    function setDuration(mins: number) {
        duration.value = mins;
    }

    function setReservationStatus(status: ReservationMakeResponse) {
        reservationStatus.value = status;
    }

    function setReservationResult(result: ReservationSearchResponse) {
        reservationSearchResult.value = result;
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

    async function reserveSpot(spotId: number, lotId: number, plateNum: string, paymentInfo: string, datetime: string, duration: number, price: number) {
        clearUserBookingData();

        // TODO: Ensure code below properly connects to the makeReservation call
        try {
            const result = await makeReservation(lotId, spotId, plateNum, paymentInfo, datetime, duration, price);
            setReservationStatus(result);
            if(result.success) {
                const targetSpot = spots.value.find(s => s.id === spotId);
                if (targetSpot) {
                    targetSpot.booked_by_user = true;
                } else {
                    console.warn(`Spot #${spotId} not found.`);
                }
            }
        } catch (error) {
            console.error("Failed to make a reservation: ", error);
        }

        
    }

    async function lookUpReservation(reserveId: number, plateNum: string) {
        clearUserBookingData();

        // TODO: Check whether below code actually works with gRPC
        try {
            const result = await getReservations(plateNum, reserveId);
            const parsed: ReservationSearchResponse = JSON.parse(result);
            setReservationResult(parsed);
            if(parsed.reservations.length > 0 ) {
                reservationSearchStatus.value = true;
                const targetSpot = spots.value.find(s => s.id === parsed.reservations[0]?.spotID );
                if (targetSpot) {
                    targetSpot.booked_by_user = true;
                } else {
                    console.warn(`Spot #${parsed.reservations[0]?.spotID} not found.`);
                }
            }
            else {
                reservationSearchStatus.value = false;
            }

        } catch (error) {
            console.error("Failed to look up reservation: ", error);
        }
    }

    return {
        currentPrice,
        spots,
        selectedSpot,
        duration,
        reservationStatus,
        reservationSearchResult,
        reservationSearchStatus,
        loadSpots,
        fetchAvailability,
        startPolling,
        stopPolling,
        setCurrentPrice,
        setDuration,
        selectParkingSpot,
        clearSelectedSpot,
        clearUserBookingData,
        reserveSpot,
        lookUpReservation,
    };
});