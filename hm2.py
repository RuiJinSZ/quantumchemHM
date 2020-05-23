import numpy
import numpy.linalg
import matplotlib.pyplot as plt

N = 1001

def potential(x):
    v = 0.5 * 1.0 * x**2
    return v

if __name__ == "__main__":
    H = numpy.empty((N,N))
    T = numpy.empty((N,N))
    V = numpy.empty((N,N))

    x = numpy.linspace(-5, 5, N, endpoint=True)
    dx = x[1] - x[0]

    for i in range(N):
        for j in range(N):
            if j != i:
                V[i,j] = 0
            else:
                V[i,j] = potential(x[i])

    for i in range(N):
        for j in range(N):
            if j ==i:
                T[i,j] = (-0.5)*(-2)/(dx*dx)
            elif j ==i+1 or j ==i-1:
                T[i,j] = -(1/2)/(dx*dx)
            else:
                T[i,j] = 0


    H = T + V
    eigval, eigvec = numpy.linalg.eigh(H)

    print(eigval[0], eigval[1], eigval[2])

    plt.plot(x, eigvec[:,2])
    plt.show()