# Day 7: Some Assembly Required

## Part One

This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: _x AND y -> z_ means to connect wires _x_ and _y_ to an _AND_ gate, and then connect its output to wire _z_.

For example:

-   _123 -> x_ means that the signal 123 is provided to wire _x_.
-   _x AND y -> z_ means that the bitwise _AND_ of wire _x_ and wire _y_ is provided to wire _z_.
-   _p LSHIFT 2 -> q_ means that the value from wire p is left-shifted by 2 and then provided to wire _q_.
-   _NOT e -> f_ means that the bitwise complement of the value from wire _e_ is provided to wire _f_.

Other possible gates include _OR_ (bitwise _OR_) and _RSHIFT_ (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

    123 -> x
    456 -> y
    x AND y -> d
    x OR y -> e
    x LSHIFT 2 -> f
    y RSHIFT 2 -> g
    NOT x -> h
    NOT y -> i

After it is run, these are the signals on the wires:

    d: 72
    e: 507
    f: 492
    g: 114
    h: 65412
    i: 65079
    x: 123
    y: 456

In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

## Part Two

Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?

Source: https://adventofcode.com/2015/day/7
