package com.mariopavlov.strategies;

import com.mariopavlov.interfaces.CalculateStrategy;

// Implements Divide and Conquer algorithm to calculate Array sum
public class RecursiveStrategy implements CalculateStrategy {

    private final int low;
    private final int high;
    private final int[] array;

    public RecursiveStrategy(int[] array, int low, int high) {
        this.array = array;
        this.low = low;
        this.high = high;
    }

    @Override
    public long sum() {
        if (low == high) {
            return array[low];
        } else if (low > high) {
            return 0;
        } else {
            int mid = (high + low) / 2;
            RecursiveStrategy lowerHalf = new RecursiveStrategy(array, low, mid);
            RecursiveStrategy upperHalf = new RecursiveStrategy(array, mid + 1, high);
            return lowerHalf.sum() + upperHalf.sum();
        }
    }
}
