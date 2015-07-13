from types import GeneratorType


def portions_iterator(sequence, step=500, iterations=None):
    """Iterate over sequence with portions.

    :param sequence: sequence
    :param step: portion size
    :type step: int
    :param iterations: max iterations number. Not required.
    :type: int

    """
    if isinstance(sequence, GeneratorType):
        for instance in sequence:
            yield instance
        raise StopIteration

    i = 0
    while True:
        if iterations and iterations == i:
            raise StopIteration()
        portion = sequence[i:i + step]
        if not portion:
            raise StopIteration()
        for instance in portion:
            i += 1
            yield instance
        if len(portion) < step:
            raise StopIteration()
