# Day 5: Doesn't He Have Intern-Elves For This?

## Part One

Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

-   It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
-   It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
-   It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

For example:

-   _ugknbfddgicrmopn_ is nice because it has at least three vowels (_u_..._i_..._o_...), a double letter (..._dd_...), and none of the disallowed substrings.
-   _aaa_ is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
-   _jchzalrnumimnmhp_ is naughty because it has no double letter.
-   _haegwjzuvuyypxyu_ is naughty because it contains the string _xy_.
-   _dvszwmarrgswjxmb_ is naughty because it contains only one vowel.

How many strings are nice?

## Part Two

Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

-   It contains a pair of any two letters that appears at least twice in the string without overlapping, like _xyxy_ (_xy_) or aabcdefgaa (_aa_), but not like _aaa_ (_aa_, but it overlaps).
-   It contains at least one letter which repeats with exactly one letter between them, like _xyx_, _abcdefeghi_ (_efe_), or even _aaa_.

For example:

-   _qjhvhtzxzqqjkmpb_ is nice because is has a pair that appears twice (_qj_) and a letter that repeats with exactly one letter between them (_zxz_).
-   _xxyxx_ is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
-   _uurcxstgmygtbstg_ is naughty because it has a pair (_tg_) but no repeat with a single letter between them.
-   _ieodomkazucvgmuy_ is naughty because it has a repeating letter with one between (_odo_), but no pair that appears twice.

How many strings are nice under these new rules?

Source: https://adventofcode.com/2015/day/5
