!-------------------------------------------------------------------------------------------------
! Fortran source code for module ctef2py.getgauss
!-------------------------------------------------------------------------------------------------
! Remarks:
!   . Enter Python documentation for this module in ``./getgauss.rst``.
!     You might want to check the f2py output for the interfaces of the C-wrapper functions.
!     It will be autmatically included in the ctef2py documentation.
!   . Documument the Fortran routines in this file. This documentation will not be included
!     in the ctef2py documentation (because there is no recent sphinx
!     extension for modern fortran.

! ---------------------------------------------------------------------------------------------------------------
! ORIGINAL AUTHORS : MIKE BLASKIEWISC, RODERIK BRUCE, MICHAELA SCHAUMANN, TOM MERTENS
! ---------------------------------------------------------------------------------------------------------------
! VERSION 2.0 : UPDATE TO TRACK MULTIPLE BUNCHES AND HAVE DIFFERENT PARTICLE TYPES (P-PB) 
!   AUTHOR    : TOM MERTENS
!   DATE      : 19/12/2016
!   COPYRIGHT : CERN
!   
!   DESCRIPTION : 
!       FUNCTION TO GET DOUBLE GAUSSIAN
!       RETURNS TWO GAUSSIAN DISTRIBUTED RANDOM NUMBERS WITH SIGMA SQRT 3
! ---------------------------------------------------------------------------------------------------------------

subroutine getgaussrv(iseed,grv1,grv2)
  double precision, intent(inout) :: iseed
  double precision, intent(out):: grv1,grv2
  double precision :: r1,r2,facc,amp
    
  44 continue
     call random_number(iseed)
     r1 = 2*iseed-1
     r2 = 2*iseed-1
     amp = r1**2 + r2**2
    
     if ((amp.ge.1).or.(amp.lt. 1.e-8)) go to 44
     facc = sqrt(-2.*log(amp)/amp)
     grv1 = r1*facc/sqrt(3.)
     grv2 = r2*facc/sqrt(3.)
     return
end subroutine getgaussrv
    
    
