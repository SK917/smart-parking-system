export interface ParkingSpot {
    id: number
    row: number
    col: number
    orientation: 'N' | 'E' | 'S' | 'W'
    is_available: boolean
    booked_by_user: boolean
}

export interface MapResponse {
    spots: ParkingSpot[]
}

export interface ParkingSpotAvailability {
    spotID: number
    lotID: number
    occupied: boolean
}

export interface ParkingSpotResponse {
    lotID: number
    totalSpots: number
    price: number
    spots: ParkingSpotAvailability[]
}

export interface Reservation { 
    resID: number
    plateNum: string
    lotID: number
    spotID: number
    startDateTime: string
    endDateTime: string
    duration: number
    totalPayment: number
    paymentStatus: "paid"
}

export interface ReservationSearchResponse {
    plateNum: string
    reservations: Reservation[];
}

export interface ReservationMakeResponse {
    success: boolean
    resID: string
}