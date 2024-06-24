import copy
from typing import List, Tuple

class Array:
    def __init__(self, value: List):
        # Initialisation de l'objet avec vérification des types et dimensions
        self.value: List = value

        def shaper(dim: List[int], list_element: List, feuilles: List[int]):
            # Ajoute la dimension courante
            dim.append(len(list_element))

            # Vérifie les types dans la liste courante
            types = [str(type(i)) for i in list_element]
            if "<class 'list'>" in types and ("<class 'int'>" in types or "<class 'float'>" in types or "<class 'str'>" in types or "<class 'bool'>" in types):
                raise ValueError("Différents types détectés. La matrice doit contenir le même type.")

            # Vérifie les sous-listes récursivement
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

        # Initialisation des dimensions et des feuilles
        shape: List[int] = []
        feuilles_list: List[int] = []
        shaper(shape, self.value, feuilles_list)
        if feuilles_list == []:
            shape.append(0)
        else:
            shape.append(feuilles_list[0])

        self.shape: Tuple[int, ...] = tuple(shape)

    def __getitem__(self, index: int):
        # Récupère l'élément à l'index donné
        return self.value[index]

    def __contains__(self, item) -> bool:
        # Vérifie si un élément est dans la liste
        return item in self.value

    def __len__(self) -> int:
        # Retourne la longueur de la liste
        return len(self.value)

    def __add__(self, matrice: 'Array') -> 'Array':
        # Additionne deux matrices élément par élément
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
        # Produit scalaire de deux vecteurs 1D
        if self.shape != vector.shape or self.shape[1] != 0 or self.shape[1] != 0:
            raise TypeError("Les vecteurs doivent être de 1D et de même longueur")
        else:
            result = sum(x * y for x, y in zip(self.value, vector.value))
        return result

    def __sub__(self, matrice: 'Array') -> 'Array':
        # Soustrait deux matrices élément par élément
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
        # Multiplie deux matrices (produit matriciel)
        if self.shape[1] != matrice.shape[0]:
            raise ValueError("Le nombre de colonnes de la première matrice doit être égal au nombre de lignes de la deuxième matrice.")
        else:
            result: List[List] = [[0] * matrice.shape[1] for _ in range(self.shape[0])]

            for i in range(self.shape[0]):
                for j in range(matrice.shape[1]):
                    sum = 0
                    for k in range(self.shape[1]):
                        sum += self.value[i][k] * matrice.value[k][j]
                    result[i][j] = sum
        return Array(result)

    def __truediv__(self, matrice: 'Array') -> 'Array':
        # Divise deux matrices élément par élément
        if self.shape != matrice.shape:
            raise ValueError("Les matrices doivent avoir la même forme pour être divisées.")
        else:
            result: List = copy.deepcopy(self.value)

            def div(result: List, self_value: List, matrix_value: List):
                for i in range(len(matrix_value)):
                    if isinstance(self_value[i], list):
                        div(result[i], self_value[i], matrix_value[i])
                    else:
                        result[i] = self_value[i] / matrix_value[i]

            div(result, self.value, matrice.value)
        return Array(result)

    def __str__(self) -> str:
        # Représente l'objet sous forme de chaîne de caractères
        return str(self.value)


# Mini-tests pour vérifier le fonctionnement
# Initialisation des arrays
n = Array([1, 2, 3])
n2 = Array([1, 2, 3])
m1 = Array([[1, 2], [3, 4]])
m2 = Array([[2, 0], [1, 2]])

# Addition
print("Addition:")
print(n + n2)  # Output: [2, 4, 6]
print(m1 + m2)  # Output: [[3, 2], [4, 6]]

# Soustraction
print("Soustraction:")
print(n - n2)  # Output: [0, 0, 0]
print(m1 - m2)  # Output: [[-1, 2], [2, 2]]

# Multiplication
print("Multiplication:")
print(m1 * m2)  # Output: [[4, 4], [10, 8]]

# Division
print("Division:")
print(n / n2)  # Output: [1.0, 1.0, 1.0]

# Produit scalaire (dot product)
print("Produit scalaire:")
print(n @ n2)  # Output: 14

# Vérifier la représentation de l'objet
print("Représentation:")
print(n)  # Output: [1, 2, 3]
print(m1)  # Output: [[1, 2], [3, 4]]