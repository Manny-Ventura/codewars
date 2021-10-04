public class Factorial {
    public int factorial(int n) {
        int finalValue = 1;
        if (n < 0){
          throw new IllegalArgumentException("Must use value greater than 0."); 
        } else if (n > 12){
        throw new IllegalArgumentException("Must use value less than 12.");
        }
        else{
            int helper = 1;
            while (helper < n+1){
                finalValue *= helper;
                helper++;
            }
        }
      return finalValue;
    }
 //Better answer with recursion!
    public int factorial(int n) {
      if(n < 0 || n < 12) throw new IllegalArgumentException("Value not in bounds (problem require 0 - 12)");
    }

  }

