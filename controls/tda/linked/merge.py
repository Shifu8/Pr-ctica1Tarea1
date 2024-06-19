class MergeSort:
    
    def merge(self, left, right, ascending=True):
        result = []
        while left and right:
            if ascending:
                if left[0] <= right[0]:
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
            else:
                if left[0] >= right[0]:
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
        result.extend(left or right)
        return result

    def merge_sort(self, array, ascending=True):
        if len(array) <= 1:
            return array
        middle = len(array) // 2
        left = self.merge_sort(array[:middle], ascending)
        right = self.merge_sort(array[middle:], ascending)
        return self.merge(left, right, ascending)

    def sort_primitive_ascendent(self, array):
        return self.merge_sort(array, ascending=True)

    def sort_primitive_descendent(self, array):
        return self.merge_sort(array, ascending=False)
    
    def sort_models_ascendent(self, array, attribute):
        def merge(left, right):
            result = []
            while left and right:
                if getattr(left[0], attribute) <= getattr(right[0], attribute):
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
            result.extend(left or right)
            return result

        def merge_sort(array):
            if len(array) <= 1:
                return array
            middle = len(array) // 2
            left = merge_sort(array[:middle])
            right = merge_sort(array[middle:])
            return merge(left, right)
        
        return merge_sort(array)
    
    def sort_models_descendent(self, array, attribute):
        def merge(left, right):
            result = []
            while left and right:
                if getattr(left[0], attribute) >= getattr(right[0], attribute):
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
            result.extend(left or right)
            return result

        def merge_sort(array):
            if len(array) <= 1:
                return array
            middle = len(array) // 2
            left = merge_sort(array[:middle])
            right = merge_sort(array[middle:])
            return merge(left, right)
        
        return merge_sort(array)