public class Kata {

    public static String encrypt(final String text, final int n) {
        int index = 0;
        String finalString = "";
        char odd = text.charAt(index);
        index++;
        char even = text.charAt(index);
        while (n != 0){
            finalString += String.valueOf(odd);
            finalString += String.valueOf(even);

            index++;
            odd = text.charAt(index);
            index++;
            even = text.charAt(index);
            n--;
        }
        return null;   
    }
    
    public static String decrypt(final String encryptedText, final int n) {
        // Your code here
        return null;
    }
    
  }