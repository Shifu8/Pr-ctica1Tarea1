class LinearSearch:
    @staticmethod
    def search(data, attribute, query, starts_with=False):
        normalized_query = query.lower() if isinstance(query, str) else query
        if isinstance(attribute, int):
            if starts_with:
                return [item for item in data if str(item).lower().startswith(str(normalized_query))]
            else:
                return [item for item in data if str(normalized_query) in str(item).lower()]
        else:
            if starts_with:
                return [item for item in data if str(getattr(item, attribute)).lower().startswith(str(normalized_query))]
            else:
                return [item for item in data if str(normalized_query) in str(getattr(item, attribute)).lower()]