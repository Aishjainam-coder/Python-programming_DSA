from typing import List

class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        x, y = 0, 0  # Starting position of the snake

        # Direction mappings
        direction_map = {
            "UP": (-1, 0),   # Move up (decrease row index)
            "DOWN": (1, 0),  # Move down (increase row index)
            "LEFT": (0, -1),  # Move left (decrease column index)
            "RIGHT": (0, 1)   # Move right (increase column index)
        }

        # Process each command
        for command in commands:
            dx, dy = direction_map[command]
            x += dx
            y += dy

        # Return the final position as a single integer
        return x * n + y  # Convert the (row, column) to a single index

