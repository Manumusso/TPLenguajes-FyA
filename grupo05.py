mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
minusculas = 'abcdefghijklmnopqrstuvwxyz'
LAMBDA = 0
reservadas = ["lambda"]
Listfolows=[]
class Gramatica():

    def GetFirsts(antec, consec, noTerminals):
        Firsts = [None] *len(antec) 
        LookingFor = []
        n = 0
        for var in antec:
            #First para n elemento 
            consecSplitted = consec[n].split(' ')
            if(consecSplitted[0] in noTerminals or consecSplitted[0] == reservadas[LAMBDA]):
                Firsts[n] = [consecSplitted[0]]
            else:
                Firsts[n] = []
                LookingFor.append([n, consecSplitted[0], 0])
            n+=1
        
        
        for noTerminal in LookingFor:
          #  if(noTerminal[1] in list(map(lambda x: x[1], LookingFor[n+1:]))):
          #      LookingFor.append(noTerminal)
          #      continue
        
                
            for x in range(0, len(antec)):
                if(x == noTerminal[0]):
                    continue

                if(antec[x] == noTerminal[1]):
                    Firsts[noTerminal[0]] = list(set(Firsts[x])|set(Firsts[noTerminal[0]]))
    
                    if(reservadas[LAMBDA] in Firsts[x]):
                        consecSplitted = consec[noTerminal[0]].split(' ')
                        if len(consecSplitted) > noTerminal[2] + 1:
                            if(consecSplitted[noTerminal[2] + 1] in noTerminals or consecSplitted[noTerminal[2]] == reservadas[LAMBDA]):
                                if(consecSplitted[noTerminal[2]] not in Firsts[noTerminal[0]]):
                                    Firsts[noTerminal[0]].append(consecSplitted[noTerminal[2]])
                            else:
                                LookingFor.append([noTerminal[0], consecSplitted[noTerminal[2] + 1], noTerminal[2] + 1])


        return Firsts




    def Search_Follows_Antecedent(Antecedentes,indiceRegla):
        for ii in range(0 ,len(Antecedentes)):
            if Antecedentes[ii] == indiceRegla:
                for rl in range(0, len(Listfollows)):
                    ## En este momento agrego los folows de la regla en que me encuentro posicionado a la lista
                    if Listfollows[rl] not in Listfollows:
                        Listfollows.append(Listfolows[rl])



    def Calculate_Follows(antecedentes,noterminal,Consecuentes):

        if (Gramatica.IsAxiom(antecedentes,noterminal) == True):
            Listfolows.append('$')
        Gramatica.Search_follows(Consecuentes,noterminal,antecedentes)

        return Listfolows


    def recurfollows(Antecedentes,r,tamindice,reglaindice,consecuentes,ListSplitted):
        FirstSi= []
        r=r+1
        band =False
        if (tamindice - 1) > r:
            NoTerminales = Gramatica.NoyT(Antecedentes, consecuentes, True)
            Terminales = Gramatica.NoyT(Antecedentes, consecuentes, False)
            if ListSplitted[r+1] in (NoTerminales):
                band = False
                # FirstSi = Gramatica.GetFirsts(Antecedentes,consec,conseSplitted[j+1])
                FirstSi=["d","lambda"]
                for aux in range(0, len(FirstSi)):
                    if ((FirstSi[aux] not in reservadas) and (FirstSi[aux] not in Listfolows)):
                        Listfolows.append(FirstSi[aux])
                    else:
                        if (FirstSi[aux] == "lambda"):
                            band = True
                if band:
                    a2 = r
                    a2 += 1
                    Gramatica.recurfollows(Antecedentes, a2, tamindice, reglaindice, consecuentes, ListSplitted)
            else:
                if ListSplitted[r+1] in (Terminales):
                    terminal = conseSplitted[a2+1]
                    if terminal not in Listfolows:
                        Listfolows.append(terminal)
        else:
            # Buscar folows del antecedente de la regla (Falta probar)
            Gramatica.Search_Follows_Antecedent(Antecedentes, reglaindice)

    def Search_follows(consec,nt,Antecedentes):
        consecu = []
        FirstSi = []

        for i in range(0, len(consec)):
            for k in range (0,len(consec[i])):
                conseSplitted = consec[i].split(' ')
            for j in range (0,len(conseSplitted)):
                if (nt== conseSplitted[j]):
                    tamanindice = len(conseSplitted)
                    if (tamanindice-1) > j:
                        NoTerminales = Gramatica.NoyT(Antecedentes, consec, True)
                        Terminales = Gramatica.NoyT(Antecedentes, consec, False)

                        if conseSplitted[j+1] in (NoTerminales):
                            band = False
                            #FirstSi = Gramatica.GetFirsts(Antecedentes,consec,conseSplitted[j+1])
                            FirstSi = ["b","lambda","c"]
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
                                Gramatica.recurfollows(Antecedentes,r,tamanindice,i,consec,conseSplitted)
                        else:
                            if conseSplitted[j+1] in (Terminales):
                                terminal = conseSplitted[j+1]
                                if terminal not in Listfolows:
                                    Listfolows.append(terminal)
                    else:
                        # Buscar folows del antecedente de la regla (Falta probar)
                        Gramatica.Search_Follows_Antecedent(Antecedentes,i)

    def IsAxiom(antec,noterminal):
        for i in range(0, len(antec)):
            if antec[i] == noterminal:
                return True
            else:
                return False


    def ConstruirReglas(gramatica,band):
        """
        Construir Reglas: Devuelve Lista de antecedentes y Consecuentes.

        True: Devuelve la lista de antecedentes
        False: Devuelve la lista de consecuentes


        """
        separador1 = "\n"
        Lista1 = gramatica.split(separador1)
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
    def NoyT(antecedentes,consecuentes,bandera):
        """  Noyt: Devuelve Lista de antecedentes y Consecuentes.
        True: Devuelve la lista de terminales
        False: Devuelve la lista de no terminales
        """
        values = []

        for antecedente in antecedentes:
            antecedenteSplitted = antecedente.split(' ')
            for terminalNoTerminal in antecedenteSplitted:
                if(bandera):
                    if (terminalNoTerminal in mayusculas and terminalNoTerminal not in values):
                        values.append(terminalNoTerminal)
                else:
                    if(terminalNoTerminal in minusculas and terminalNoTerminal not in values):
                        values.append(terminalNoTerminal)
         
        
        for consecuente in consecuentes:
            consecuenteSplitted = consecuente.split(' ')
            for terminalNoTerminal in consecuenteSplitted:
                if(bandera):
                    if (terminalNoTerminal in mayusculas and terminalNoTerminal not in values):
                        values.append(terminalNoTerminal)
                else:
                    if((terminalNoTerminal in minusculas or terminalNoTerminal == reservadas[LAMBDA])and terminalNoTerminal not in values):
                        values.append(terminalNoTerminal)

        return values


    def __init__(self,gramatica1):
        """Constructor de la clase.

        Parameters
        ----------
        gramatica : string
            Representación de las producciones de una gramática determinada.

            Ejemplo:
            "A:b A\nA:a\nA:A B c\nA:lambda\nB:b"

        """
        self.gramatica = gramatica1
        self.Antecedentes = Gramatica.ConstruirReglas(self.gramatica, True)
        self.Consecuentes = Gramatica.ConstruirReglas(self.gramatica, False)
        self.Terminales = Gramatica.NoyT(self.Antecedentes, self.Consecuentes, True)
        self.NoTerminales = Gramatica.NoyT(self.Antecedentes, self.Consecuentes, False)
        self.Firsts = Gramatica.GetFirsts(self.Antecedentes, self.Consecuentes, self.NoTerminales)

        self.CalcularFolows = Gramatica.Calculate_Follows(Gramatica.ConstruirReglas(self.gramatica, True),"A",Gramatica.ConstruirReglas(self.gramatica, False))

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
        print(self.Terminales)
        print("Terminales: ")
        print(self.NoTerminales)
        print("Firsts: ")
        print(self.Firsts)
        print("Folows")
        print(self.CalcularFolows)


        pass

# Pruebas:
"""
A:b A   
A:a
A:A B c
A: lambda
B: b

"""
gramatica = "A:b\nA:a\nA:A B c\nA:lambda\nB:b\nB:lambda\nC:z"
prueba = Gramatica(gramatica)
prueba.ImprimirPrueba()

