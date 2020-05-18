
class Gramatica():


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
    def NoyT(antec,consec,band):
        """  Noyt: Devuelve Lista de antecedentes y Consecuentes.

        True: Devuelve la lista de terminales
        False: Devuelve la lista de no terminales

        """

        ListaNT=[]
        ListaT=[]
        mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        minusculas = 'abcdefghijklmnopqrstuvwxyz'
        reservadas = "lambda"
        ListaPalabrasAux1 = []
        ListaPalabrasAux2 = []
        for i in range(0, len(antec)):
            ListaPalabrasAux1.append(antec[i].split(" "))

        for i in range(0, len(consec)):
            ListaPalabrasAux2.append(consec[i].split(" "))

        #Antecedentes
        for j in range(0,len(ListaPalabrasAux1)):
            palabra2= ListaPalabrasAux1[j]
            for j2 in range(0,len(palabra2)):
                aux1=palabra2[j2]
                if aux1[0] in mayusculas:
                    ListaNT.append(aux1)

            palabra2 = ""
            primletra=""

        #Consecuentes

        cadena=[]

        for j in range(0,len(ListaPalabrasAux2)):
            palabra2= ListaPalabrasAux2[j]
            for j2 in range(0,len(palabra2)):
                aux1=palabra2[j2]

                if aux1[0] in mayusculas:
                    ListaNT.append(aux1)
                else:
                    if ((aux1[0] in minusculas) or (aux1 == "lambda")):
                        ListaT.append(aux1)

            palabra2 = ""
            primletra=""

        terminales= set(ListaT)
        noterminales=set(ListaNT)


        #Bandera true retorno No terminales
        #Bandera False retorno terminales


        """print(ListaPalabrasAux1)"""

        """print(ListaPalabrasAux2)"""
        if (band==True):
            return terminales
        else:
            return noterminales


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
        self.NoTerminales = Gramatica.NoyT(self.Antecedentes, self.Consecuentes, True)
        self.Terminales = Gramatica.NoyT(self.Antecedentes, self.Consecuentes, False)


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
        print(self.Terminales
              )

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

