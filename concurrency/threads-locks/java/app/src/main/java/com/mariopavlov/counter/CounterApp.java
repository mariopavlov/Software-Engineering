package com.mariopavlov.counter;

public class CounterApp {
    public static void main(String[] args) throws InterruptedException {
        // To work properly this I need to synchronize counter increment method
        // Otherwise I will have Data race
        Counter counter = new Counter();
        Counting counting1 = new Counting(counter);
        Counting counting2 = new Counting(counter);

        counting1.start(); counting2.start();
        counting1.join(); counting2.join();
        System.out.println("Counter: " + counter.getCount());
    }
}
