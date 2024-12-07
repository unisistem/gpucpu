import numpy as np
from timeit import default_timer as timer
from numba import vectorize

# Função vetorizada que será executada na GPU
@vectorize(["float32(float32, float32)"], target='cuda')
def VectorAdd(a, b):
    return a + b

def main():
    N = 32000000  # Número de elementos por array

    # Criação de arrays na CPU
    A = np.ones(N, dtype=np.float32)
    B = np.ones(N, dtype=np.float32)

    # Medir o tempo da operação na GPU
    start = timer()
    C = VectorAdd(A, B)  # Operação realizada na GPU
    vectoradd_time = timer() - start

    # Exibir os resultados
    print("C[:5] =", C[:5])  # Mostra os primeiros 5 elementos
    print("C[-5:] =", C[-5:])  # Mostra os últimos 5 elementos
    print("VectorAdd took %f seconds" % vectoradd_time)

if __name__ == '__main__':
    main()
