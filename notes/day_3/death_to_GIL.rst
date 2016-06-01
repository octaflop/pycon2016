Python's Infamous GIL
=====================

multithreading
cpython internals

cf. "Python's Infamous GIL"

the GIL
-------

Added to support threading and a way to support global and static threading in threads. 24 years ago 1992.

ramifications
*************

* simple
* easy to get right
* no deadlocks
* low overhead
* great at single-threaded code

* i/o bound with mulitple threads everything was OK
* cpu bound programs was not so OK 🚯

the world has changed
*********************

Python hasn't. Python can take advantage of all of your computer's resources *except* for mutlple cores.

Free-Threading patch had no api changes
Made code run 4×-7× slower.

The GILEctomy
-------------


Technical considerations
************************

1. reference counting
2. globals and statics
  * per-thread information
  * shared singletons
3. C-extentions and reentrancy
4. 


