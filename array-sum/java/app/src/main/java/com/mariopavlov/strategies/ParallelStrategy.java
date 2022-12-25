package com.mariopavlov.strategies;

import com.mariopavlov.interfaces.CalculateStrategy;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.ForkJoinTask;
import java.util.concurrent.RecursiveAction;

public class ParallelStrategy implements CalculateStrategy {

    private int number_of_tasks = 2; // Default

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
            // Sequential algorithm
            for (int i = start; i < end; i++) {
                value += input[i];
            }
        }
    }

    public void setNumberOfTasks(int tasks) {
        this.number_of_tasks = tasks;
    }

    @Override
    public long sum() {

        List<ParallelSumTask> tasks = new ArrayList<>();

        for (int task = 0; task < number_of_tasks; task++) {
            int inclusiveStart = getChunkStartInclusive(task, number_of_tasks, array.length);
            int exclusiveEnd = getChunkEndExclusive(task, number_of_tasks, array.length);

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
