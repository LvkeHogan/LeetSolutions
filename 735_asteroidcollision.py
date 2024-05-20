class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        newStack = []
        for asteroid in asteroids:
            if asteroid > 0:
                newStack.append(asteroid)
            else:
                while newStack and newStack[-1] > 0 and newStack[-1] < abs(asteroid):
                    newStack.pop()
                if  not newStack or newStack[-1] < 0:
                    newStack.append(asteroid)
                elif newStack[-1] == abs(asteroid):
                    newStack.pop()
        return newStack