import sys
sys.path.append('../')  # Ajusta la ruta según la ubicación de tu archivo sorting.py

# import random
# import time
# from controls.tda.linked.merge import MergeSort
# from controls.tda.linked.quick import QuickSort
# from controls.tda.linked.shell import ShellSort
# from controls.tda.linked.binarySearch import BinarySearch
# from controls.tda.linked.linearSearch import LinearSearch 
from controls.personaDaoControl import PersonaDaoControl
from controls.tda.linked.linkedList import Linked_List
pcd = PersonaDaoControl()

# def main():
#     sizes = [10000, 20000, 25000]
#     sorters = {
#         "MergeSort": MergeSort(),
#         "QuickSort": QuickSort(),
#         "ShellSort": ShellSort()
#     }
#     searchers = {
#         "BinarySearch": BinarySearch(),
#         "LinearSearch": LinearSearch()
#     }
    
#     for size in sizes:
#         print(f"\n\033[93mOrdenar array por tamaño de: {size}:\033[0m")
#         print("**Metodos de Ordenamiento:")
#         data = [random.randint(1, 100000) for _ in range(size)]
        
#         for sorter_name, sorter in sorters.items():
#             data_copy = data.copy()
#             start_time = time.time()
#             sorter.sort_primitive_ascendent(data_copy)
#             end_time = time.time()
#             print(f"{sorter_name}: {end_time - start_time:.5f} seconds")
        
#         # Búsqueda de un valor aleatorio en el arreglo
#         print(f"\n**Metodos de Busqueda:")
#         query = random.choice(data)
#         query_attribute = 0  # Usado para búsqueda en datos primitivos

#         for searcher_name, searcher in searchers.items():
#             data_copy = data.copy()
#             start_time = time.time()
#             if searcher_name == "BinarySearch":
#                 searcher.search(data_copy, query_attribute, query, starts_with=False)
#             else:
#                 searcher.search(data_copy, query_attribute, query, starts_with=False)
#             end_time = time.time()
#             print(f"{searcher_name}: {end_time - start_time:.5f} seconds")

# if __name__ == "__main__":
#     main()
lista = Linked_List()
try:
    lista = pcd._list()
    lista.print 
    print(lista.toArray._array)
except Exception as e : 
    print(e) 
