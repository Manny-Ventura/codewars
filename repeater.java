//Make a function that will repeat a string n number of times

public class Repeater{
    public static String repeat(String string,long n){
        String finalString = "";
        for (int i = 0; i < n; i++){
            finalString += string;
        }
        return finalString;
    }
  }