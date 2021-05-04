---
tags:
- udacity
- nanodegree
- problem
- problem-to-solve
---

# Investigating Texts and Calls

## Problem Definition

- In this problem I need to complete 5 tasks, based on a fabricated files of **calls** and **texts**;
	- The problem is broken beforehand on 5 tasks that I need to solve and analyze;
- I will use Python to analyze and answer questions about the texts and calls contained in the datasets;
- I will perform runtime and space analysis of my solutions;


## Steps to solve the problem

![[Problem Solving Techniques#Pythonista’s Guide to All problems in the Galaxy]]


## Input Requirements


All telephone numbers are **10 or 11 numerical digits long**. Each telephone number starts with a code indicating the **location** and/or **type of the telephone number**. There are three different kinds of telephone numbers, each with a different format:

- <em class="text-symbol"> Fixed lines </em> - **start with an area code enclosed in brackets**. The **area codes vary in length but always begin with 0**. Example: "(**022**)40840621".
- <em class="text-symbol">Mobile numbers</em> - have **no parentheses, but have a space in the middle of the number to help readability**. The **mobile code** of a mobile number **is its first four digits and they always start with 7, 8 or 9**. Example: "**9341**2 66159".
- <em class="text-symbol">Telemarketers</em> - numbers have **no parentheses or space**, but **start with the code 140**. Example: "**140**2316533".


### Messages File

Text data file (text.csv) in CSV format with following columns:
- sending telephone number (string)
- receiving telephone number (string)
- timestamp of text message (string)

![[(Investigating_Texts_and_Calls) texts.csv.png]]


### Phone Call File

Text data file (call.csv) in CSV format with following columns:

- calling telephone number (string)
- receiving telephone number (string)
- start timestamp of the call (string)
- duration of telephone call in seconds (string)

![[(Investigating_Texts_and_Calls) calls.csv.png]]



## Space Complexity

In Python is less clear how to calculate the Space efficiency due to the underlying data structures for housekeeping. So I will borrow from C and C++ the following sizes:  [^2]
![[Pasted image 20210426183223.png]]

When calculating the list Space complexity I'm not taking into consideration any of the metadata used by Python to store and housekeep the structures.

Also I'm not taking into consideration any of the environment or instructional space at that point.

Calls and Texts lists in Python are list of lists, example form:
```bash
calls = [
	['78130 00821', '98453 94494', '01-09-2016 06:01:12', '186'],
	['78298 91466', '(022)28952819', '01-09-2016 06:01:59', '2093']
	.
	.
	.
]

texts = [
	['97424 22395', '90365 06212', '01-09-2016 06:03:22'], 
	['94489 72078', '92415 91418', '01-09-2016 06:05:35'],
	.
	.
	.
]
```

All input data stored in the CSV file is stored and represented as [[String]].

### Representing single Phone call record

**Telephone numbers (calling and receiving)** can be:
- 10 or 11 symbols (+2 additional for brackets), so I will calculate it as a worst-case 13 symbols.
- every string symbol is represented as character, and the string as a sequence of chars will take up to: **$13\:Bytes$**

**Timestamp** is represented with 19 character symbols or **$19\:Bytes$**

**Duration** - there is no limit on the phone duration, and I will assume as worst case scenario that the time duration is no longer than 9999 seconds, or 4 characters. This results in **$4\:Bytes$**

The final calculation for Space complexity based on that will be:
**$O(2 \cdot 13\:Bytes + 19\:Bytes + 4\:Bytes) = 49\:Bytes$**

### Representing single Texts record

**Telephone numbers (sending and receiving)** are represented by worst-case 13 symbols record (same as the Phone call).

**Timestamp** is represented with 19 character symbols or **$19\:Bytes$**

Final calculation for single text record (constant size): 
**$O(2 \cdot 13\:Bytes + 19\:Bytes) = 45\:Bytes$**


### Storing Texts and Phone Calls

The final calculation for Space Complexity is:
**`texts[]`** list: **$O(n \cdot 45\:Bytes)$**
**`calls[]`** list: **$O(n \cdot 49\:Bytes)$**


### Live Experiment

The experiment was conducted on MacBook Pro (Intel Processor), using:
- PyCharm Professional[^3]; 
- Python 3.9[^4];
- and Python Memory-Profiler module[^5].

Rough calculations for texts list: it appears that most of the records are only mobile numbers (11 chars): 
$11\:Bytes \cdot 2 + 19\:Bytes = 41\:Bytes \cdot 9072\:records = 371952\:Bytes$ or **$0.354721\: Megabytes$**

But actually the list takes around: **$2.7\:MiB$**

```bash
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     9     16.1 MiB     16.1 MiB           1   @profile
    10                                         def read_texts():
    11                                             global f, reader, income_number, answering_number, timestamp
    12     16.1 MiB      0.0 MiB           1       with open('texts.csv', 'r') as f:
    13     16.1 MiB      0.0 MiB           1           reader = csv.reader(f)
    14                                         
    15                                                 # List of list elements containing all calls
    16     18.7 MiB      2.7 MiB           1           texts = list(reader)
    17                                         
    18                                                 # Access the first element in the list
    19     18.7 MiB      0.0 MiB           1           first_record = texts[0]
    20     18.7 MiB      0.0 MiB           1           income_number = first_record[0]
    21     18.7 MiB      0.0 MiB           1           answering_number = first_record[1]
    22     18.7 MiB      0.0 MiB           1           timestamp = first_record[2]
    23                                         
    24                                                 # Output the result
    25     18.7 MiB      0.0 MiB           1           print(f'First record of texts, {income_number} texts {answering_number} at time {timestamp}')
```

I'm not sure why the result differs so much, even if single list record representation takes 2 times or 3 times the size of the strings, the result does not come close to the actual.  Need #further-investigation , or during the Nanodegree I may receive the answers.


## Problems to be solved

The problem (or project) is divided into 5 tasks, that are predefined by Udacity. Each task needs to solve a problem, and analyze the solution to the problem. At first glance over the project requirements I'm **not seeing any requirements for Space or Time complexities**.

However, the final solution needs to be checked against [[Udacity Rubric]]?, and submitted for review by Udacity reviewer.

In task 3 and Task 4, I can use built-in Python methods **`sorted()`** and **`list.sort()`**, which are implementations of Timsort[^timsort] and Samplesort[^samplesort]. I can read further how to use these Python Built-in function on Python documentation[^how-to-sort]. In Python documentation I can also find more information and analyses for Time complexity[^python-samplesort-docs] on the sorting algorithms used.

General Bio O Cheetsheet can be downloaded from [Know Thy Complexities!](https://www.bigocheatsheet.com/)[^complexity-cheetsheet].

### Task 0: Printing First and Last records

First task of the project, requires from me to:
- print first record from texts file;
- print last record from calls file;

**Example of the output:**
```bash
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
```

#### Flowchart of the solution

![[Pasted image 20210427223205.png]]

#### Analyses on Printing First record from Texts

-   using Python built-in function **`open`** to load file: $O(1)$ (**constant time**), this is actually a pointer to a system handle (C++);
-   creating reader iterator: $O(1)$ (**constant time**);
-   **(Operation: Insert)**[^wiki-time-complexity] - Creating text record in Python list from iterator, for every input record: $O(n)$ (**linear time**);
-   **(Operation: Get Item)**[^wiki-time-complexity] - getting an item from a list has constant time complexity;
-   output to console operation has constant time complexity;

The most demanding operation is the creation of texts list from iterator, which is linear iteration over CSV file.
Task 0 - Print first item from list: **$O(n)$**

#### Analyses on Printing Last record from Calls

Printing last record from a CSV is similar to printing the first record. There is one difference here, we are getting the **last item**. If we were talking for C++, I had to carefully analyze also the type of list implemented for the operation Time Complexity calculation. However, in Python **getting item from list** is **constant time operation**, without taking into consideration the place of the element that I seek.

Taking into consideration the above mentioned implementation specifics, I can conclude that the complexity for printing last record from CSV file is with the same complexity:
Task 0 - Print last item from list: **$O(n)$**

#### Task 0 time complexity

For the whole task (considered as a module) time complexity is:
$O(2 \cdot n)$

### Task 1: Counting unique telephone numbers

For the second task I need to calculate how many unique numbers are the records. It is not clearly specified whether or not I need to count numbers from Phone file, or from Texts file, also it is not specified whether or not I need to count In or Out telephone numbers so I do assume by default that I need to calculate numbers from both **`calls.csv`** and and **`texts.csv`**. Columns used to count unique numbers:
- sending telephone number (texts.csv)
- receiving telephone number (texts.csv)
- calling telephone number (calls.csv)
- receiving telephone number (calls.csv)

#### Flowchart of the solution

![[Pasted image 20210502081824.png]]

#### Analysis on Counting unique numbers

To count the unique numbers as described in the Flowchart I need to iterate twice every input file, which translates to $O(2 \cdot n)$.

Once:
- Create global set variable (**Constant time**")
- Print output length of **`unique_numbers`** set (**Constant time**)

For every input file (texts and calls):
- Open python file (**Constant time**)
- Create Iterator (**Constant time**) 
- Create list from reader iterator - $O(n)$ 
- For every input, add numbers (in/out) to global set $O(n)$

#### Task 1 time complexity

For the whole task (considered as a module) time complexity is:
$O(4 \cdot n)$

### Task 2: Longest Phone Call

In this task I need to find the longest Phone call that is stored in **`calls.csv`**, and output the following information:
**`"<telephone number> spent the longest time, <total time> seconds, on the phone during September 2016."`**

I can think of couple solutions:
- Go for each record and compare the time duration;
- Sort the list by duration field and pick first/last record depending on the sorting criteria;

In the previous task [[#Task 1 Counting unique telephone numbers]] I already have performed going record by record to search for unique numbers. This will easily give me again time complexity of $O(2 \cdot n)$, comparing with sorting methods that are outlined in the project **`Timsort`** and **`Samplesort`** I will get the same time complexity if not worse. 

Based on that I will go with the linear search in the whole list. Also, I will not consider which record to choose if two or more call records are with the same duration. I will simply get the first record found.

#### Flowchart

![[Pasted image 20210503151919.png]]

#### Analysis

Most of the operation that are happening in this task have been already discussed in the previous tasks. The difference here is in the for loop:
- Creating list from input csv file is **Linear operation** $O(n)$
- Converting duration from string to integer is **Constant operation**
- Iterating over a list is **Linear** $O(n)$
- If condition is by itself does have $O(1)$ complexity, but it depends a lot on what operation is performed. In my case the operation of setting variable is constant time. So the whole operation will have **Constant time complexity**.

#### #### Task 2 time complexity

**Absolutely complexity**: $O(2 \cdot n)$
**Relative complexity: $O(n)$**

### Task 3: Bangalore Call Statistics

At this stage I'm considering to create new function that get as input phone number and returns the type of the phone number. The best location of such function would be in a new module for re-usability, but I'm not sure still what is the [[Udacity Rubric]], and whether or not I can pass a new module for this Project. I'm guessing that this will not be possible. So I will make a function inside the Task and unit test it against the task.

The task itself looks for certain call statistics.
- Find all mobile phone prefixes and and area codes, for Bangalore numbers;
- The list of phone codes need to be printed out in [[Lexicographic Order]] [^wiki-lexi-order] [^lexi-sorted-order];
- How many calls from Bangalore are made to Bangalore (return as percent);


Helper functions that I will need for the current task:
- **get_telephone_type** - get telephone number as input, and returns: **fixed**, **mobile**, **telemarketers**;
- **get_area_code** - takes as input phone number, returns area code such as **(080)**;
- **get_fixed_location** - takes as input **fixed** type of telephone number, and returns location ex. **Bangalore**, for all other numbers (including fixed lines outside of Bangalore) return unknown of the moment;

#### Flowchart

Task 3
![[Pasted image 20210503151951.png]]

Helper functions
![[Pasted image 20210503121037.png]]

![[Pasted image 20210503121043.png]]

![[Pasted image 20210503121050.png]]

#### Analysis

Going from backward of the solution, I had to take a decision whether to extend in iterative manner the first solution, to produce the second one. However, as we are looking for simple mechanical solutions at first, and as we are looking for **Relative complexity**  not **Absolute** I decided to go with two similar solution one after another. The overhead of going twice element by element in the Calls list is not so big (compared to relative complexity). Also at this stage I'm not seeing any restrictions on performance or memory.

Now getting into analyzing the **Helper functions**.

Helper function to find what telephone type we are dealing with: **get_telephone_type**:
- in this helper function we do have two comparisons with **str.startswith**. I did not manage to find how the function is implemented, but for the sake of this exercise I can guess that it compares symbol by symbol. In normal circumstances this translates to **Linear complexity** - $O(n)$, but in my scenarios I'm comparing fixed width strings every time, so I will consider the operation as a **Constant**.

Helper function that finds the area code **get_area_code**:
- First we have a **constant operation** call to **get_telephone_type**;
- Then we have couple comparisons which are also **Constant time operations**;
- For the fixed line numbers, as their size can vary I decided for first implementation go to with regex search **Linear operation**, I'm not trying to compare the whole string only bits of the string, but as I'm not looking specifically for the start of a string (even the I know it should be there), I will consider the operation as linear. **$O(n)$** (**This may be a good candidate for future improvements**)

And finally we are getting into get fixed location function, which at the moment is used only to match Bangalore call codes.
- I will consider this helper function to be of **Constant time complexity - $O(1)$**

Now, I can focus on calculating the whole **Task 3 complexity**.

**Solution A**: On top of the previously calculated time complexity (in Tasks 0, 1 and 2) of $O(n)$ we have:
- adding item to **set** - **Linear time complexity $O(n)$**
- get_fixed_location is with **Constant time complexity**
- get_area_code has **Linear time complexity**
- **sorted (Timsort)** function call to get **lexicographical order of the set**, which has **Linearithmic** time according to the documentations $O(n \cdot log \: n)$ [^timsort]

Calculating the final time complexity:
- Having an for loop that makes call to another **Linear time complexity** function translates to **Quadratic - $O(n^2)$**
- And comparing **Quadratic time** against **Linearithmic time**, I conclude[^complexity-cheetsheet] the final **Relative time complexity is: $O(n^2)$**

**Solution B:**
- as in looking for the percentage of calls from Bangalore to Bangalore I'm comparing twice against **get_fixed_location** the time complexity is still **$O(n)$**


#### Task 3 time complexity

The final conclusion for the whole Task, is that the **relative time complexity** of my solution is: **$O(n^2)$**. (Of course if I was looking for performance optimizations this time is not good enough)

### Task 4: Looking for Marketing telephones

I can reuse all helper functions from the previous task in order to finish faster Task 4.
The job for me here is to find all telemarketer phones in both **`texts.csv`** and **`calls.csv`**. From the phone that I find in those lists then I need to create a set of possible phone numbers. The possible phone numbers I need to check against both files again but this time I need to search in the second columns, they **should not receive any incoming calls** or **should not receive any text messages**.

#### Flowchart

![[Pasted image 20210504211002.png]]

#### Analysis

Most of the code is reused from the previous Task (although the fact that is copy and paste). So I will analyze only bits and parts of the code.

- starting from the end, **sorted (Timsort)** has **Linearithmic** time according to the documentations $O(n \cdot log \: n)$;
- going to the new function from this module: **`find_non_telemarketers`** I have for loop for every element in the input list, which translated to **$O(n)$**. Then for every element that is **telemarketer** I have **add operation** to a **set** which translates to another **$O(n)$**. Even though not every element will be **telemarketer** there is a possibility in which all the numbers are **telemarketers**. Time complexity for the function is: **$O(n^2)$**;
- for the same reason as above **`filter_telemarketers`** (the **set**) I conclude that the time complexity is again: **$O(n^2)$** (even though the chance is smaller than the previous to hit all records);

#### Task 4 time complexity

As we are having three operations to compare, two of which are with **Quadratic time** and one is with **Linearithmic (Log-linear Time)** the slower of them is **Quadratic**[^complexity-cheetsheet].

For the whole module, time complexity is: **Quadratic Time - $O(n^2)$**

## Bibliography and Resources

[^complexity-cheetsheet]: _Know Thy Complexities! (Cheatsheet)_. (2020). https://www.bigocheatsheet.com/
[^2]: _Space Complexity Examples_. (n.d.). Udacity. Retrieved April 27, 2021, from https://classroom.udacity.com/nanodegrees/nd256/parts/f74fc064-524b-4ee8-8fb1-570b3c31a993/modules/3675395a-5de0-4f74-a4c1-eadafd6be9f9/lessons/b5ed8170-8fce-463a-aefc-64272cb3852e/concepts/09af2846-2d8a-4688-870e-89fb57e7c74c
[^3]: JetBrains. (2021). _PyCharm Professional_ (2021.1.1). JetBrains. https://www.jetbrains.com/pycharm/
[^4]: Python Software Foundation. (2020). _Python 3.9.0_ (3.9.0). Python Software Foundation. https://www.python.org/downloads/release/python-390/
[^5]: fpedregosa. (2020). _memory-profiler 0.58.0_ (0.58.0). Open Source. https://pypi.org/project/memory-profiler/
[^timsort]: _Timsort Wikipedia_. (n.d.). Wikimedia Foundation. Retrieved April 27, 2021, from https://en.wikipedia.org/wiki/Timsort
[^samplesort]: _Samplesort Wikipedia_. (n.d.). Wikimedia Foundation. Retrieved April 27, 2021, from https://en.wikipedia.org/wiki/Samplesort
[^how-to-sort]: Python Software Foundation. (n.d.). _Sorting How To_. Python.Org. Retrieved April 27, 2021, from https://docs.python.org/3/howto/sorting.html
[^python-samplesort-docs]: Python Software Foundation. (n.d.). _Comparison with Python’s Samplesort Hybrid_. Python.Org. Retrieved April 27, 2021, from https://svn.python.org/projects/python/trunk/Objects/listsort.txt
[^wiki-time-complexity]: _Python Wiki TimeComplexity_. (n.d.). https://wiki.python.org/moin/TimeComplexity
[^wiki-lexi-order]: _Lexicographic Order_. (n.d.). Wikimedia Foundation. Retrieved May 2, 2021, from https://en.wikipedia.org/wiki/Lexicographic\_order
[^lexi-sorted-order]: Samual Sam. (2018). _Sort the words in lexicographical order in Python_. Tutorials Point. https://www.tutorialspoint.com/Sort-the-words-in-lexicographical-order-in-Python


