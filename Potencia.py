""""Programa para calcular la potencia de "a" a la "b" """

print ("-------------------------------------")
print ("--------POTENCIA--- a ^ b------------")

# input
a= input ("Ingrese un nùmero: ")
a= int (a)
b= input ("A que número lo quiere elevar: ")
b= int (b)

#Processing 
c= a**b

# Output
print (str (a) + " elevado a la "+ str(b)+ " es igual a " + str(c))
