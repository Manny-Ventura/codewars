//Write a function that will remove vowels from a string.

public class Troll {
	public static String disemvowel(String str) {
		char character;
		String finalString = "";
		String vowels = "";
		for (int i = 0; i < str.length(); i++) {
			character = str.toLowerCase().charAt(i);
			if (character == 'a' || character == 'e' || character == 'i' || character == 'o' || character == 'u') {
				vowels += String.valueOf(str.charAt(i));
			}
			else {
			finalString += String.valueOf(str.charAt(i));
			}
		}
		return finalString;
	}
}