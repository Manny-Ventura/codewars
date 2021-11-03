import java.util.ArrayList;

public class Palindromes {
    public static int longestPalindrome(final String s) {
        String[] splits = s.split(" ");
        ArrayList<String> palindromes = new ArrayList<String>();
    	for (String st : splits) {
    		int start = 0;
    		int finish = st.length() - 1;
    		boolean palindrome = true;
        	while (start < st.length() - 1) {
        		if (splits[start] != splits[finish]) {
        			palindrome = false;
        		} start++;
        		finish--;
        	} if (palindrome == true) {
        		palindromes.add(st);
        	}
        } //end for loop , end checking each word in String
    	System.out.println(palindromes);
    	return 1;
    }
    public static void main(String[] args) {
    	System.out.println(longestPalindrome("racecars are the best"));
    }
}