class Solution:
    def isPalindrome(self, x: int) -> bool:
          return str(x) == str(x)[::-1]
if __name__ == '__main__':
    S=Solution()
    print(S.isPalindrome(x=363))