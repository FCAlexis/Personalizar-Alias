def vectorizar(directorio):
    vector = []

    m = open(directorio, 'r')

    for x in m:
        vector.append(x)

    m.close()

    return vector
