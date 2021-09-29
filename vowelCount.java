public class Vowels {
    public static int getCount(String str) {
      int vowelsCount = 0;
      int index = 0;
      while (index < str.length()){
          char c = str.toLowerCase().charAt(index);
          if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'){
              vowelsCount++;
          }
          index++;
      }
      return vowelsCount;
    }
  }