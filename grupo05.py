mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
minusculas = 'abcdefghijklmnopqrstuvwxyz'
LAMBDA = 0
reservadas = ["lambda"]
Listfolows=[]
First=[]
import corrector

class Gramatica():

# Metodos para calcular first
    def GetFirsts(self):
        Firsts = [None] * len(self.Antecedentes)
        LookingFor = []
        n = 0
        for var in self.Antecedentes:
            consecSplitted = self.Consecuentes[n].split(' ')
            if (consecSplitted[0] in self.Terminales or consecSplitted[0] == reservadas[LAMBDA]):
                Firsts[n] = [consecSplitted[0]]
            else:
                Firsts[n] = []
                LookingFor.append([n, consecSplitted[0], 0])
            n += 1

        maxNoTerminal = len(LookingFor)
        index = 0
        while index < maxNoTerminal:
            noTerminal = LookingFor[index]

            if(noTerminal[1] in list(map(lambda x: self.Antecedentes[x],list(map(lambda x: x[0], LookingFor[index+1:]))))):
                LookingFor.append(noTerminal)
                maxNoTerminal = len(LookingFor)
                index+=1
                continue

            for x in range(0, len(self.Antecedentes)):
                if (x == noTerminal[0]):
                    continue
                    x+=1
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
                            if(reservadas[LAMBDA] in Firsts[noTerminal[0]]):
                                Firsts[noTerminal[0]].remove(reservadas[LAMBDA])

            maxNoTerminal = len(LookingFor)
            index+=1
        return Firsts

    def GetFirstByLetter(self,letra):
        firstsLetra = []
        for index in range(0, len(self.Antecedentes)):
            if (letra == self.Antecedentes[index]):
                    firstsLetra = list(set(self.Firsts[index])|set(firstsLetra))
        return firstsLetra


# Metodos para calcular Selects
    def GetSelects(self):
        Selects = [None] * len(self.Antecedentes)
        for index in range(len(self.Antecedentes)):
            Selects[index] = self.Firsts[index].copy()
            if(reservadas[LAMBDA] in Selects[index]):
                Selects[index].remove(reservadas[LAMBDA])
                Selects[index] = list(set(Selects[index]).union(set(self.Folows.get(self.Antecedentes[index]))))
        return Selects


# Recursividad y Factor Comun
    def HasRecursivity(self):
        for index in range(len(self.Antecedentes)):
            consSplitted = self.Consecuentes[index].split(" ")
            if(consSplitted[0] == self.Antecedentes[index]):
                return True

        return False

    def HasCommonFactor(self):
        terminalsDicc = {}
        for index in range(len(self.Antecedentes)):
            consSplitted = self.Consecuentes[index].split(" ")
            if(terminalsDicc.get(self.Antecedentes[index]) is not None):
                if(consSplitted[0] in terminalsDicc[self.Antecedentes[index]]):
                    return True
                else:
                    terminalsDicc[self.Antecedentes[index]].append(consSplitted[0])
            else:
                terminalsDicc[self.Antecedentes[index]] = [consSplitted[0]]
        return False


# Follows
    def Search_Follows_Antecedent(self,indiceRegla,Listfolows,indicons):
        Lfolows = []
        conseSplitted=[]
        Letrafolows = self.Antecedentes[indiceRegla]
        for i2 in range(0, len(self.Consecuentes)):
            for k in range (0,len(self.Consecuentes[i2])):
                conseSplitted = self.Consecuentes[i2].split(' ')
            for j in range(0, len(conseSplitted)):
                if (i2 == indiceRegla):
                    Gramatica.Search_follows(self, Letrafolows)
            break

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
            Bandauxiliar = False
            FirstAux = self.GetFirstByLetter(self.Consecuentes[reglaindice][r])
            for j1 in range(0, len(FirstAux)):
                if  (FirstAux[j1] == reservadas[LAMBDA]):
                    Bandauxiliar = True
            if (Bandauxiliar) and ("$") not in Listfolows:
                Listfolows.append("$")
            Gramatica.Search_Follows_Antecedent(self, reglaindice,Listfolows,r)

    def Search_follows(self,nt):
        consecu = []
        FirstSi = []
        if ((Gramatica.IsAxiom(self,nt)) == True) and (('$') not in Listfolows):
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
                        Gramatica.Search_Follows_Antecedent(self,i,Listfolows,j)

    def CalcularFollows(self):
        dicFollows = {}
        noterminals = self.NoTerminales
        for id in range(0,len(noterminals)):
            dicFollows[noterminals[id]] = Gramatica.Calculate_Follows(self,noterminals[id]).copy()
            Listfolows.clear() #Limpiamos la lista de follows general.

        return dicFollows


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
                if(not bandera):
                    if (terminalNoTerminal in mayusculas and terminalNoTerminal not in values):
                        values.append(terminalNoTerminal)
                else:
                    if(terminalNoTerminal in minusculas and terminalNoTerminal not in values):
                        values.append(terminalNoTerminal)


        for consecuente in self.Consecuentes:
            consecuenteSplitted = consecuente.split(' ')
            for terminalNoTerminal in consecuenteSplitted:
                if(not bandera):
                    if (terminalNoTerminal in mayusculas and terminalNoTerminal not in values):
                        values.append(terminalNoTerminal)
                else:
                    if((terminalNoTerminal in minusculas or terminalNoTerminal == reservadas[LAMBDA])and terminalNoTerminal not in values):
                        values.append(terminalNoTerminal)

        return values


    def IsCalculate(self):
        IsCalculate = False
        ListaAux = []

        for i in range(0, len(self.Consecuentes)):
            for k in range(0, len(self.Consecuentes[i])):
                conseSplit = self.Consecuentes[i].split(' ')
            for index in range(0, len(conseSplit)):
                if (conseSplit[index] in self.NoTerminales):
                    for indexa in range(0, len(self.Antecedentes)):
                        if (conseSplit[index] == self.Antecedentes[indexa]) and (conseSplit[index] not in ListaAux):
                            ListaAux.append(conseSplit[index])
        if self.Antecedentes[0] not in ListaAux:
            ListaAux.append(self.Antecedentes[0])
        if len(ListaAux) == len(self.NoTerminales):
            IsCalculate = True

        return IsCalculate

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
        self.Terminales = Gramatica.NoyT(self,  True)
        self.NoTerminales = Gramatica.NoyT(self, False)

        self.IsCalculate = Gramatica.IsCalculate(self)

        if self.IsCalculate:
            self.Firsts = Gramatica.GetFirsts(self)
            self.Folows = Gramatica.CalcularFollows(self)
            self.Selects = Gramatica.GetSelects(self)




    def isLL1(self):
            """Verifica si una gramática permite realizar derivaciones utilizando
               la técnica LL1.

            Returns
            -------
            resultado : bool
                Indica si la gramática es o no LL1.
            """

            if (Gramatica.HasRecursivity(self)):
                return False
            if Gramatica.HasCommonFactor(self):
                return False
            if self.IsCalculate:
                dicc = {}
                for index in range(0, len(self.Antecedentes)):
                    if dicc.get(self.Antecedentes[index]) is not None:
                            for element in self.Selects[index]:
                                if(element in dicc[self.Antecedentes[index]]) and (dicc.keys() == self.Antecedentes[index]):
                                    return False
                            dicc[self.Antecedentes[index]] = list(set(dicc[self.Antecedentes[index]]).union(set(self.Selects[index])))
                    else:
                        dicc[self.Antecedentes[index]] = self.Selects[index]
            else:
                return False
                
            return True



    def parse(self,cadena):
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
        cadenav = cadena.split(' ')
        stringListed = list(cadenav)
        steps = list()
        steps.append(self.Antecedentes[0])
        rangeStr = len(stringListed)

        while True:
            input = stringListed[0]

            nextNoTerminal =""
            stepSplitted = steps[len(steps)-1].split(' ')
            stepSplitted = list(filter(Gramatica.isNoTerminal, stepSplitted))

            if len(stepSplitted) > 0:
                nextNoTerminal = stepSplitted[0]
            else:
                if(input == '$'):
                    if(reservadas[LAMBDA] in steps[len(steps)-1].split(" ")):
                         steps[len(steps)-1] = steps[len(steps)-1].replace(" " + reservadas[LAMBDA],"")
                    return "=>".join(steps)
                else:
                    return "=>".join([])


            isASelect = False
            for index in range(len(self.Antecedentes)):
                if(self.Antecedentes[index] == nextNoTerminal):
                    if(input in self.Selects[index]):
                        isASelect = True
                        steps.append(steps[len(steps)-1].replace(nextNoTerminal,self.Consecuentes[index],1))
                        if(input == self.Consecuentes[index].split(' ')[0]):
                            stringListed.pop(0)
                        break

            if(not isASelect):
                return "=>".join([])
        return "=>".join(steps)


    def isNoTerminal(value):
        return value in mayusculas
