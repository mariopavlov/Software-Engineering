package com.mariopavlov;

public class App {

    public static void main(String[] args) throws InterruptedException {

        Thread thread = new Thread() {
            public void run() {
                System.out.println("Hello from Thread!");
            }
        };

        // Perform Unit of work in new Thread
        thread.start();

        // Hint to the scheduler that current thread will Yield current use of processor
        // Without this statement on almost every execution main thread print statement will execute first
        Thread.yield();

        System.out.println("Hello from Main program");

        // Wait to newly created thread to finish
        thread.join();
    }
}
