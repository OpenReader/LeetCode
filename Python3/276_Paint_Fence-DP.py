class Solution:
    def numWays(self, n: int, k: int) -> int:
        # if previous two posts' color is different: opt[0][i] = (k - 1) * opt[0][i-1] + opt[1][i-1]
        # if previous two posts' color is the same:  opt[1][i] = (k - 1) * opt[0][i-1]
        if n == 0:
            return 0
        if n == 1:
            return k
        opt_0_pre, opt_1_pre = k, k - 1
        opt_0_cur = opt_1_cur = 0
        for i in range(1, n-1):
            opt_0_cur = (k - 1) * opt_0_pre + opt_1_pre
            opt_1_cur = (k - 1) * opt_0_pre
            opt_0_pre, opt_1_pre = opt_0_cur, opt_1_cur
        return k * opt_0_pre