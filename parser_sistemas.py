from pathlib import Path

def parse_systems_from_file(path: str):
    """
    Lê um arquivo contendo um ou mais sistemas lineares e retorna
    uma lista de tuplas (A, B).
    """
    text = Path(path).read_text()

    tokens = text.replace(",", ".").split()

    values = []
    for t in tokens:
        try:
            values.append(float(t))
        except ValueError:
            pass

    systems = []
    i = 0

    while i < len(values):
        if i >= len(values):
            break

        N = int(round(values[i]))
        i += 1

        if N <= 0:
            raise ValueError(f"Tamanho inválido N={N}")

        total_needed = N * N + N
        if i + total_needed > len(values):
            raise ValueError(
                f"Arquivo terminou antes de completar o sistema {N}x{N}."
            )

        A = []
        for _ in range(N):
            row = values[i:i+N]
            A.append(row)
            i += N

        B = values[i:i+N]
        i += N

        systems.append((A, B))

    return systems
