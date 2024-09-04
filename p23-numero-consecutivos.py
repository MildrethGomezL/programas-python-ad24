#  Tres numeros indica si son o no consecutivos 

print("Dame 3 numeros separados para saber si son consecutivos ")
n1, n2, n3 = map(int, input().split())

if n2 - n1 == 1 and n3 - n2 == 1:
    print("\nSon numeros consecutivos\n")
  
else:
    print("\nNo son numeros consecutivos\n")    