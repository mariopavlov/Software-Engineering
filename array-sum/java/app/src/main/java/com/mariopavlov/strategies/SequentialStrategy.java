package com.mariopavlov.strategies;

import com.mariopavlov.interfaces.CalculateStrategy;

public class SequentialStrategy implements CalculateStrategy {

    private final int[] array;

    public SequentialStrategy(int[] array) {
        this.array = array;
    }

    @Override
    public long sum() {
        long sum = 0;

        for (int item : array) {
            sum += item;
        }

        return sum;
    }
}
