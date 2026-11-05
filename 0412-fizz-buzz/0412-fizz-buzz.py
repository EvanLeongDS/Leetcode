class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        

        # RETURN a list, don't print
        return_list = []

        for i in range(1, n + 1):
            print(i)
            if i % 3 == 0 and i % 5 == 0: 
                return_list.append("FizzBuzz")
            elif i % 3 == 0:
                return_list.append("Fizz")
            elif i % 5 == 0:
                return_list.append("Buzz")
            else:
                i = str(i)
                return_list.append(i)
        return return_list