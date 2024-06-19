class BinarySearch:
    @staticmethod
    def search(data, attribute, query, starts_with=False):
        if isinstance(attribute, int):
            sorted_data = sorted(data)
            attribute_accessor = lambda x: x
        else:
            sorted_data = sorted(data, key=lambda x: getattr(x, attribute))
            attribute_accessor = lambda x: getattr(x, attribute)
        
        left, right = 0, len(sorted_data) - 1
        results = []

        normalized_query = query.lower() if isinstance(query, str) else query

        while left <= right:
            mid = (left + right) // 2
            mid_value = attribute_accessor(sorted_data[mid])

            if isinstance(mid_value, str):
                mid_value = mid_value.lower()

            if starts_with:
                if str(mid_value).startswith(str(normalized_query)):
                    # Agregar todos los elementos iguales hacia la izquierda
                    i = mid
                    while i >= 0 and str(attribute_accessor(sorted_data[i])).lower().startswith(str(normalized_query)):
                        results.append(sorted_data[i])
                        i -= 1
                    # Agregar todos los elementos iguales hacia la derecha
                    i = mid + 1
                    while i < len(sorted_data) and str(attribute_accessor(sorted_data[i])).lower().startswith(str(normalized_query)):
                        results.append(sorted_data[i])
                        i += 1
                    return results
                elif mid_value < normalized_query:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if str(normalized_query) in str(mid_value):
                    # Agregar todos los elementos iguales hacia la izquierda
                    i = mid
                    while i >= 0 and str(normalized_query) in str(attribute_accessor(sorted_data[i])).lower():
                        results.append(sorted_data[i])
                        i -= 1
                    # Agregar todos los elementos iguales hacia la derecha
                    i = mid + 1
                    while i < len(sorted_data) and str(normalized_query) in str(attribute_accessor(sorted_data[i])).lower():
                        results.append(sorted_data[i])
                        i += 1
                    return results
                elif mid_value < normalized_query:
                    left = mid + 1
                else:
                    right = mid - 1

        return results