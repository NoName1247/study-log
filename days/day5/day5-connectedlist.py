class Solution:

    def intt(self,s: str) -> int:
        char_to_digit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,'5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        result = 0
        for char in s:
            result = result * 10 + char_to_digit[char]        
        return result

    def strr(self, n: int) -> str:
        if n == 0:
            return "0"
        digit_to_char = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
        result = ""
        while n > 0:
            last_digit = n % 10
            result = digit_to_char[last_digit] + result
            n = n // 10        
        return result

    def multiply(self, num1: str, num2: str) -> str:
        if self.intt(num1)==0 or self.intt(num2)==0:
            return '0'
        first = [self.intt(i) for i in num1][::-1]
        sec = [self.intt(i) for i in num2][::-1]
        summ = {}
        for a in range(len(first)):
            for b in range(len(sec)):
                summ[a+b] = summ.get(a+b,0) + (first[a]*sec[b])
        
        for i in range(len(summ)-1):
            summ[i+1] = summ[i+1] + (summ[i]//10)
            summ[i] = summ[i]%10
        ans = ''
        for i in range(len(summ)):

            ans = self.strr(summ[i])+ ans
        

        return ans     