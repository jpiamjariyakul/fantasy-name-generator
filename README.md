# Fantasy Name Generator

I have found coming up with fantasy names to be a massive pain in the ass, so I wrote this program to help me with that.

This program runs in Python, and requires Python 3+ to run. Not sure if Python of lower versions work, but it works on 3!

The program takes the input of the length of the name the user wants, and generates it conforming to the following rules:

Consider position x in string.

1) If x-1 does not exist, set x to either consonant or vowel

2) If x-1 does exist:

>a) If x-1 is consonant:

>>1) If x-2 does not exist, set x to vowel

>>2) If x-2 does exist:

>>>a) If x-2 is consonant, set x to vowel

>>>b) If x-2 is vowel, set to either

>b) If x-1 is vowel:

>>1) If x-2 does not exist, set x to consonant

>>2) If x-2 does exist:

>>>a) If x-2 is consonant, set to either

>>>b) If x-2 is vowel, set to consonant

(Note that these rules are still being worked on.)

See program's comments for (slightly) more detailed description.

The program's still a work-in-progress, so don't expect too much. But it works, so hey, enjoy!
