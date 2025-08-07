class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        # Pair up each car's position and speed
        cars = zip(position, speed)
        # Sort cars by position in descending order (closer to the target first)
        cars_sort = sorted(cars, reverse=True)
        for p, s in cars_sort:
            time = (target - p) / s
            # If the current car takes longer to reach, it starts a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)
        # The number of fleets is the length of the stack
        return len(stack)
