class Solution:
    
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        res = (C - A) * (D - B) + (G - E) * (H - F)
        if (max(A, E) < min(C, G) and max(B, F) < min(D, H)):
            res -= (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))
        return res