class Array:
    def __init__(self, value:list):
        self.value:list = value

        shape_len = []
        count_lines = 0
        for i in self.value:
            count_lines += 1
            if str(type(i)) == "<class 'list'>":
                if shape_len == []:
                    shape_len.append(len(i))
                else:
                    if shape_len[-1] != len(i):
                        raise ValueError("Sous-listes de tailles différentes détectées.\nLes sous-listes doivent avoir la même taille.")
                    else:
                        shape_len.append(len(i))
        if shape_len == []:
            shape = [count_lines, 0]
        else:
            shape = [count_lines, shape_len[0]]

        self.shape:tuple = tuple(shape)

    
    def __str__(self):
        for i in self.value:
            if self.value.index(i) == 0:
                print(f"[{i},")
            elif self.value.index(i) == len(self.value)-1:
                print(f" {i}]")
            else:
                print(f" {i},")
        return ""

n = Array([[1, 23, 5]])
print(n)
print(n.shape)