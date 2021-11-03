/*
We want to generate a function that computes the series 
starting from 0 and ending until the given number.
Ex Input: 6
Output: "0+1+2+3+4+5+6=21"

*/

public class SequenceSum{

  public static String showSequence(int value){
    if (value < 0){
      String string = String.valueOf(value);
      return string += "<0";
    } else if (value == 0){
      return "0=0";
    }
    String finalString ="0+";
    int finalValue = 0;
    int index = 1;
    if (value >= 0){
     while (index <= value){
      finalString += String.valueOf(index);
      if (index < value){
        finalString += "+";
      }
       
      finalValue += index;
       index++;
     } finalString += " = ";
      finalString += String.valueOf(finalValue);
   } return finalString;
  }

  /*public static void main(String args[]){
    int param=Integer.ParseInt(args[0]);
    SequenceSum.showSequence(param);
  }*/
}