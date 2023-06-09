# Titran 
Programming language based on the Turing-complete nature of high school intercom announcements. Contains both a compiler and interpreter, both written in Python.

## (In)frequently Asked Questions

**Q: How was such an elegant, sublime programming language ever created?**

A: Two students, one recently graduated from high school ('22) and one a junior at the time ('24), received a divine flash of inspiration from the spirit of John McCarthy, creator of Lisp. HE inspired the creation of a language that would no longer be plagued by feature creep, one whose expression could be learned, nay, indoctrinated into students before they even touched a computer to begin with. 

**Q: Why would I ever want my code to look like high school intercom announcements?**

A: A few advantages for the unbelievers:
 - Debugging is easy: ask yourself, "would I actually hear this in high school?"
 - Easy learning curve, especially for Python programmers because all Titran transpiles to Python. 
 - Titran ignores all lines of code that are not Titran: you can integrate it into Python as needed.
 - Whitespace doesn't matter in Titran, so no more annoying bugs based on blank space!

**Q: I wrote my spaceship launch computer [or equally important software] in Titran and it broke.**

A: You have learned a valuable lesson in the reliability of hacky projects from teenagers. That said, please email andyyt2 at stanford dot edu with bugs and how the code broke: we will fix things as quickly as we can. We accept no liability for use of this code (sorry about your billion-dollar rocketship).

**Q: Is Titran related to Fortran?**

A: We certainly hope to be as easy to learn! Otherwise, the two share only one fact: Fortran was made for scientific computation, and Titran was made from announcements at the Illinois Math and Science Academy. We certainly take the "screw around and find out" view of things, popularized by languages like C.

## Specifications

There are two scopes for our program: Titran scope and Python scope. The program, by default, is in Titran scope. In Titran scope, you can switch to Python scope through the opening and closing characters `P{` and `}Y`. In Python scope, you can switch back to Titran scope using `IM{` and `}SA`. The general gist of our language is that functions are defined as club announcements, with variable names defined as the people giving the announcement, by tradition. This maximizes the chance of said person feeling slighted by the way you wrote the function, resulting in familiar, joyful high school drama. The main function is defined as a chronicle of an ordinary high school day.

Note that Titran does not throw compiler errors and will joyfully spit out garbage if you code things wrong. It will try to indent properly for Python, but this is never perfect. Do email me (andyyt2 at stanford dot edu) and/or open an issue if you discover any bugs though, I will joyfully fix them.

In more detail, here's the subset of Python that we modify:

```
Special Number Literals: 150X = X
SECURITY = 0

MULTIPLY = COLLAB BETWEEN(CLUB1, CLUB2), where CLUB1 and CLUB2 are arbitrary expressions

DEFINE FUNCTION: HEY IMSA [(parameters are people) FROM CLUB_NAME]
END FUNCTION: IT’S GONNA BE LIT

CALL FUNCTION: 
ANNOUNCEMENT FROM CLUB_NAME
ANNOUNCEMENT BY (names) FROM CLUB_NAME

BEGIN MAIN: GOOD MORNING IMSA
END MAIN: THE MAIN BUILDING IS CLOSING

ASSIGN VARIABLE: 
[person] PLEASE REPORT TO {[statement]}
[person] PLEASE REPORT TO {[statement] IMMEDIATELY} (input from standard in)

RETURN: BE THERE OR BE SQUARE
PRINT: {[statement]}

IF STATEMENT: HEY [NAME], ARE YOU [CONDITIONAL?]:
ELSE IF: OR ARE YOU [X]?
ELSE: OR DO YOU JUST WANT FREE PIZZA?
END IF BLOCK: Then come down to the [PLACE] right now!

WHILE LOOP: We’re hosting a fundraiser at 05 slabs!
END WHILE: Get your stuff while [conditional]
```


## Testing
To test, run the following command from the root directory of the cloned repository.

`python ./src/titran-compile.py ./examples/[EXAMPLE_NAME].imsa; python output.py`

All examples are working except the explicit fibonacci example (no recursion).
