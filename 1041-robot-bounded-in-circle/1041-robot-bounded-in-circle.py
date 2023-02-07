class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        prev_direction = "north"
        l_direction = {"north": "west", "south": "east", "west":"south", "east": "north"}
        r_direction = {"north": "east", "south": "west", "west":"north", "east": "south"}
        start = [0,0]
        
        def moveforward(prev_direction):
            if prev_direction == "north":
                start[1] += 1
            elif prev_direction == "south":
                start[1] -= 1
            elif prev_direction == "east":
                start[0] += 1
            else:
                start[0] -= 1
        
        for command in instructions:
            if command == "G":
                moveforward(prev_direction)
            elif command == "L":
                prev_direction = l_direction[prev_direction]
            elif command == "R":
                prev_direction = r_direction[prev_direction]
        
        if prev_direction != "north" or start == [0,0]:
            return True
        
        return False
        
                