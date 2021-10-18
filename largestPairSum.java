/*
Given an array of integers, return the pair of values that will
result in the largest sum.
*/public class Solution{
	public static int largestPairSum(int[] numbers){
        int index = 2;
        int larger = 0;
        int large = 0;
        if (numbers[0] > numbers [1]) {
        	larger = numbers[0];
        	large = numbers[1];
        } else {
        	larger = numbers[1];
        	large = numbers[0];
        }
        while (index < numbers.length) {
        	int testValue = numbers[index];
        	if (testValue > larger) {
        		if (testValue > large) {
        			large = larger;
        			larger = testValue;
        		} else {
        			larger = large;
        			large = testValue;
        		}
        	} else if (testValue > large) {
        		large = testValue;
        	} index++;
        } return large + larger;
    } public static void main(String[] args) {
    	int[] test = {5,6,7,1,2,3,8,9,0,10};
		System.out.println(largestPairSum(test));

	}
}
