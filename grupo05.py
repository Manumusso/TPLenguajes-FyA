mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
minusculas = 'abcdefghijklmnopqrstuvwxyz'
LAMBDA = 0
reservadas = ["lambda"]

class Gramatica():

    def GetFirsts(antec, consec, noTerminals):
        Firsts = [None] *len(antec) 
        LookingFor = []
        n = 0
        for var in antec:
            #First para n elemento 
            consecSplitted = consec[n].split(' ')
            if(consecSplitted[0] in noTerminals):
                Firsts[n] = [consecSplitted[0]]
            else:
                if(consecSplitted[0] == reservadas[LAMBDA]):
                    Firsts[n] = [consecSplitted[0]]
                else:
                    Firsts[n] = []
                    LookingFor.append([n, var ,consecSplitted[0], 0])
            n+=1
        print('FIRST TERMINALS')
        print(Firsts)
        print('----------------')

        n = -1
        for noTerminal in LookingFor:
            n=n+1
            if(noTerminal[1] in list(map(lambda x: x[1], LookingFor[n+1:]))):
                LookingFor.append(noTerminal)
                continue
        
                
            for x in range(0, len(antec)):
                if(antec[x] == noTerminal[2]):
                    Firsts[noTerminal[0]] = list(set(Firsts[x])|set(Firsts[noTerminal[0]]))
    
                    if(reservadas[LAMBDA] in Firsts[x]):
                        if(consec[n].split(' ')[noTerminal[3]] in noTerminals or consec[n].split(' ')[noTerminal[3]] == reservadas[LAMBDA]):
                            if(consec[n].split(' ')[noTerminal[3]] not in Firsts[noTerminal[0]]):
                                Firsts[noTerminal[0]].append(consec[n].split(' ')[noTerminal[3]])
                        else:
                            LookingFor.append([n, None,consec[n].split(' ')[noTerminal[3]], noTerminal[3]+1])


        return Firsts


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
                i=i+2
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
              

        pass

# Pruebas:
"""
A:b A   
A:a
A:A B c
A: lambda
B: b

"""
gramatica = "A:b A\nA:a\nA:A B c\nA:lambda\nB:b"
prueba = Gramatica(gramatica)
prueba.ImprimirPrueba()

