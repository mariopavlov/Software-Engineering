package com.mariopavlov;

import com.mariopavlov.array.ArraySum;
import com.mariopavlov.strategies.ParallelStrategy;
import com.mariopavlov.strategies.RecursiveStrategy;
import com.mariopavlov.strategies.SequentialStrategy;
import org.junit.Test;

import java.util.Random;

import static org.junit.Assert.*;

public class ArraySumTest {

    private final static int REPEATS = 10;

    @Test
    public void testSequentialSum() {
        int[] array = new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9};

        ArraySum arraySum = new ArraySum();
        SequentialStrategy sequentialStrategy = new SequentialStrategy(array);

        long result = arraySum.calculateSum(sequentialStrategy);
        assertEquals(45, result);
    }

    @Test
    public void testRecursiveSum() {
        int[] array = new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9};

        ArraySum arraySum = new ArraySum();
        SequentialStrategy sequentialStrategy = new SequentialStrategy(array);
        long expected = arraySum.calculateSum(sequentialStrategy);

        RecursiveStrategy recursiveStrategy = new RecursiveStrategy(array, 0, array.length - 1);
        long actual = arraySum.calculateSum(recursiveStrategy);

        assertEquals(expected, actual);
    }

    @Test
    public void testParallelSum() {
        int[] array = generateArray(80_000_000);

        ArraySum arraySum = new ArraySum();

        RecursiveStrategy recursiveStrategy = new RecursiveStrategy(array, 0, array.length - 1);
        ParallelStrategy parallelStrategy = new ParallelStrategy(array, 0, array.length - 1);


        long expected = -1;
        long actual = -2;

        /*
         * Run several repeats of the sequential and parallel versions to get an accurate measurement of parallel
         * performance.
         */
        final long recursiveStartTime = System.currentTimeMillis();
        for (int r = 0; r < REPEATS; r++) {
            expected = arraySum.calculateSum(recursiveStrategy);
        }
        final long recursiveEndTime = System.currentTimeMillis();

        final long parallelStartTime = System.currentTimeMillis();
        for (int r = 0; r < REPEATS; r++) {
            actual = arraySum.calculateSum(parallelStrategy);
        }
        final long parallelEndTime = System.currentTimeMillis();

        System.out.println("Array sum: " + actual);

        final long recursiveTime = (recursiveEndTime - recursiveStartTime) / REPEATS;
        final long parallelTime = (parallelEndTime - parallelStartTime) / REPEATS;

        System.out.println("Recursive Time: " + recursiveTime);
        System.out.println("Parallel Time: " + parallelTime);

        final double speedup = (double)recursiveTime / (double)parallelTime;
        final double expectedSpeedup = 1.5;

        assertEquals(expected, actual);
        assertTrue(recursiveTime > parallelTime);
        assertTrue(speedup >= expectedSpeedup);
    }

    private int[] generateArray(final int N) {
        final int[] input = new int[N];
        final Random rand = new Random(314);

        for (int i = 0; i < N; i++) {
            input[i] = rand.nextInt(100);
            // Don't allow zero values in the input array to prevent divide-by-zero
            if (input[i] == 0.0) {
                i--;
            }
        }

        return input;

    }

}
