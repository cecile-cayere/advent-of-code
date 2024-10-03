# Day 12: JSAbacusFramework.io

## Part One

Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software uses a peculiar storage format. That's where you come in.

They have a JSON document which contains a variety of things: arrays (_[1,2,3]_), objects (_{"a":1, "b":2}_), numbers, and strings. Your first job is to simply find all of the numbers throughout the document and add them together.

For example:

-   _[1,2,3]_ and _{"a":2,"b":4}_ both have a sum of 6.
-   _[[[3]]]_ and _{"a":{"b":4},"c":-1}_ both have a sum of 3.
-   _{"a":[-1,1]}_ and _[-1,{"a":1}]_ both have a sum of 0.
-   _[]_ and _{}_ both have a sum of 0.

You will not encounter any strings containing numbers.

What is the sum of all numbers in the document?

## Part Two

Uh oh - the Accounting-Elves have realized that they double-counted everything red.

Ignore any object (and all of its children) which has any property with the value "red". Do this only for objects ({...}), not arrays ([...]).

-   _[1,2,3]_ still has a sum of 6.
-   _[1,{"c":"red","b":2},3]_ now has a sum of 4, because the middle object is ignored.
-   _{"d":"red","e":[1,2,3,4],"f":5}_ now has a sum of 0, because the entire structure is ignored.
-   _[1,"red",5]_ has a sum of 6, because "red" in an array has no effect.

Source: https://adventofcode.com/2015/day/12
