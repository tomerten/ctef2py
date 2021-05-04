This file documents a python module built from Fortran code with f2py.
You should document the Python interfaces, *NOT* the Fortran interfaces.

Module ctef2py.fmohl
*********************************************************************

Module :py:mod:`fmohl` built from fortran code in :file:`f90_fmohl/fmohl.f90`.

.. function:: fmohl(a,b,q,np)
   :module: ctef2py.fmohl

   Compute the function fmohl as described in the paper on fast IBS calculations by `Nagaitsev <https://journals.aps.org/prab/abstract/10.1103/PhysRevSTAB.8.064403>`_.

   :param a: float  ``dtype=numpy.float64`` (input)
   :param b: float ``dtype=numpy.float64`` (input)
   :param q: float  ``dtype=numpy.float64`` (input)
   :param np: int ``dtype=numpy.float64`` (input)

   :returns: float