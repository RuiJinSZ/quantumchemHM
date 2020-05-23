import numpy
import numpy.linalg

N = 1001

def potential(x):
    v = 0.5 * 1.0 * x**2
    return v

if __name__ == "__main__":
    H = numpy.empty((N,N))
    T = numpy.empty((N,N))
    V = numpy.empty((N,N))

    x = numpy.linspace(-5, 5, N, endpoint=True)

    for i in range(N):
        for j in range(N):
            if j != i:
                V[i,j] = 0
            else:
                V[i,j] = potential(x[i])

    
    H = T + V
    eigval, eigvec = numpy.linalg.eigh(H)

    print(eigval[0], eigval[1], eigval[2])