class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        sortedArr = sorted(zip(position, speed), reverse = True)
        fleetCount, fleetTime = 0, 0

        for p, s in sortedArr:

            timeLeft = (target - p) / s

            if timeLeft > fleetTime:
                fleetCount += 1
                fleetTime = timeLeft
        
        return fleetCount

