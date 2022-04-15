class SortService:

    def __init__(self):
        self.movements_to_right = dict()

    def all_improvements_by_previous_position(self, lista):
        if len(lista) > 1:
            medio = len(lista) // 2
            izquierda = lista[:medio]
            derecha = lista[medio:]
            print(izquierda, '*' * 5, derecha)

            # Llamada recursiva en cada mitad.
            self.all_improvements_by_previous_position(izquierda)
            self.all_improvements_by_previous_position(derecha)

            # Iteradores para recorrer las dos sublistas
            i = 0
            j = 0
            # Iterador de la lista principal
            k = 0

            while i < len(izquierda) and j < len(derecha):
                if izquierda[i] < derecha[j]:
                    lista[k] = izquierda[i]
                    i += 1
                else:
                    if izquierda[i] in self.movements_to_right:
                        self.movements_to_right[izquierda[i]] += 1
                    else:
                        self.movements_to_right[izquierda[i]] = 1
                    lista[k] = derecha[j]
                    j += 1
                k += 1

            while i < len(izquierda):
                lista[k] = izquierda[i]
                i += 1
                k += 1

            while j < len(derecha):
                lista[k] = derecha[j]
                j += 1
                k += 1

            print(f'izquierda {izquierda}, derecha {derecha}')
            print(lista)
            print('-' * 50)

        return self.movements_to_right
