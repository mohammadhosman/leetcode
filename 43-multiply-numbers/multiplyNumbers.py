class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        int1 = 0
        int2 = 0
        for char in num1:
            temp = int(char)
            int1 += temp
            int1 *= 10
        int1 = int1 // 10
        prod1 = int(int1)

        for char in num2:
            temp = int(char)
            int2 += temp
            int2 *= 10
        int2 = int2 // 10
        prod2 = int(int2)

        new_num = int(prod1 * prod2)
        answer = str(new_num)
        return answer