# Proiect MAP - Valentin Maria

Problemă Celor 8 Turnuri pe Tabla de Șah

Această implementare rezolvă problema Celor 8 Turnuri pe o tablă de șah de dimensiunea 8x8. Scopul este de a plasa 8 turnuri pe tablă astfel încât niciunul dintre ele să nu se atace reciproc. Soluția este realizată utilizând un algoritm de backtracking.

Structura fișierului:
- turnuri.py: Conține codul sursă al programului.
  
Funcții principale:
1. `is_safe(board, row, col)`: Verifică dacă este în siguranță să plasezi un turn la poziția (row, col) pe tabla de șah.
2. `solve_tower_problem_util(board, row, solutions)`: Funcție utilitară de backtracking care găsește toate soluțiile posibile pentru problema turnurilor.
3. `generate_all_solutions()`: Generează toate soluțiile posibile pentru problema celor 8 turnuri.
4. `print_board(board)`: Afișează tabla de șah.

Utilizare:
1. Rulați scriptul `turnuri.py` într-un mediu Python.

Exemplu de utilizare:
```python
python turnuri.py
