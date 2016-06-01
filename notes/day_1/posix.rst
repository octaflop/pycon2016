Posix with Christian Heimes
===========================

https://us.pycon.org/2016/schedule/presentation/2019/

* 0 = stdin
* 1 stdout
* 2 sys.stderr
* -1 ⇒ python exception


Modern OS
---------

everything goes through the kernal

everything is created with ``fork()`` and ``exec()``

``subprocess.PIPE``
-------------------

.. code:: python
  
  import os
  readend, writeend = os.pipe()
  pid = os.fork()
  if pid != 0:
      os.close(writeend)
      with open(readend) as f:
        # do stuff



