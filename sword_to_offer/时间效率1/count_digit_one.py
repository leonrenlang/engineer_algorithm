
# 输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
# 例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。


class Solution(object):
    def countDigitOne(self,n):
        if n<=0: return 0

        num_s = str(n) 
        high = int(num_s[0])  
        Pow = 10**(len(num_s)-1) 
        last = n - high*Pow
        
        if high == 1:
            return self.countDigitOne(Pow-1)+self.countDigitOne(last)+last+1
        else:
            return Pow+high*self.countDigitOne(Pow-1)+self.countDigitOne(last)


