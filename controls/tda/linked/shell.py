class ShellSort:
    def shell_sort(self, array, ascending=True):
        n = len(array)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = array[i]
                j = i
                if ascending:
                    while j >= gap and array[j - gap] > temp:
                        array[j] = array[j - gap]
                        j -= gap
                else:
                    while j >= gap and array[j - gap] < temp:
                        array[j] = array[j - gap]
                        j -= gap
                array[j] = temp
            gap //= 2
        return array

    def sort_models_ascendent(self, array, attribute):
        return self.shell_sort(array, attribute, ascending=True)

    def sort_models_descendent(self, array, attribute):
        return self.shell_sort(array, attribute, ascending=False)
    
    def sort_primitive_ascendent(self, array):
        return self.shell_sort(array, ascending=True)

    def sort_primitive_descendent(self, array):
        return self.shell_sort(array, ascending=False)