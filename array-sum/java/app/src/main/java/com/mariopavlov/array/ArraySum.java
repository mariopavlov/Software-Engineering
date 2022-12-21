package com.mariopavlov.array;

import com.mariopavlov.interfaces.CalculateStrategy;

public class ArraySum {
    public long calculateSum(CalculateStrategy strategy) {
        return strategy.sum();
    }
}
