program main
    use LinearAlgebra
    implicit none
    integer:: i, j, N
    real*8, allocatable, dimension(:,:):: H
    real*8, allocatable, dimension(:):: eigval

    N = 2
    allocate(H(N, N))
    allocate(eigval(N))
    
    do i = 1, N
        do j = 1, i
            H(i, j) = i + j
        end do
    end do

    ! call My_dsyev('N', H, eigval, N)
    call My_dsyev('V', H, eigval, N)

    write(*,*)eigval

end program main