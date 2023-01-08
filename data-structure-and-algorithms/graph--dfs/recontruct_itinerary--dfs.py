from typing import List
from collections import defaultdict

class Solution:
    def backtrack(self, 
                  origin: str, 
                  flights_taken: list[str], 
                  flightmap: dict[str, list[str]], 
                  flight_taken_matrix: dict[str, list[bool]], 
                  flights: int,
                  flight_path: list[str]):
        
        # if we've taken all flights from tickets list
        if len(flights_taken) == flights + 1:  # +1 becuase we added 'JFK' intially as starting point
            for airport in flights_taken:
                flight_path.append(airport)  # append doesn't change list reference
            return True
        
        for idx, nextOrigin in enumerate(flightmap[origin]):
            if flight_taken_matrix[origin][idx] == False:
                flights_taken.append(nextOrigin)
                flight_taken_matrix[origin][idx] = True
                
                all_paths_taken = self.backtrack(nextOrigin, flights_taken, flightmap, flight_taken_matrix, flights, flight_path)
                if all_paths_taken:
                    return True
                flights_taken.pop()
                flight_taken_matrix[origin][idx] = False
        return False
                
            
    
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # we must take all these flights
        flights: int = len(tickets)
        
        # adj matrix
        flightmap: defaultdict[str, list[str]] = defaultdict(list)
        for origin, destination in tickets:
            flightmap[origin].append(destination)
        
        
        # flighpath tracker during backtracking
        flight_taken_matrix: defaultdict[str, list[bool]] = defaultdict(list)
        for Origin, flight_list in flightmap.items():
            flight_list.sort()  # since we wil travel in lexicographical order
            flight_taken_matrix[Origin] = [False]*len(flight_list)
        
        origin: str = 'JFK'
        flights_taken: list[str] = ['JFK']
        flight_path: list[str] = []
        
        # since we're guranteed an answer per the question
        # so we don't need to check if we didn't get an answer here
        self.backtrack(origin, flights_taken, flightmap, flight_taken_matrix, flights, flight_path)
        return flight_path
    
solution = Solution()
print(solution.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))