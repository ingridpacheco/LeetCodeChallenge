class UndergroundSystem:

    def __init__(self):
        self.travels = {}
        self.travel_time = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.travels[id] = [stationName,t]        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_place, start_time = self.travels[id]
        dif_time = t - start_time
        if start_place in self.travel_time:
            if stationName in self.travel_time[start_place]:
                self.travel_time[start_place][stationName].append(dif_time)
            else:
                self.travel_time[start_place][stationName] = [dif_time]
        else:
            self.travel_time[start_place] = {}
            self.travel_time[start_place][stationName] = [dif_time]
            
        del self.travels[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travels = self.travel_time[startStation][endStation]
        
        return sum(travels) / len(travels)

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)