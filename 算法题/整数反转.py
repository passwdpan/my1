def reverse_better(x: int) -> int:
    y, res = abs(x), 0
    # 则其数值范围为 [−2^31,  2^31 − 1]
    boundry = (1 << 31) - 1 if x > 0 else 1 << 31
    while y != 0:
        res = res * 10 + y % 10
        if res > boundry:
            return 0
        y //= 10
    return res if x > 0 else -res
if __name__ == '__main__':
    print(reverse_better(121366588))
#
# 作者：boywithacoin_cn
# 链接：https: // leetcode - cn.com / problems / reverse - integer / solution / pythondan - chu - he - tui - ru - shu - zi - yi - chu - qian - jin - xin /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。