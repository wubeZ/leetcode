class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flightLabels = [0] * (n+2)
        
        for i in range(len(bookings)):
            flightLabels[bookings[i][0]] += bookings[i][2]
            flightLabels[bookings[i][1]+1] += -(bookings[i][2])
    
        prefixSum = [0] * (n+1)
        
        for i in range(n+1):
            prefixSum[i] = prefixSum[i-1] + flightLabels[i]
        
        return prefixSum[1:]