import copy
from typing import List, Tuple

class Array:
    def __init__(self, value: List) :
        self.value: List = value

        def shaper(dim: List[int], list_element: List, feuilles: List[int]):
            dim.append(len(list_element))

            types = [str(type(i)) for i in list_element]
            if "<class 'list'>" in types and ("<class 'int'>" in types or "<class 'float'>" in types or "<class 'str'>" in types or "<class 'bool'>" in types):
                raise ValueError("Différents types détectés. La matrice doit contenir le même type.")

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
                                raise ValueError("Sous-listes de tailles différentes détectées. Les sous-listes doivent avoir la même taille.")
                            else:
                                feuilles.append(len(element))

        shape = []
        feuilles_list = []
        shaper(shape, self.value, feuilles_list)
        if feuilles_list == []:
            shape.append(0)
        else:
            shape.append(feuilles_list[0])

        self.shape: Tuple[int, ...] = tuple(shape)

    def __getitem__(self, index: int):
        return self.value[index]

    # def __getitem__(self, index):
    # if isinstance(index, tuple):
    #     result = self.value
    #     for i in index:
    #         result = result[i]
    #     return result
    # return self.value[index]

    def __contains__(self, item) -> bool:
        return item in self.value

    def __len__(self) -> int:
        return len(self.value)

    def __add__(self, matrice: 'Array') -> 'Array':
        if self.shape != matrice.shape:
            raise ValueError("Les matrices doivent avoir la même forme pour être additionnées.")
        else:
            result: List = copy.deepcopy(self.value)

            def add(result: List, self_value: List, matrix_value: List):
                for i in range(len(matrix_value)):
                    if isinstance(self_value[i], list):
                        add(result[i], self_value[i], matrix_value[i])
                    else:
                        result[i] = self_value[i] + matrix_value[i]

            add(result, self.value, matrice.value)
        return Array(result)

    def __matmul__(self, vector: 'Array') -> int:
        if self.shape != vector.shape or self.shape[1] != 0 or self.shape[1] != 0:
            raise TypeError("Les vecteurs doivent être de 1D et de même longueur")
        else:
            result = sum(x * y for x, y in zip(self.value, vector.value))
        return result

    def __sub__(self, matrice: 'Array') -> 'Array':
        if self.shape != matrice.shape:
            raise ValueError("Les matrices doivent avoir la même forme pour être soustraites.")
        else:
            result: List = copy.deepcopy(self.value)

            def soustrat(result: List, self_value: List, matrix_value: List):
                for i in range(len(matrix_value)):
                    if isinstance(self_value[i], list):
                        soustrat(result[i], self_value[i], matrix_value[i])
                    else:
                        result[i] = self_value[i] - matrix_value[i]

            soustrat(result, self.value, matrice.value)
        return Array(result)

    def __mul__(self, matrice: 'Array') -> 'Array':
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

    def __truediv__(self, matrice: 'Array') -> 'Array':
        if self.shape != matrice.shape:
            raise ValueError("Les matrices doivent avoir la même forme pour être divisées.")
        else:
            result = copy.deepcopy(self.value)

            def div(result: List, self_value: List, matrix_value: List):
                for i in range(len(matrix_value)):
                    if isinstance(self_value[i], list):
                        div(result[i], self_value[i], matrix_value[i])
                    else:
                        result[i] = self_value[i] / matrix_value[i]

            div(result, self.value, matrice.value)
        return Array(result)

    def __str__(self) -> str:
        return str(self.value)


# TESTS
n = Array([1, 2, 3])
n2 = Array([1, 2, 3])
m1 = Array([[1, 2], [3, 4]])
m2 = Array([[2, 0], [1, 2]])

# Addition
print("Addition:")
print(n + n2)  
print(m1 + m2)  

# Soustraction
print("Soustraction:")
print(n - n2) 
print(m1 - m2)  

# Multiplication
print("Multiplication:")
print(m1 * m2)

# Division
print("Division:")
print(n / n2)

# Produit scalaire
print("Produit scalaire:")
print(n @ n2)
