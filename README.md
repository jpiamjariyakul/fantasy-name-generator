# Fantasy Name Generator

I have found coming up with fantasy names to be a massive pain in the ass, so I wrote this program to help me with that.

This program runs in Python, and requires Python 3+ to run. Not sure if Python of lower versions work, but it works on 3!

The program takes the input of the length of the name the user wants, and generates it conforming to the following rules:

Consider position x in string.

1) If x-1 does not exist, set x to either consonant or vowel

2) If x-1 does exist:

2.a) If x-1 is consonant:

2.a.1) If x-2 does not exist, set x to vowel

2.a.2) If x-2 does exist:

2.a.2.a) If x-2 is consonant, set x to vowel

2.a.2.b) If x-2 is vowel, set to either

2.b) If x-1 is vowel:

2.b.1) If x-2 does not exist, set x to consonant

2.b.2) If x-2 does exist:

2.b.2.a) If x-2 is consonant, set to either

2.b.2.b) If x-2 is vowel, set to consonant

(Note that these rules are still being worked on.)

The program's still a work-in-progress, so don't expect too much. But it works, so hey, enjoy!
