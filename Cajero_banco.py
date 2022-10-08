# Programa N. 7. repeticiones:  El cajero de un banco solo dispone de billetes de $10000, $2000 y monedas de $100. Su función es cambiar los cheques a los clientes, 
# dándoles el menor número posible de billetes. Asumiendo que todos los cheques son múltiples de $100, hacer el diagrama de flujo y el programa en Python que 
# reciba el valor del cheque a cambiar y que le informe al cajero cuántos billetes de cada denominación debe entregar. Como no se sabe cuántos clientes vienen en un día, 
# el programa debe terminar cuando reciba cero como valor del cheque, y al final del día debe informar cuántos billetes de cada denominación se gastaron.

from os import system

print("\n------------------------------------------------")
print("-------------- Programa cajero -------------------")
print("------------------------------------------------\n")

B10k=0
B2k=0
M100=0
Total_B10k=0
Total_B2k=0
Total_M100=0

#input
cheque=int(input("\n Ingrese el valor del cheque que desea cambiar: "))

#processing
while cheque!=0:
    B10k=cheque//10000
    B2k=(cheque-(B10k*10000))//2000
    M100=((cheque-(B10k*10000))-(B2k*2000))//100
    Total_B10k=Total_B10k+B10k
    Total_B2k=Total_B2k+B2k
    Total_M100=Total_M100+M100
    cheque=int(input("\n Ingrese el valor del cheque que desea cambiar: "))

#output
print("------------------------------------------------------------------------")
print("\n EL total de billetes de 10.000 entregados fue de: "+str(Total_B10k))
print(" El total de billetes de 2.000 entregados fue de:  "+str(Total_B2k))
print(" El total de monedas de 100 entregadas fue de: "+str(Total_M100))
print(" ")