import { defineStore } from "pinia";
import { ref } from "vue";
import { getAvailableSpots, makeReservation, getReservations } from "@/services/parking-service";
import type { ParkingSpot, ParkingSpotResponse, ParkingSpotAvailability, MapResponse, Reservation, ReservationMakeResponse, ReservationSearchResponse } from "@/services/types";

export const useParkingStore = defineStore("parking", () => {
    const currentPrice = ref(20);
    const duration = ref(2);
    const reservationStatus = ref<ReservationMakeResponse>({ success: true, resID: Math.floor(100000 + Math.random() * 900000) });
    const reservationSearchResult = ref<ReservationSearchResponse>();
    const reservationSearchStatus = ref(false);
    const spots = ref<ParkingSpot[]>([]);
    const selectedSpot = ref<ParkingSpot>();
    const loading = ref(false);
    const reservationCountdown = ref(0);
    let pollingInterval: ReturnType<typeof setInterval> | null = null;
    let countdownInterval: ReturnType<typeof setInterval> | null = null;

    // Called once upon first load to load map onto the UI
    async function loadSpots() {
        try {
            loading.value = true;
            const response = await fetch("/parking-spots.json");
            const data: MapResponse = await response.json();
            spots.value = data.spots;
            await fetchAvailability(1);
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
            console.log(parsed);

            const availableSpotIds = new Set(parsed.spots.map(spot => spot.spotID));

            spots.value.forEach(spot => {
                spot.is_available = availableSpotIds.has(spot.id);
            });

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
        try {
            const result = await makeReservation(lotId, spotId, plateNum, paymentInfo, datetime, duration, price);
            setReservationStatus(result);
            if(result.success) {
                reservationSearchStatus.value = false;
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
        try {
            const result = await getReservations(plateNum, reserveId);
            const parsed: ReservationSearchResponse = JSON.parse(result);
            setReservationResult(parsed);
            if(parsed.reservations.length > 0 ) {
                reservationSearchStatus.value = true;
                startCountdownPoll(plateNum, reserveId);
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

    async function startCountdownPoll(plateNum: string, resID: number) {
        countdownInterval = setInterval(async () => {
            try {
                const result = await getReservations(plateNum, resID);
                const parsed: ReservationSearchResponse = JSON.parse(result);
                if (parsed.reservations.length > 0) {
                    const res = parsed.reservations[0];
                    const timeLeft = res?.timeRemainingSeconds;

                    if (timeLeft !== undefined && timeLeft <= 0) {
                        reservationSearchStatus.value = false;
                        clearUserBookingData();
                        clearInterval(countdownInterval ?? 0);
                        countdownInterval = null;
                        reservationCountdown.value = 0;
                    } else {
                        reservationCountdown.value = timeLeft ?? 0;
                    }
                }
            } catch (error) {
                console.error("Failed to poll countdown: ", error);
            }
        }, 1000);
    }

    function stopCountdownPoll() {
        if (countdownInterval) {
            clearInterval(countdownInterval);
            countdownInterval = null;
        }
        reservationCountdown.value = 0;
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
        reservationCountdown,
        startCountdownPoll,
        stopCountdownPoll,
    };
});