"""
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
"""
class Sulotion:
    def RomanToInt(self,s):
        Hadict={"I":1,"V":5,"IV":4,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000}
        n=len(s)
        Int=0
        for i in range (n):
            Int+=Hadict[s[i]]
        return Int

if __name__ == '__main__':
    s=Sulotion()
    print(s.RomanToInt(""))