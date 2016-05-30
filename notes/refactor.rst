Refactoring Python
==================

Brett Slatkin

What, when, why, & how, strategies, follow-up


What, when, why, & how
----------------------

When
++++

* in advance of adding features. 
* For testing (is it hard to test?)
* DRY
* Brittleness, features break each other
* complexity


Why
+++

Good vs Great programmers: take the time to test and document

How
+++

1. ID bad code
2. Improve it
3. Run tests
4. Fix and improve tests
5. Repeat

In practice:

* rename, split, move
* simplify
* Redraw boundaries

Prerequesites:

* Thorough tests
* Quick tests
* Source control
* Willing to make mistakes


Strategies
----------

Extract into variables

Extract into functions (great for combining variables in conditionals)

Or you can extract variables into a class

Eg: ``self.__bool__(self)`` aka ``__nonzero__``: return self.result 

This is how you can call an instantiated class in an if statement. This helps enourmously for testing.

More Class Strategies
+++++++++++++++++++++

.. code::

  class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def needs_heat_lamp(self):
        # etc

A huge mega-class is a strong indication that you need to refactor.

Redraw boundaries
+++++++++++++++++

1. Add an improved interface, matinain backwards compatibility, issue warnings
2. migrate old to new, run tests to verify, fix and imporive broken tests
3. Remove old code interface

Warnings
********

.. code::

    import warnings
    warnings.warn("helpful message")

There's a way to raise warnings as errors. This ensures that people are utilizing the new usage.

After
*****

.. code::

    class Pet:
      def __init__(self, name, age, animal=None, **kwargs):
          if kwargs and animal is not None:
              # old and new style
              raise TypeError('Mixed Usage')
          if animal is None:
            warnings.warn('Should use Animal')
            animal = Animal(**kwargs)
          # the rest of the code

      @property
      def has_scales(self):
          warning.warning("Use the animal attribute")
          return self.animal.has_scales

Split classes using optional arguments to __init__

Move Field Gotchas
------------------

before we refactor, we ask: "Is this obvious?"

.. code::

  @age.setter
  def age(self, new_age):
    raise AttributeError('Use new age')
