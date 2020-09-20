---
layout: assignment
title: "Lab 5: Randomized Comparison Tests and Timing Tests"
categories: lab
released: false
---
* TOC
{:toc}

Introduction
--------------------------------
In this lab, you'll create a timing test for the `SLList` and `AList` implementations of the `List61B` interface. You'll also create a randomized comparison test for a new interface called a `Lab5FloorSet`.

The ideas in this lab will be very important for when we get to project 2a and project 2b in mid October. These two projects will be similar to proj1a, except that we will not be providing an autograder! That is, you'll be responsible for verifying the correctness and speed of your code.

Timing Tests for List61B
--------------------------------

For project 1A, you were given a suite of extensive autograder tests that validated your code's accuracy and speed. However, in the real world, you'll be responsible for ensuring the correctness and efficiecny of your code. While we've seen some correctness testing (in the testing lecture, lab, and in the optional gold points for project 1), we have not yet discussed timing tests.

### Timing the construction of an AList with a bad resize strategy

As discussed [in lecture](https://docs.google.com/presentation/d/1xNOQqaazj_Qgzryc9KQegKyMds7msyWYAGXoQaXq02Q/edit#slide=id.g625dc7e36_0943), a multiplicative resizing strategy will result in fast add operations / good performance, whereas an additive resizing strategy will result in slow add operations / bad performance.

For this lab, we've provided the `AList` class created in lecture with the bad resizing strategy below:

```java
    public void addLast(Item x) {
        if (size == items.length) {
            resize(size + 1);
        }

        items[size] = x;
        size = size + 1;
    }
```

Your goal for this part of the lab is to write code that tabulates the amount of time needed to create a `AList` of various sizes using the `addLast` method above. The output of this timing test will look something like this:

```
Timing table for addLast
           N     time (s)        # ops  microsec/op
------------------------------------------------------------
        1000         0.00        10000         0.10
        2000         0.00        10000         0.10
        4000         0.00        10000         0.20
        8000         0.00        10000         0.20
       16000         0.00        10000         0.40
       32000         0.01        10000         0.90
       64000         0.01        10000         0.90
      128000         0.02        10000         1.50
```      

The first column `N` gives the size of the data structure. The second column `time (s)` gives the time required to complete all operations. The third column `# ops` gives the number of calls to `addLast` made during the timing experiment. And finally the fourth column `microsec/op` gives the number of microseconds it took on average to complete each call to `addLast`. Note that for this experiment, `N` and `# ops` is redundant, since the result of making 128,000 calls to `addLast` will result in an `N` of 128,000.

The important thing to notice here is that `addLast` is not "constant time". That is, the time to takes each `addLast` call to complete varies significantly with the size of the list: 1.50 microseconds when the list is long, and only 0.1 microseconds when the list is short. This is essentially how our autograder tests worked for your `LinkedListDeque` and `ArrayDeque` classes, i.e. we made sure that the time was constant for operations that should have been constant.

You might notice that the time per `addLast` operation is the same for N = 1000 and N = 2000. This is common for timing tests. For small inputs, results are unreliable for two reasons: The variance in runtime is high (due to issues like caching, process switching, branch prediction, etc. which you'll learn about if you take 61C), and the accuracy of our timer (milliseconds) is insufficient to resolve the difference between N = 1000 and N = 2000.

Now that you understand the table above, add a function `public void timeAListConstruction` to the class `TimeAList` that generates the table above for an `AList`. Note: If your computer is a little slow, you might want to stop at 64,000 instead of 128,000. Make sure to add a function call to `timeAListConstruction` to the `main` method of `TimeAList` class. 

For your convenience, we've provided a method called `printTimingTable(List<Integer> Ns, List<Integer> times, List<Double> opCounts)` that will print the table above, where `Ns` is the first column, `times` is the second column, and `opCounts` is the third column. The fourth column (`microsec/op`) is automatically computed for you. Your times should be in seconds. You should use the `Stopwatch` class. See `stopwatchDemo` for an example. 

### Timing the construction of an AList with a good resize strategy

Now modify the `AList`  class so that the resize strategy is multiplicative instead of additive and rerun `timeAListConstruction`. Your `AList` objects should now be constructed nearly instantly, even for N = 128,000, and each add operation should only take a fraction of a microsecond. 

Optional: Try increasing the maximum N to larger values, e.g. 10 million. You should see that the time per add operation remains constant.

Optional: Try experimenting with different resizing factors and see how the runtimes change. For example, if you resize by a factor of 1.01, you should still get constant time addLast operations!

```java
    public void addLast(Item x) {
        if (size == items.length) {
            resize((int) (size * 1.01));
        }

        items[size] = x;
        size = size + 1;
    }
```

### Timing the getLast method of SLList


In your `LinkedListDeque`, you were supposed to have `addLast` operations that were fast, or as the spec put it: "`add` and `remove` operations must not involve any looping or recursion. A single such operation must take "constant time", i.e. execution time should not depend on the size of the deque. This means that you cannot use loops that go over all/most elements of the deque."


Above, we showed how we can time the construction of a data structure. It is also common to compute the time per operation on a data structure that is pre-built before the test begins. That is, suppose we want to compute the time per operation for `getLast` for an `SLList` and want to know how this runtime depends on N. To do this, we need to follow the procedure below:

1. Create an `SLList`.
2. Add N items to the `SLList`.
3. Start the timer.
4. Perform M getLast operations on the `SLList`.
5. Check the timer. This gives the total time to complete all M operations.

It's important that we do not start the timer until after step 2 has been completed. Otherwise the timing test is including something other than the `getLast` operations.

In the `TimeSLListGetLast` class, add a function `timeGetLast` that performs the procedure above, and generates a table similar to the one shown below:

```
Timing table for getLast
           N     time (s)        # ops  microsec/op
------------------------------------------------------------
        1000         0.02        10000         1.70
        2000         0.03        10000         3.10
        4000         0.06        10000         6.20
        8000         0.13        10000        12.50
       16000         0.25        10000        25.00
       32000         0.53        10000        52.80
       64000         1.35        10000       135.30
      128000         2.57        10000       257.30
```

Note that the `N` and `# ops` columns are no longer the same. This is because we are always calling `getLast` regardless of the size of the list, i.e. `M = 10000` for step 4 of the procedure described above.

Note that the operations are again not constant time! This means that as the list gets bigger, the `getLast` operation becomes slower. This would be a serious problem in a real world application. For example, suppose the list is of ATM transactions, and the `getLast` operation was being called in order to get the most recent transaction to print a receipt. Every time the ATM is used, the next receipt would take a little bit longer to print. Eventually over many months or years, the list would become so large that the `getLast` operation would be unusably slow. While this is a contrived example, similar problems have plagued real world systems!

Optional question to ponder: Why is `getLast` so slow? Was your `LinkedListDeque` `getLast` function also slow?

Randomized Comparison Tests
-----------------------------------

For many interfaces, we'll often find that there are two extremes:
1. A simple but inefficient implementation.
2. A complex but efficient implementation.

For example, building an `ArrayDeque` where the list is always stored as an array of length corresponding to the items in the list would be easy, but very slow, whereas what you did in project 1a was much more complex, but also very fast.

For example, the slow but simple way would store `[9, 15, 31, 35]` as a length 4 array containing only `[9, 15, 31, 35]`. Your approach project 1A might have stored this list as `[0, 0, 9, 15, 31, 35, 0, 0]`, `nextFirst = 1`, `nextLast = 6`.

One way you might have tested your code if you were doing this in a real world setting would be to first implement a `SlowArrayDeque` and then `ArrayDeque`, and then compare the output of the two after applying random operations to make sure your `ArrayDeque` was correct.

For this part of the lab, we'll try to validate an implementation of a new interface called `Lab5FloorSet` class, which has two methods:
 - `add(double x)` adds x to the set. If x is already present, it has no effect.
 - `floor(double x)` gives the largest value in the set that is less than or equal to x. If no values are smaller than x, it should return negative infinity (`Double.NEGATIVE_INFINITY`).

For example, if we call `add(2.5)`, `add(10.0)`, and `add(11.2)`, then `floor(9)` would return `2.5`, since 2.5 is the largest value in the list that is smaller than  `9`. `floor(0)` would return negative infinity.

We've provided an implementation `RedBlackBST`. Your goal in this part of this lab will be to first write a correct but inefficient solution, then to use a randomized test to determine whether or not `RedBlackBST` is correct.

#### Implementing AListFloorSet (Optional)

Create a simple but correct implementation of `Lab5FloorSet` called `AListFloorSet`. Your `AListFloorSet` should have exactly one instance variable: an `AList`. Do not modify the `AList` class. 

Or if you'd rather skip this exercise, you can find the solution [here](link).

#### Using AListFloorSet to verify RedBlackFloorSet correctness

There is a bug somewhere in `RedBlackFloorSet`. To show that this bug exists, fill in the JUnit test in the `TestRedBlackFloorSet` file so that it follows the following procedure:

1. Generate 1,000,000 random doubles between -5000 and 5000, and add them to both an `AListFloorSet` and a `RedBlackFloorSet`.
2. Repeats the same random call 100,000 times to the `contains` method of the `AListFloorSet` and `RedBlackFloorSet`. Use `assertEquals` to compare the results. Note that since we're using doubles, you'll need to specify a tolerance, e.g. if you pick `0.000001`, then two doubles will be considered equal so long as they are within `0.000001` of each other.

To generate a random number between a and b, use `StdRandom.uniform(a, b)`.

Note: Since your `AListFloorSet` provides the expected output, make sure to use this as your left argument to `assertEquals`.


Submission
--------------------

TBD