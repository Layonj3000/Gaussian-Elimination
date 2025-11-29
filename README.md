# 🧮 Eliminação Gaussiana

## 📝 Descrição
Este repositório contém uma implementação do método de Eliminação Gaussiana, um algoritmo fundamental em álgebra linear usado para resolver sistemas de equações lineares. O algoritmo transforma uma matriz em forma escalonada através de operações elementares de linha.

## ⚡ Funcionalidades
- Resolve sistemas de equações lineares
- Realiza redução de linhas para forma escalonada
- Funciona com matrizes quadradas e retangulares
- Inclui substituição reversa para encontrar soluções

## 📋 Requisito
- Python 3.x

## 🚀 Uso
1. Clone o repositório
2. Execute o programa Python com um arquivo de sistema
3. Veja a solução do sistema linear

## 💡 Exemplo
```bash
python main.py ./sistemas/sistema4x4.dat
```

Arquivo sistema4x4.dat:
```
4
5.0 2.0 0.0 -1.0
1.0 8.0 -3.0 2.0
0.0 1.0 6.0 1.0
1.0 -1.0 2.0 9.0
6.0 10.0 -5.0 0.0
```

Resultado:
```
--- Sistema #1 (N=4) ---

--- Forma decimal ---
x[1] = 0.95
x[2] = 0.71
x[3] = -0.98
x[4] = 0.19

--- Forma fracionada ---
x[1] = 19/20
x[2] = 71/100
x[3] = -49/50
x[4] = 19/100
```

## 👨‍💻 Autores 
<div>
  <table style="margin: 0 auto;">
    <tr>
      <td><a href="https://github.com/DavidPotentini"><img loading="lazy" src="https://avatars.githubusercontent.com/u/106561154?v=4" width="115"><br><sub>David Potentini</sub></a></td>
      <td><a href="https://github.com/Layonj300"><img loading="lazy" src="https://avatars.githubusercontent.com/u/106559843?v=4" width="115"><br><sub>Layon Reis</sub></a></td>
    </tr>
  </table>
</div>
