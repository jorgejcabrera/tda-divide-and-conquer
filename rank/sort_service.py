class SortService:

    def __init__(self):
        self.movements_to_right = dict()

    def all_improvements_by_previous_position(self, lista):
        if len(lista) > 1:
            half = len(lista) // 2
            left = lista[:half]
            right = lista[half:]

            self.all_improvements_by_previous_position(left)
            self.all_improvements_by_previous_position(right)

            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    lista[k] = left[i]
                    i += 1
                else:
                    if left[i] in self.movements_to_right:
                        self.movements_to_right[left[i]] += 1
                    else:
                        self.movements_to_right[left[i]] = 1
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

        return self.movements_to_right
