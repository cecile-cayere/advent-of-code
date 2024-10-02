# Day 11: Corporate Policy

## Part One

Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: _xx_, _xy_, _xz_, _ya_, _yb_, and so on. Increase the rightmost letter one step; if it was _z_, it wraps around to _a_, and repeat with the next letter to the left until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

-   Passwords must include one increasing straight of at least three letters, like _abc_, _bcd_, _cde_, and so on, up to _xyz_. They cannot skip letters; _abd_ doesn't count.
-   Passwords may not contain the letters _i_, _o_, or _l_, as these letters can be mistaken for other characters and are therefore confusing.
-   Passwords must contain at least two different, non-overlapping pairs of letters, like _aa_, _bb_, or _zz_.

For example:

-   _hijklmmn_ meets the first requirement (because it contains the straight _hij_) but fails the second requirement requirement (because it contains _i_ and _l_).
-   _abbceffg_ meets the third requirement (because it repeats _bb_ and _ff_) but fails the first requirement.
-   _abbcegjk_ fails the third requirement, because it only has one double letter (bb).
-   The next password after _abcdefgh_ is _abcdffaa_.
-   The next password after _ghijklmn_ is _ghjaabcc_, because you eventually skip all the passwords that start with ghi..., since i is not allowed.

Given Santa's current password (your puzzle input), what should his next password be?

## Part Two

Santa's password expired again. What's the next one?

Source: https://adventofcode.com/2015/day/11
