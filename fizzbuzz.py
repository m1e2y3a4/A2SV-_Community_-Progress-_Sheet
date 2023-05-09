class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for x in range(1, n+1):
            temp = ''
            if x % 3 == 0:
                temp += 'Fizz'
            if x % 5 == 0:
                temp += 'Buzz'
            if not temp:
                temp = str(x)
            result.append(temp)
        return result
