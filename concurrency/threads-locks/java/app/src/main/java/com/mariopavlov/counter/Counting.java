package com.mariopavlov.counter;

public class Counting extends Thread {
    final Counter counter;

    public Counting(Counter counter) {
        this.counter = counter;
    }

    public void run() {
        for (int i  = 0; i < 10_000; i++) {
            counter.increment();
        }
    }
}
