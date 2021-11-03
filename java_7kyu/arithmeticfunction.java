//Write a function that does arithmetic with
//The appropriate parameters
class ArithmeticFunction {
  public static int arithmetic(int a, int b, String operator) {
    int value = 0;
    if (operator == "add"){
        value = a + b;
    } else if (operator == "subtract"){
        value = a - b;
    } else if (operator == "multiply"){
        value = a * b;
    } else if (operator == "divide"){
        value = a / b;
    } return value; 
  }
}