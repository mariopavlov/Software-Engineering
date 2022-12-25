// See https://aka.ms/new-console-template for more information

void PrintMessage()
{
    Console.WriteLine("Hello from Thread.");
}

Thread thread = new Thread(PrintMessage);

thread.Start();
Thread.Yield();

Console.WriteLine("Hello from Main.");

thread.Join();
