package com.mariopavlov.Philosophers;

import java.util.Random;

public class Philosopher extends Thread {

    private final Chopstick first;
    private final Chopstick second;
    private final Random random;
    private int thinkCount;

    public Philosopher(Chopstick left, Chopstick right) {
        // Deadlock behavior
        /*
        first = left;
        second = right;
        */

        // Prevent Deadlocks
        // Always obtain locks in global order
        if (left.getId() < right.getId()) {
            first = left;
            second = right;
        } else {
            first = right;
            second = left;
        }

        random = new Random();
        thinkCount = 0;
    }

    public void run() {
        try {
            while (true) {
                // Thinking
                Thread.sleep(random.nextInt(1000));
                ++thinkCount;
                System.out.println("Philosopher " + this + " has thought " + thinkCount + " times");

                synchronized (first) {
                    synchronized (second) {
                        // Eat
                        Thread.sleep(random.nextInt(1000));
                    }
                }
            }
        } catch (InterruptedException e) {
        }
    }

}
