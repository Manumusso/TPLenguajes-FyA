mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
minusculas = 'abcdefghijklmnopqrstuvwxyz'
LAMBDA = 0
reservadas = ["lambda"]
Listfolows=[]
First=[]
class Gramatica():

    def GetFirsts(self):
        Firsts = [None] * len(self.Antecedentes)
        LookingFor = []
        n = 0
        for var in self.Antecedentes:
            # First para n elemento
            consecSplitted = self.Consecuentes[n].split(' ')
            if (consecSplitted[0] in self.Terminales or consecSplitted[0] == reservadas[LAMBDA]):
                Firsts[n] = [consecSplitted[0]]
            else:
                Firsts[n] = []
                LookingFor.append([n, consecSplitted[0], 0])
            n += 1
        for noTerminal in LookingFor:
            for x in range(0, len(self.Antecedentes)):
                if (x == noTerminal[0]):
                    continue

                if (self.Antecedentes[x] == noTerminal[1]):
                    Firsts[noTerminal[0]] = list(set(Firsts[x]) | set(Firsts[noTerminal[0]]))
                    if (reservadas[LAMBDA] in Firsts[x]):
                        consecSplitted = self.Consecuentes[noTerminal[0]].split(' ')
                        if len(consecSplitted) > noTerminal[2] + 1:
                            if (consecSplitted[noTerminal[2] + 1] in self.Terminales or consecSplitted[
                                noTerminal[2]] == reservadas[LAMBDA]):
                                if (consecSplitted[noTerminal[2]] not in Firsts[noTerminal[0]]):
                                    Firsts[noTerminal[0]].append(consecSplitted[noTerminal[2]])
                            else:
                                LookingFor.append([noTerminal[0], consecSplitted[noTerminal[2] + 1], noTerminal[2] + 1])
                            print(noTerminal[0])
                            print(Firsts)
                            if(reservadas[LAMBDA] in Firsts[noTerminal[0]]):
                                Firsts[noTerminal[0]].remove(reservadas[LAMBDA])

        return Firsts

    def GetFirstByLetter(self,letra):
        firstsLetra = []
        for index in range(0, len(self.Antecedentes)):
            if (letra == self.Antecedentes[index]):
                    firstsLetra = list(set(self.Firsts[index])|set(firstsLetra))
        return firstsLetra

    def HasRecursivity(self):
        pass

    def HasCommonFactor(self):
        terminalsDicc = {}
        for index in range(len(self.Antecedentes)):
            consSplitted = self.Consecuentes[index].split(" ")
            if(terminalsDicc.get(self.Antecedentes[index]) is not None):
                if(consSplitted[0] in terminalsDicc[self.Antecedentes[index]]):
                    print(terminalsDicc)
                    return True
                else:
                    terminalsDicc[self.Antecedentes[index]].append(consSplitted[0])
            else:
                terminalsDicc[self.Antecedentes[index]] = [consSplitted[0]]
        print(terminalsDicc)
        return False
    def Search_Follows_Antecedent(self,indiceRegla,Listfolows,indicons):
        Lfolows = []
        conseSplitted=[]
        Letrafolows = self.Antecedentes[indiceRegla]
        for i2 in range(0, len(self.Consecuentes)):
            for k in range (0,len(self.Consecuentes[i2])):
                conseSplitted = self.Consecuentes[i2].split(' ')
            for j in range(0, len(conseSplitted)):
                if (i2 == indiceRegla) and (j == indicons):
                    LetraLook = conseSplitted[j]
        for ii in range(0 ,len(self.Antecedentes)):
            if (ii == indiceRegla) and (Letrafolows != LetraLook):
                    Gramatica.Search_follows(self, Letrafolows)





    def Calculate_Follows(self,nt):

        Gramatica.Search_follows(self,nt)

        return Listfolows


    def recurfollows(self,r,tamindice,reglaindice,ListSplitted):
        FirstSi= []
        r=r+1
        band =False

        if (tamindice - 1) > r:
            NoTerminales = Gramatica.NoyT(self, True)
            Terminales = Gramatica.NoyT(self, False)
            if ListSplitted[r+1] in (NoTerminales):
                band = False
                FirstSi = Gramatica.GetFirsts(self,conseSplitted[j+1])
                for aux in range(0, len(FirstSi)):
                    if ((FirstSi[aux] not in reservadas) and (FirstSi[aux] not in Listfolows)):
                        Listfolows.append(FirstSi[aux])
                    else:
                        if (FirstSi[aux] == "lambda"):
                            band = True
                if band:
                    a2 = r
                    a2 += 1
                    Gramatica.recurfollows(self, a2, tamindice, reglaindice, ListSplitted)
            else:
                if ListSplitted[r+1] in (Terminales):
                    terminal = conseSplitted[a2+1]
                    if terminal not in Listfolows:
                        Listfolows.append(terminal)
        else:
            # Buscar folows del antecedente de la regla (Falta probar)
            Gramatica.Search_Follows_Antecedent(Antecedentes, reglaindice,Listfolows,r)


    def Search_follows(self,nt):
        consecu = []
        FirstSi = []
        if ((Gramatica.IsAxiom(self,nt)) == True):
            Listfolows.append('$')

        for i in range(0, len(self.Consecuentes)):
            for k in range (0,len(self.Consecuentes[i])):
                conseSplitted = self.Consecuentes[i].split(' ')
            for j in range (0,len(conseSplitted)):
                if (nt== conseSplitted[j]):
                    tamanindice = len(conseSplitted)
                    if (tamanindice-1) > j:
                        if conseSplitted[j+1] in (self.NoTerminales):
                            band = False
                            FirstSi = Gramatica.GetFirstByLetter(self,conseSplitted[j+1])

                            for aux in range(0, len(FirstSi)):
                                if ((FirstSi[aux] not in reservadas) and (FirstSi[aux] not in Listfolows)):
                                        Listfolows.append(FirstSi[aux])
                                else:
                                    if (FirstSi[aux]== "lambda"):
                                        band = True
                            if band:
                                global r
                                r=j
                                r+=1
                                Gramatica.recurfollows(self,r,tamanindice,i,conseSplitted)
                        else:
                            if conseSplitted[j+1] in (self.Terminales):
                                terminal = conseSplitted[j+1]
                                if terminal not in Listfolows:
                                    Listfolows.append(terminal)
                    else:
                        # Buscar folows del antecedente de la regla (Falta probar)
                        Gramatica.Search_Follows_Antecedent(self,i,Listfolows,j)

    def IsAxiom(self,nt):
        if self.Antecedentes[0] == nt:
            return True
        else:
            return False


    def ConstruirReglas(self,band):
        """
        Construir Reglas: Devuelve Lista de antecedentes y Consecuentes.

        True: Devuelve la lista de antecedentes
        False: Devuelve la lista de consecuentes


        """
        separador1 = "\n"
        Lista1 = self.gramatica.split(separador1)
        ListaReglas = []
        LineaAntecedentes= []
        LineaConsecuentes= []
        Linea = []

        for i in range(0, len(Lista1)):
            ListaReglas.append(Lista1[i].split(":"))

        distin=0

        for i in range(0, len(ListaReglas)):
            List = ListaReglas[i]

            if (distin==0):
                LineaAntecedentes.append(List[0])
                LineaConsecuentes.append(List[1])
                distin == 1

            else:
                LineaAntecedentes.append(List[i])
                LineaConsecuentes.append(List[i+1])
                i=i+2

        if band==True:
            return LineaAntecedentes
        else:
            return LineaConsecuentes

        pass
    def NoyT(self,bandera):
        """  Noyt: Devuelve Lista de antecedentes y Consecuentes.
        True: Devuelve la lista de terminales
        False: Devuelve la lista de no terminales
        """
        values = []

        for antecedente in self.Antecedentes:
            antecedenteSplitted = antecedente.split(' ')
            for terminalNoTerminal in antecedenteSplitted:
                if(bandera):
                    if (terminalNoTerminal in mayusculas and terminalNoTerminal not in values):
                        values.append(terminalNoTerminal)
                else:
                    if(terminalNoTerminal in minusculas and terminalNoTerminal not in values):
                        values.append(terminalNoTerminal)
         
        
        for consecuente in self.Consecuentes:
            consecuenteSplitted = consecuente.split(' ')
            for terminalNoTerminal in consecuenteSplitted:
                if(bandera):
                    if (terminalNoTerminal in mayusculas and terminalNoTerminal not in values):
                        values.append(terminalNoTerminal)
                else:
                    if((terminalNoTerminal in minusculas or terminalNoTerminal == reservadas[LAMBDA])and terminalNoTerminal not in values):
                        values.append(terminalNoTerminal)

        return values


    def __init__(self,gramatica):
        """Constructor de la clase.

        Parameters
        ----------
        gramatica : string
            Representación de las producciones de una gramática determinada.

            Ejemplo:
            "A:b A\nA:a\nA:A B c\nA:lambda\nB:b"

        """
        self.gramatica = gramatica
        self.Antecedentes = Gramatica.ConstruirReglas(self, True)
        self.Consecuentes = Gramatica.ConstruirReglas(self, False)
        self.Terminales = Gramatica.NoyT(self,False)
        self.NoTerminales = Gramatica.NoyT(self, True)
        self.Firsts = Gramatica.GetFirsts(self)

        self.CalcularFolows = Gramatica.Calculate_Follows(self,"S")

    def isLL1(self):
        """Verifica si una gramática permite realizar derivaciones utilizando
           la técnica LL1.

        Returns
        -------
        resultado : bool
            Indica si la gramática es o no LL1.
        """
        pass

    def parse(self, cadena):
        """Retorna la derivación para una cadena dada utilizando las
           producciones de la gramática y los conjuntos de Fi, Fo y Se
           obtenidos previamente.

        Parameters
        ----------
        cadena : string
            Cadena de entrada.

            Ejemplo:
            babc

        Returns
        -------
        devivacion : string
            Representación de las reglas a aplicar para derivar la cadena
            utilizando la gramática.
        """
        pass
    def ImprimirPrueba(self):
        print("Gramatica: ")
        print(self.gramatica)
        print("Antecedentes: ")
        print(self.Antecedentes)
        print("Consecuentes: ")
        print(self.Consecuentes)
        print("No terminales: ")
        print(self.NoTerminales)
        print("Terminales: ")
        print(self.Terminales)
        print("Firsts: ")
        print(self.Firsts)
        print("Folows")
        print(self.CalcularFolows)
        print("Tiene Factor Comun")
        print(Gramatica.HasCommonFactor(self))


        pass

# Pruebas:
"""
A:b A   
A:a
A:A B c
A: lambda
B: b

"""
gramatica = "S:A B\nA: a A\nA:c\nA:lambda\nB:b B\nB:d"
prueba = Gramatica(gramatica)
prueba.ImprimirPrueba()

