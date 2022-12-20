package com.mariopavlov;

public class ArraySum {

    public long calculateSum(int[] array) {
        long sum = 0;

        for (int item : array) {
            sum += item;
        }

        return sum;
    }

    // Implementing Divide and Conquer Algorithm
    public long calculateRecursive(int[] array, int low, int high) {
        if (low == high) {
            return array[low];
        } else if (low > high) {
            return 0;
        } else {
            int mid = (high + low) / 2;
            return calculateRecursive(array, low, mid) + calculateRecursive(array, mid + 1, high);
        }
    }

}
