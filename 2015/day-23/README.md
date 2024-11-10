# Day 23: Opening the Turing Lock

## Part One

Little Jane Marie just got her very first computer for Christmas from some unknown benefactor. It comes with instructions and an example program, but the computer itself seems to be malfunctioning. She's curious what the program does, and would like you to help her run it.

The manual explains that the computer supports two registers and six instructions (truly, it goes on to remind the reader, a state-of-the-art technology). The registers are named a and b, can hold any non-negative integer, and begin with a value of 0. The instructions are as follows:

-   _hlf r_ sets register _r_ to half its current value, then continues with the next instruction.
-   _tpl r_ sets register _r_ to triple its current value, then continues with the next instruction.
-   _inc r_ increments register _r_, adding 1 to it, then continues with the next instruction.
-   _jmp offset_ is a jump; it continues with the instruction _offset_ away relative to itself.
-   _jie r, offset_ is like _jmp_, but only jumps if register _r_ is even ("jump if even").
-   _jio r, offset_ is like _jmp_, but only jumps if register _r_ is 1 ("jump if one", not odd).

All three jump instructions work with an offset relative to that instruction. The offset is always written with a prefix + or - to indicate the direction of the jump (forward or backward, respectively). For example, _jmp +1_ would simply continue with the next instruction, while _jmp +0_ would continuously jump back to itself forever.

The program exits when it tries to run an instruction beyond the ones defined.

For example, this program sets _a_ to 2, because the _jio_ instruction causes it to skip the tpl instruction:

    inc a
    jio a, +2
    tpl a
    inc a

What is the value in register b when the program in your puzzle input is finished executing?

## Part Two

The unknown benefactor is very thankful for releasi-- er, helping little Jane Marie with her computer. Definitely not to distract you, what is the value in register b after the program is finished executing if register a starts as 1 instead?

Source: https://adventofcode.com/2015/day/23
