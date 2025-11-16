import sys
from pathlib import Path
from parser_sistemas import parse_systems_from_file
from gauss_solver import gaussian_elimination

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py arquivo.dat")
        sys.exit(1)

    path = sys.argv[1]

    if not Path(path).exists():
        print(f"Arquivo não encontrado: {path}")
        sys.exit(1)

    systems = parse_systems_from_file(path)

    for idx, (A, B) in enumerate(systems, start=1):
        print(f"\n--- Sistema #{idx} (N={len(A)}) ---")

        try:
            X = gaussian_elimination(A, B)
            for i, xi in enumerate(X, start=1):
                print(f"x[{i}] = {xi:.2f}")
        except Exception as e:
            print(f"Erro ao resolver sistema #{idx}: {e}")

if __name__ == "__main__":
    main()
