entrada = input("A B C").split()
A, B, C = int(entrada[0]), int(entrada[1]), int(entrada[2])
if A < 1 or A > 300 or B < 1 or B > 300 or C < 1 or C > 300:
    raise ValueError("Deu Erro")
entrada = input("Qual a altura e largura").split()
H, L = int(entrada[0]), int(entrada[1])
if H < 1 or H > 250 or L < 1 or L > 250:
    raise ValueError("Deu Erro")
if (A and B) > (H and L) or (A and C) > (H and L) or (B and C) > (H and L):
    print ("N")
else:
    print("S")
    
#https://pt.stackoverflow.com/q/454645/101
