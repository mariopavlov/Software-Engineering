package com.mariopavlov.strategies;

import com.mariopavlov.interfaces.CalculateStrategy;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.ForkJoinTask;
import java.util.concurrent.RecursiveAction;

public class ParallelStrategy implements CalculateStrategy {

    private static final int NUMBER_TASKS = 8;

    private final int low;
    private final int high;
    private final int[] array;

    public ParallelStrategy(int[] array, int low, int high) {
        this.array = array;
        this.low = low;
        this.high = high;
    }

    private static class ParallelSumTask extends RecursiveAction {

        private final int start;
        private final int end;
        private final int[] input;

        // Intermediate value produced
        private long value;

        ParallelSumTask(int[] input, int start, int end) {
            this.input = input;
            this.start = start;
            this.end = end;
        }

        public long getValue() {
            return value;
        }


        @Override
        protected void compute() {
            /*if (start == end) {
                value = input[start];
            } else if (start > end) {
                value = 0;
            } else {
                int mid = (end + start) / 2;
                ParallelSumTask lowerHalf = new ParallelSumTask(input, start, mid);
                ParallelSumTask upperHalf = new ParallelSumTask(input, mid + 1, end);
                // invokeAll(lowerHalf, upperHalf);
                lowerHalf.compute();
                upperHalf.compute();
                value = lowerHalf.value + upperHalf.value;
            }*/

            for (int i = start; i < end; i++) {
                value += input[i];
            }
        }
    }

    @Override
    public long sum() {

        List<ParallelSumTask> tasks = new ArrayList<>();
        ForkJoinPool pool = new ForkJoinPool(NUMBER_TASKS);

        for (int task = 0; task < NUMBER_TASKS; task++) {
            int inclusiveStart = getChunkStartInclusive(task, NUMBER_TASKS, array.length);
            int exclusiveEnd = getChunkEndExclusive(task, NUMBER_TASKS, array.length);

            // Use this call for Recursive Implementation
            // tasks.add(new ParallelSumTask(array, inclusiveStart, exclusiveEnd - 1));

            // Use this call for Sequential
            tasks.add(new ParallelSumTask(array, inclusiveStart, exclusiveEnd));
        }

        ForkJoinTask.invokeAll(tasks);
        return tasks.stream().mapToLong(t -> t.getValue()).sum();
    }

    private static int getChunkSize(final int nChunks, final int nElements) {
        // Integer ceil
        return (nElements + nChunks - 1) / nChunks;
    }

    private static int getChunkStartInclusive(final int chunk,
                                              final int nChunks, final int nElements) {
        final int chunkSize = getChunkSize(nChunks, nElements);
        return chunk * chunkSize;
    }


    private static int getChunkEndExclusive(final int chunk, final int nChunks,
                                            final int nElements) {
        final int chunkSize = getChunkSize(nChunks, nElements);
        final int end = (chunk + 1) * chunkSize;
        if (end > nElements) {
            return nElements;
        } else {
            return end;
        }
    }


}
