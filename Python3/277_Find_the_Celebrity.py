# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    # O(n)
    def findCelebrity(self, n: int) -> int:
        a = 0
        for i in range(1, n):
            if knows(a, i):
                a = i
        # verify
        for i in range(n):
            if i != a and (knows(a, i) or not knows(i, a)):
                return -1
        return a