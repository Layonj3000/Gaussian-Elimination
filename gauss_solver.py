def gaussian_elimination(A, B, eps=1e-12):
    """
    Resolve o sistema linear Ax = B usando Eliminação de Gauss
    com pivotamento parcial.
    """
    N = len(A)

    M = [row[:] for row in A]
    Y = B[:]

    # Eliminação direta
    for k in range(N):
        # Encontrar maior pivô
        max_row = max(range(k, N), key=lambda r: abs(M[r][k]))
        if abs(M[max_row][k]) < eps:
            raise ValueError(f"Matriz singular ou quase singular na coluna {k}.")

        if max_row != k:
            M[k], M[max_row] = M[max_row], M[k]
            Y[k], Y[max_row] = Y[max_row], Y[k]

        pivot = M[k][k]

        for i in range(k + 1, N):
            factor = M[i][k] / pivot
            for j in range(k, N):
                M[i][j] -= factor * M[k][j]
            Y[i] -= factor * Y[k]

    # Substituição regressiva
    X = [0.0] * N
    for i in range(N - 1, -1, -1):
        soma = Y[i] - sum(M[i][j] * X[j] for j in range(i + 1, N))

        if abs(M[i][i]) < eps:
            raise ValueError(f"Pivô zero na linha {i}. Sistema inconsistente.")

        X[i] = soma / M[i][i]

    return X
