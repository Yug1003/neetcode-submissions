class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        lst = []

        for i in asteroids:
            while lst and i < 0 and lst[-1] > 0:
                if lst[-1] < abs(i):
                    lst.pop()
                    continue

                elif lst[-1] == abs(i):
                    lst.pop()

                break
            else:
                lst.append(i)

        return lst