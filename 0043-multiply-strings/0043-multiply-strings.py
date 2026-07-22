class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        result_array = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):

                int1 = int(num1[i])
                int2 = int(num2[j])
                product = int1 * int2
                tens = product // 10
                ones = product % 10 

                result_array[i + j] += tens
                result_array[i+j+1] += ones
        carry = 0 
        for k in range(len(result_array) - 1, -1, -1):
            total = result_array[k] + carry
            result_array[k] = total % 10
            carry = total // 10
        
        final_string = ""
        # iterate and get the final number
        for l in range(len(result_array)):
            if l == 0 and result_array[l] == 0:
                pass
            else:
                my_string = str(result_array[l])
                final_string = final_string + my_string 
        return final_string

        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna