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
4. atomicity. Object operations need to be consistent and happen one at a time

A patch to remove the GIL would be accepted if it doesn't hurt single-threaded performance.

It also shouldn't hurt C extensions.

Bad approaches
**************

tracing garbage collection: will break C extensions

software transactional memory: too early

Proposal
********

Keep reference counting

* atomic incr/decr

Globals and Static Variables

* Already moved to PyThreadState
* Shared singletons

c extension parallelism and reentrancy: they will break initially

Millions of locks instead of one giant one.

A new internal lock api.
Py_LOCK and Py_UNLOCK

``__lock__``

What needs locks
****************

All mutable objects: ``str``: 
+++++++++++++++++++++++++++++
  * ``hash``
  * ``utf8``
  * ``wstr`


Userspace lock
++++++++++++++

linux futex
windows critical_section
os x pthread_mutex

Political constraints
*********************

two builds that builds with and without the gil

Single ``.so``?

PEP 489
*******

This is perhaps a new C API

Enforce best practices

``PyType_Ready``

Why is it so slow
-----------------

2. Lock contention
1. synchronization and cache misses


