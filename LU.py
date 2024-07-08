import numpy as np

def doolittle(mat):
    n = len(mat)
    L = np.zeros((n, n))  # Sakhtane matrice L ba andaze (n, n) va meghdare avalie 0
    U = np.zeros((n, n))  
    
    for i in range(n):
        L[i][i] = 1  # Meghdare araye ghotri matrice L ra barabar ba 1 gharar midahim
        for j in range(i, n):
            sum_U = sum(L[i][k] * U[k][j] for k in range(i))  # Mohasebe majmooe L[i][k] * U[k][j] baraye k az 0 ta i
            U[i][j] = mat[i][j] - sum_U  # Mohasebe meghdare U[i][j]
            
        for j in range(i + 1, n):
            sum_L = sum(L[j][k] * U[k][i] for k in range(i))  # Mohasebe majmooe L[j][k] * U[k][i] baraye k az 0 ta i
            L[j][i] = (mat[j][i] - sum_L) / U[i][i]  # Mohasebe meghdare L[j][i]
    
    return L, U

def crout(mat):
    n = len(mat)
    L = np.zeros((n, n))  # Sakhtane matrice L ba andaze (n, n) va meghdare avalie 0
    U = np.zeros((n, n))  
    
    for j in range(n):
        U[j][j] = 1  # Meghdare araye ghotri matrice U ra barabar ba 1 gharar midahim
        for i in range(j, n):
            sum_L = sum(L[i][k] * U[k][j] for k in range(j))  # Mohasebe majmooe L[i][k] * U[k][j] baraye k az 0 ta j
            L[i][j] = mat[i][j] - sum_L  # Mohasebe meghdare L[i][j]
            
        for i in range(j + 1, n):
            sum_U = sum(L[j][k] * U[k][i] for k in range(j))  # Mohasebe majmooe L[j][k] * U[k][i] baraye k az 0 ta j
            U[j][i] = (mat[j][i] - sum_U) / L[j][j]  # Mohasebe meghdare U[j][i]
    
    return L, U

def get_matrix():
    n = int(input("Andaze matrice n ra vared konid: "))
    mat = []
    for i in range(n):
        row = []
        for j in range(n):
            val = float(input(f"Adade {j + 1} az satre {i + 1} ra vared konid: "))  
            row.append(val)  
        mat.append(row)  
    return np.array(mat)


def is_invertible(mat):
    n = mat.shape[0]
    for i in range(1, n+1):
        if np.linalg.det(mat[:i, :i]) == 0:  # Mohasebe determinant zirmatrice asli pishro
            return False  # Agar determinant sefr bashad, matrice makoos pazir nist
    return True  # matrice makoos pazir ast

def main():
    while True:
        print("Lotfan yek gozine ra entekhab konid:")
        print("1. Tajzie LU be raveshe Doolittle")
        print("2. Tajzie LU be raveshe Crout")
        print("3. Khoroje")
        
        choice = input("Entekhab: ")
        
        if choice == '3':
            break
        
        mat = get_matrix()
        
        if not is_invertible(mat):
            print("Error: Matrice ghabele tajzie shodan be LU nist")
            continue
        
        if choice == '1':
            L, U = doolittle(mat)
            print("Matrice L (raveshe Doolittle):")
            print(L)
            print("Matrice U (raveshe Doolittle):")
            print(U)
        elif choice == '2':
            L, U = crout(mat)
            print("Matrice L (raveshe Crout):")
            print(L)
            print("Matrice U (raveshe Crout):")
            print(U)
        else:
            print("Entekhab namotabar ast.")

if __name__ == "__main__":
    main()
