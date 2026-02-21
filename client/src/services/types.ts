export interface ParkingSpot {
    id: number
    row: number
    col: number
    orientation: 'N' | 'E' | 'S' | 'W'
    is_available: boolean
    booked_by_user: boolean
}

export interface ParkingSpotResponse {
    spots: ParkingSpot[]
}