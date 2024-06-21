import copy
class Array:
    def __init__(self, value:list):
        self.value:list = value

        def shaper(dim, list_element, feuilles):
            dim.append(len(list_element))

            types = [str(type(i)) for i in list_element]
            if "<class 'list'>" in types and ( "<class 'int'>" in types or "<class 'float'>" in types or "<class 'str'>" in types or "<class 'bool'>" in types):
                raise ValueError("Différents types détectées.La matrice doit contenir le même type.")

            for element in list_element:
                if str(type(element)) == "<class 'list'>":
                    types = [str(type(i)) for i in element]
                    if "<class 'list'>" in types:
                        shaper(dim, element, feuilles)
                    else:
                        if feuilles == []:
                            feuilles.append(len(element))
                        else:
                            if feuilles[-1] != len(element):
                                raise ValueError("Sous-listes de tailles différentes détectées.\nLes sous-listes doivent avoir la même taille.")
                            else:
                                feuilles.append(len(element))         
        shape = []
        feuilles_list = []
        shaper(shape, self.value, feuilles_list)
        if feuilles_list == []:
            shape.append(0)
        else:
            shape.append(feuilles_list[0])

        self.shape:tuple = tuple(shape)

    def __getitem__(self, index):
        return self.value[index]

    def __contains__(self, item):
        return item in self.data

    def __len__(self):
        return len(self.value)

    def __add__(self, matrice):
        if self.shape != matrice.shape:
            raise ValueError("Les matrices doivent avoir la même forme pour être additionnées.")
        else:
            result = copy.deepcopy(self.value)
            
            def add(result, self_value, matrix_value):
                for i in range(len(matrix_value)):
                    if isinstance(self_value[i], list):
                        add(result[i], self_value[i], matrix_value[i])
                    else:
                        result[i] = self_value[i] + matrix_value[i]
            
            add(result, self.value, matrice.value)
        return Array(result)

    def __sub__(self, matrice):
        if self.shape != matrice.shape:
            raise ValueError("Les matrices doivent avoir la même forme pour être soustraites.")
        else:
            result = copy.deepcopy(self.value)
            
            def soustrat(result, self_value, matrix_value):
                for i in range(len(matrix_value)):
                    if isinstance(self_value[i], list):
                        soustrat(result[i], self_value[i], matrix_value[i])
                    else:
                        result[i] = self_value[i] - matrix_value[i]
            
            soustrat(result, self.value, matrice.value)
        
        return Array(result)
    
    def __mul__(self, matrice):
        if self.shape[1] != matrice.shape[0]:
            raise ValueError("Le nombre de colonnes de la première matrice doit être égal au nombre de lignes de la deuxième matrice.")
        else:
            result = [[0] * matrice.shape[1] for _ in range(self.shape[0])]
            
            for i in range(self.shape[0]):
                for j in range(matrice.shape[1]):
                    sum = 0
                    for k in range(self.shape[1]):
                        sum += self.value[i][k] * matrice.value[k][j]
                    result[i][j] = sum
        return Array(result)
    
    def __truediv__(self, matrice):
        if isinstance(matrice, (int, float)):
            result = [[self.value[i][j] / matrice for j in range(self.shape[1])] for i in range(self.shape[0])]
        elif isinstance(matrice, Matrix):
            if self.shape != matrice.shape:
                raise ValueError("Les matrices doivent avoir la même forme pour être divisées.")
            result = [[self.value[i][j] / matrice.value[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
        else:
            raise TypeError("La division n'est définie que par un scalaire (int ou float) ou une autre matrice.")
        return Array(result)

    def __str__(self):
        return str(self.value)

n = Array([[1, 2, 3], [1, 2, 3]])
n1 = Array([[1, 2, 3], [1, 2, 4]])

# print(n)
# print(n.shape)
print(n + n1)
# print(len(n))