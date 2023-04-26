def ler_numero():
    while True:
        try:
            inteiro = int(input("Insira um número"))       
        except ValueError:
            print("Não inseriu um número")
            continue
        else:
            return inteiro
        
def imprime_resultados(n,positivo,par):
    print(f"Número inserido: {n}, Positivo: {positivo}, Par: {par}")

def menu():
    """Menu"""
    
    for i in [ler_numero,imprime_resultados,menu]:
        print(f"{i.__name__}: {i.__doc__}")