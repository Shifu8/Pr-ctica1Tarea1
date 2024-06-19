class Insercion:
    def sort_primitive_ascendent(self, array):
        for i in range (1, len(array)):
            j = i - 1
            t = array[i]
            while j >= 0 and t < array[j]:
                array [j + 1] = array[j]
                j = j - 1
                array[j + 1] = t
        return array
    
    def sort_primitive_descendent(self, array):
        for i in range (1, len(array)):
            j = i - 1
            t = array[i]
            while j >= 0 and t > array[j]:
                array [j + 1] = array[j]
                j = j - 1
                array[j + 1] = t
        return array
    
    def sort_models_ascendent(self, array, attribute):
        for i in range(1, len(array)):
            j = i - 1
            t = array[i]
            while j >= 0 and getattr(t, attribute) < getattr(array[j], attribute):
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = t

        return array
    
    def sort_models_descendent(self, array, attribute):
        for i in range(1, len(array)):
            j = i - 1
            t = array[i]
            while j >= 0 and getattr(t, attribute) > getattr(array[j], attribute):
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = t

        return array
    #if getattr(array[j -  1], attribute) > getattr(array[j], attribute)

# from datetime import datetime

# class Insercion:
#     def sort_primitive_ascendent(self, array):
#         for i in range(1, len(array)):
#             t = array[i]
#             j = i - 1
#             while j >= 0 and t < array[j]:
#                 array[j + 1] = array[j]
#                 j -= 1
#             array[j + 1] = t
#         return array

#     def sort_primitive_descendent(self, array):
#         for i in range(1, len(array)):
#             t = array[i]
#             j = i - 1
#             while j >= 0 and t > array[j]:
#                 array[j + 1] = array[j]
#                 j -= 1
#             array[j + 1] = t
#         return array

#     def sort_models_ascendent(self, array, attribute, data_format=None):
#         for i in range(1, len(array)):
#             j = i - 1
#             t = array[i]
#             while j >= 0 and self.compare(getattr(t, attribute), getattr(array[j], attribute), data_format, asc=True):
#                 array[j + 1] = array[j]
#                 j = j - 1
#             array[j + 1] = t
#         return array
    
#     def sort_models_descendent(self, array, attribute, data_format=None):
#         for i in range(1, len(array)):
#             j = i - 1
#             t = array[i]
#             while j >= 0 and self.compare(getattr(t, attribute), getattr(array[j], attribute), data_format, asc=False):
#                 array[j + 1] = array[j]
#                 j = j - 1
#             array[j + 1] = t
#         return array
    
#     def compare(self, a, b, data_format, asc=True):
#         if data_format:
#             a = datetime.strptime(a, data_format)
#             b = datetime.strptime(b, data_format)
#         if asc:
#             return a < b
#         else:
#             return a > b
        

