/*
 * This Java source file was generated by the Gradle 'init' task.
 */
package com.mariopavlov;

import com.mariopavlov.array.ArraySum;
import com.mariopavlov.strategies.SequentialStrategy;

public class App {

    public static void main(String[] args) {

        int[] array = new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9};

        ArraySum arraySum = new ArraySum();
        SequentialStrategy sequentialStrategy = new SequentialStrategy(array);

        System.out.println("Sequential Array Sum: " + arraySum.calculateSum(sequentialStrategy));
    }
}
