import matplotlib.pyplot as plt


class Noeud:

    def __init__(self, valeur):
        self.valeur = valeur                    #
        self.enfants = [] 

    def __repr__(self):
        return f"Noeud({self.valeur})"

    def add_noeud(self,enfant) : 
        self.enfants.append(enfant)

    def ecriture_polonaise(self) : 
        texte = str(self.valeur)
        for x in self.enfants : 
            texte += " " + x.ecriture_polonaise()
        return texte

    def affiche_polonaise(self) : 
        print(self.ecriture_polonaise())

    def evaluer(self, dic) :
        res = 0
        if isinstance(self.valeur,(int,float)): 
            return self.valeur
        if len(self.enfants) == 0 : 
            if self.valeur not in dic : 
                raise ValueError 
            return dic[self.valeur]


        #cas 3 : Existance d'un operateur. 
        gauche = self.enfants[0].evaluer(dic)
        droite  = self.enfants[1].evaluer(dic)

        if self.valeur in ("+","add") : 
            return gauche + droite 
        elif self.valeur in ("-") : 
            return gauche - droite 
        elif self.valeur in ("mul","*") : 
            return gauche*droite 


    def tracer(self, variable , valeurs): 
        res = [] 
        for x in valeurs : 
            res.append(self.evaluer({variable : x}))
        plt.plot(valeurs,res) 
        plt.show()

        





