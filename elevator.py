#!/usr/bin/env python3
import sys
import argparse

singleFloorTravelTime = 10.0

def calculateTravelTime(oneFloorTime: float, floors: list[int]) -> float:
    travelTime = 0
    previousFloor = None
    for currentFloor in floors:
        if previousFloor is not None:
            travelTime += (abs(currentFloor - previousFloor) * oneFloorTime)
        previousFloor = currentFloor
    return travelTime


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="elevator", 
            description="Simulates an elevator moving between listed floors in order provided.",
            epilog="Assumptions:  Python 3.5 or greater to execute."
            "  Floors are visited in exactly the order user provides (including duplicate floors)."
            "  Duplicate floors next to one-another do not impact total travel time."
            "  Basement floors can be simulated by entering a negative value."
            "  Starting floor is not provided in list of floors, it is a unique argument."
            "  Example usage:  elevator.py -s 12 -f 2 9 1 32")
    parser.add_argument('-t', '--single-floor-travel-time', type=float, default=singleFloorTravelTime, 
            help=f"Single floor travel time (default of {singleFloorTravelTime}, must be non-negative)")
    parser.add_argument('-s', '--starting-floor', type=int, help='Floor which elevator will start on')
    parser.add_argument('-f', '--floors', type=int, nargs='+', help='List of floors to travel to in order (not including start)')

    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    else:
        if args.single_floor_travel_time < 0:
            raise argparse.ArgumentTypeError("Input error. Single_floor_travel_time is less than 0. Please enter a non-negative value. Exiting.")
        
        args.floors.insert(0, args.starting_floor)
        time = calculateTravelTime(args.single_floor_travel_time, args.floors)
        print(f"Total Travel Time:  {time}\nFloors visited in order:  {args.floors}")
