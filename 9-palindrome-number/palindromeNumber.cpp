class Solution {
    public:
    int reverseNumber(int n){
        long int reversedNumber = 0;
        while (n > 0){
            reversedNumber += (n % 10);
            reversedNumber *= 10;
            n /= 10;
        }
        return reversedNumber / 10;
    }
    
    bool isPalindrome(int x){
        long int newX = x;
        long int reversedNumber = reverseNumber(newX);
        if (reversedNumber == newX)
            return true;
        else 
            return false;
    }
};