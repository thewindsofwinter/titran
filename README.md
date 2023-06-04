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

**Q: I wrote my spaceship launch computer [or equally important software] in TITRAN and it broke.**

A: You have learned a valuable lesson in the reliability of hacky projects from teenagers. That said, please email andyyt2@stanford.edu with bugs and how the code broke: we will fix things as quickly as we can. We accept no liability for use of this code (sorry about your billion-dollar rocketship).

## Specifications

Functions are defined as club announcements for certain club names. Each function is prefixed with "HEY IMSA" and ends with "ITS GONNA BE LIT"

## Testing
To test, run the following command from the root directory of the cloned repository.

`python ./src/titran-compile.py ./examples/[EXAMPLE_NAME].imsa; python output.py`

All examples are working except the explicit fibonacci example (no recursion).
