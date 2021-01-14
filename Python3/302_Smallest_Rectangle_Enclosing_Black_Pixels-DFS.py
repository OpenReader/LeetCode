class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        m = len(image)
        if m == 0:
            return 0
        n = len(image[0])
        if n == 0:
            return 0
        top, bottom, left, right = x, x, y, y
        
        sk = [(x, y),]
        image[x][y] = '0'
        while sk:
            cur = sk.pop()
            i, j = cur[0], cur[1]
            # up
            if i-1 >= 0 and image[i-1][j] == '1':
                sk.append((i-1, j))
                image[i-1][j] = '0'
                top = min(top, i-1)
            # dowm
            if i+1 < m and image[i+1][j] == '1':
                sk.append((i+1, j))
                image[i+1][j] = '0'
                bottom = max(bottom, i+1)
            # right
            if j+1 < n and image[i][j+1] == '1':
                sk.append((i, j+1))
                image[i][j+1] = '0'
                right = max(right, j+1)
            # left
            if j-1 >= 0 and image[i][j-1] == '1':
                sk.append((i, j-1))
                image[i][j-1] = '0'
                left = min(left, j-1)
        
        return (bottom - top + 1) * (right - left + 1)