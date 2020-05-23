program main
    use LinearAlgebra
    implicit none
    integer:: i, j, N
    real*8, allocatable, dimension(:,:):: T, V, H
    real*8, allocatable, dimension(:):: eigval

    N = 1001

    allocate(H(N, N))
    allocate(T(N, N))
    allocate(V(N, N))
    allocate(eigval(N))
    
    do i = 1, N
        do j = 1, N
            if (j/=i) then
                V(i,j)=0
            else
                V(i,j)=0.5*1*(-5+i*0.01)**2
            end if
        end do
    end do

    do i = 1, N
        do j = 1, N
            if (j==i) then
                T(i,j)=(-2)/(0.01*0.01)
            else if (j==i+1 .or. j==i-1) then
                T(i,j)=1/(0.01*0.01)
            else
                T(i,j)=0
            end if
        end do
    end do
    T = (-1.0)/(2.0*1.0) * T

    !write(*,*)T(1,1), T(1,2), T(2,1), T(2,2), T(2,3)

    H=T+V
    call My_dsyev('V', H, eigval, N)

    write(*,*)eigval(1), eigval(2), eigval(3)

end program main
