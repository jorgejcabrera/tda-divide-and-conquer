class SortService:

    def __init__(self):
        self.movements_to_right_v2 = dict()

    def all_improvements_by_previous_position_v2(self, lista):
        if len(lista) > 1:
            half = len(lista) // 2
            left = lista[:half]
            right = lista[half:]

            self.all_improvements_by_previous_position_v2(left)
            self.all_improvements_by_previous_position_v2(right)

            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i].previous_rank < right[j].previous_rank:
                    lista[k] = left[i]
                    i += 1
                else:
                    if left[i].name in self.movements_to_right_v2:
                        self.movements_to_right_v2[left[i].name] += 1
                    else:
                        self.movements_to_right_v2[left[i].name] = 1
                    lista[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                lista[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                lista[k] = right[j]
                j += 1
                k += 1

        return self.movements_to_right_v2
