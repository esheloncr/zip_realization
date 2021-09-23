def custom_zip(*args):
    sentinel = object()
    iterators = [iter(it) for it in args]
    while iterators:
        result = []
        for i in iterators:
            elem = next(i, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)
