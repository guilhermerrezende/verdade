import itertools

def calcular_sentenca(P, Q, M):
   
    p_implies_q = not P or Q
    p_or_q = P or Q
    m_implies_r = not M or p_or_q
    not_p = not P
    not_p_implies_m_implies_r = not_p or m_implies_r
    r = (p_or_q and p_or_q) or (not_p and m_implies_r)


    return p_implies_q, p_or_q, m_implies_r, not_p, not_p_implies_m_implies_r, r

def gerar_tabela_verdade():
  
    tabela = []
    for P, Q, M in itertools.product([True, False], repeat=3):
        p_implies_q, p_or_q, m_implies_r, not_p, not_p_implies_m_implies_r, r = calcular_sentenca(P, Q, M)
        tabela.append({
            'P': P, 'Q': Q, 'M': M,
            'P → Q': p_implies_q,
            'P ∨ Q': p_or_q,
            'M → R': m_implies_r,
            '¬P': not_p,
            '¬P → (M → R)': not_p_implies_m_implies_r,
            'R (a festa é animada)': r
        })
    return tabela

def mostrar_tabela(tabela):
    
    print(f"{'P':<5} {'Q':<5} {'M':<5} {'P → Q':<8} {'P ∨ Q':<8} {'M → R':<8} {'¬P':<5} {'¬P → (M → R)':<15} {'R (a festa é animada)':<8}")
    print("-" * 80)
    for linha in tabela:
        print(f"{linha['P']:<5} {linha['Q']:<5} {linha['M']:<5} {linha['P → Q']:<8} {linha['P ∨ Q']:<8} {linha['M → R']:<8} "
              f"{linha['¬P']:<5} {linha['¬P → (M → R)']:<15} {linha['R (a festa é animada)']:<8}")

def verificar_sentenca(tabela):
   
    while True:
        try:
            P = bool(int(input("Digite 1 para Verdadeiro ou 0 para Falso para P (Ana vai à festa): ")))
            Q = bool(int(input("Digite 1 para Verdadeiro ou 0 para Falso para Q (Bruno vai à festa): ")))
            M = bool(int(input("Digite 1 para Verdadeiro ou 0 para Falso para M (Bruno traz música): ")))
        except ValueError:
            print("Entrada inválida. Digite apenas 1 (Verdadeiro) ou 0 (Falso).")
            continue

       
        for linha in tabela:
            if linha['P'] == P and linha['Q'] == Q and linha['M'] == M:
                resultado = linha['R (a festa é animada)']
                print(f"\nCom P={P}, Q={Q}, e M={M}, a sentença 'A festa é animada' é {'VERDADEIRA' if resultado else 'FALSA'}.\n")
                break

        
        outra_verificacao = input("Deseja verificar outra combinação? (s/n): ").strip().lower()
        if outra_verificacao != 's':
            break


tabela_verdade = gerar_tabela_verdade()
mostrar_tabela(tabela_verdade)
verificar_sentenca(tabela_verdade)
