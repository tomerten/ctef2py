This file documents a python module built from Fortran code with f2py.
You should document the Python interfaces, *NOT* the Fortran interfaces.

Module ctef2py.getgauss
*********************************************************************

Module :py:mod:`getgauss` built from fortran code in :file:`f90_getgauss/getgauss.f90`.

.. function:: add(x,y,z)
   :module: ctef2py.getgauss

   Compute the sum of *x* and *y* and store the result in *z* (overwrite).

   :param x: 1D Numpy array with ``dtype=numpy.float64`` (input)
   :param y: 1D Numpy array with ``dtype=numpy.float64`` (input)
   :param z: 1D Numpy array with ``dtype=numpy.float64`` (output)
