/*
There is an array with some numbers. All numbers are equal except for one. Try to find it!
Given a double arr[], write a function that will return the double that is not equal to the rest.
*/

// Make sure your class is public
public class Kata {
    public static double findUniq(double arr[]) {
		double unique = -999999999;
		double firstValue = arr[0];
		int index = 1;
		while (index < arr.length - 1){
			//have if statement being any condition in which arr[0] is not unique
			if (arr[index] != firstValue && arr[index] != arr[index -1]){
				unique = arr[index];
				break;
			}
			index++;
		} if (unique == -999999999) {
			unique = arr[0];
		}
		 return unique;
	} 
}