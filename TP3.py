from noeud import Noeud 


exp = Noeud("exp")
x = Noeud("x")
y = Noeud("y")
n2 = Noeud(2)
n3 = Noeud(3)


print(exp.valeur)
print(n3.valeur)


# Creation de l'arbre : 

#Arbre 1 

mul = Noeud("mul")    #declaration du Noeud mul
mul.add_noeud(x)      #Je rajoute un enfant x
mul.add_noeud(n3)     #Je rajoute un enfant n3 = 3


print(exp.enfants)
print(mul.enfants)
mul.affiche_polonaise()


#Arbre 2  

"""

mul.add_noeud(n2)
mul.add_noeud(y)
mul.affiche_polonaise()

"""



dico = { "x" : 3 }
print(mul.evaluer(dico))
mul.tracer("x",[-3,-2,-1,0,1,2,3])












