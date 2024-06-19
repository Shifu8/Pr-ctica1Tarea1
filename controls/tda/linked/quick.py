class QuickSort:
    def partition(self, array, low, high, ascending=True):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if ascending:
                if array[j] <= pivot:
                    i += 1
                    array[i], array[j] = array[j], array[i]
            else:
                if array[j] >= pivot:
                    i += 1
                    array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    def quick_sort(self, array, low, high, ascending=True):
        if low < high:
            pi = self.partition(array, low, high, ascending)
            self.quick_sort(array, low, pi - 1, ascending)
            self.quick_sort(array, pi + 1, high, ascending)
        return array

    def sort_models_ascendent(self, array, attribute):
        return self.quick_sort(array, 0, len(array) - 1, attribute, ascending=True)

    def sort_models_descendent(self, array, attribute):
       return self.quick_sort(array, 0, len(array) - 1, attribute, ascending=False)
   
    def sort_primitive_ascendent(self, array):
        return self.quick_sort(array, 0, len(array) - 1, ascending=True)

    def sort_primitive_descendent(self, array):
        return self.quick_sort(array, 0, len(array) - 1, ascending=False)
    
    

