import numpy as np
import random

NOISE = 0.1
N_LETTERS = 4

alphabet = [[1,1,1,1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,1,1,1,1],
            [1,1,1,1,-1, 1,-1,-1,-1,1, 1,1,1,1,-1, 1,-1,-1,-1,1, 1,1,1,1,-1],
            [-1,1,1,1,-1, 1,-1,-1,-1,1, 1,-1,-1,-1,-1, 1,-1,-1,-1,1, -1,1,1,1,-1],
            [1,1,1,1,-1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,1,1,1,-1],
            [1,1,1,1,1, 1,-1,-1,-1,-1, 1,1,1,-1,-1, 1,-1,-1,-1,-1, 1,1,1,1,1],
            [1,1,1,1,1, 1,-1,-1,-1,-1, 1,1,1,1,-1, 1,-1,-1,-1,-1, 1,-1,-1,-1,-1],
            [1,1,1,1,1, 1,-1,-1,-1,-1, 1,-1,1,1,1, 1,-1,-1,-1,1, 1,1,1,1,1],
            [1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,1,1,1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1],
            [1,1,1,1,1, -1,-1,1,-1,-1, -1,-1,1,-1,-1, -1,-1,1,-1,-1, 1,1,1,1,1],
            [1,1,1,1,1, -1,-1,-1,1,-1, -1,-1,-1,1,-1, 1,-1,-1,1,-1, 1,1,1,-1,-1],
            [1,-1,-1,-1,1, 1,-1,-1,1,-1, 1,1,1,-1,-1, 1,-1,-1,1,-1, 1,-1,-1,-1,1],
            [1,-1,-1,-1,-1, 1,-1,-1,-1,-1, 1,-1,-1,-1,-1, 1,-1,-1,-1,-1, 1,1,1,1,1],
            [1,-1,-1,-1,1, 1,1,-1,1,1, 1,-1,1,-1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1],
            [1,-1,-1,-1,1, 1,1,-1,-1,1, 1,-1,1,-1,1, 1,-1,-1,1,1, 1,-1,-1,-1,1],
            [1,1,1,1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,1,1,1,1],
            [1,1,1,1,1, 1,-1,-1,-1,1, 1,1,1,1,1, 1,-1,-1,-1,-1, 1,-1,-1,-1,-1],
            [1,1,1,1,-1, 1,-1,-1,1,-1, 1,-1,-1,1,-1, 1,1,1,1,-1, -1,-1,-1,-1,1],
            [1,1,1,1,1, 1,-1,-1,-1,1, 1,1,1,1,1, 1,-1,-1,1,-1, 1,-1,-1,-1,1],
            [1,1,1,1,1, 1,-1,-1,-1,-1, 1,1,1,1,1, -1,-1,-1,-1,1, 1,1,1,1,1],
            [1,1,1,1,1, -1,-1,1,-1,-1, -1,-1,1,-1,-1, -1,-1,1,-1,-1, -1,-1,1,-1,-1],
            [1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,1,1,1,1],
            [1,-1,-1,-1,1, 1,-1,-1,-1,1, -1,1,-1,1,-1, -1,1,-1,1,-1, -1,-1,1,-1,-1],
            [1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,-1,1,-1,1, 1,1,-1,1,1],
            [1,-1,-1,-1,1, -1,1,-1,1,-1, -1,-1,1,-1,-1, -1,1,-1,1,-1, 1,-1,-1,-1,1],
            [1,-1,-1,-1,1, -1,1,-1,1,-1, -1,-1,1,-1,-1, -1,-1,1,-1,-1, -1,-1,1,-1,-1],
            [1,1,1,1,1, -1,-1,-1,1,-1, -1,-1,1,-1,-1, -1,1,-1,-1,-1, 1,1,1,1,1]]

alphabet_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                  'p','q','r','s','t','u','v','w','x','y','z']

def chooseLetters():
    to_return = np.empty((N_LETTERS,25), dtype=int)
    for i in range(0,N_LETTERS):
        p = random.randint(0,len(alphabet)-1)
        while alphabet[p] in to_return.tolist():
            p = p+1
            if p == len(alphabet)-1:
                p = 0
        to_return[i] = alphabet[p]
        print(f'Letra pickeada: {alphabet_chars[p]}, ({to_return[i]})')
    return to_return


def getWeights(letters):
    matrix = np.zeros((len(letters[0]), len(letters[0])))
    for i in range(0, len(letters[0])):
        for j in range(i, len(letters[0])):
            if i == j:
                matrix[i][j] = 0
                matrix[j][i] = 0
            else:
                sum = 0.0
                for elem in range(0, len(letters)-1):
                    sum += (letters[elem][i] * letters[elem][j])
                matrix[i][j] = sum / len(letters[0])
                matrix[j][i] = matrix[i][j]
    return matrix

def randWithNoNoise(chose):
    for i in range(0, len(chose)):
        p = np.random.uniform()
        if p < NOISE:
            chose[i] = -1 if chose[i] == 1 else 1
    return chose

def randLetterPattern(letters):
    selected = letters[random.randint(0, len(letters)-1)]
    print("\n" + f'Letra seleccionada: {selected}')
    return selected

def printLetter(letter):
    test = np.array_split(letter, 5)
    for line in range(0, len(test)):
        str = ''
        for i in range(0, len(test[0])):
            if test[line][i] == 1:
                str = str + '*'
            else:
                str = str + ' '
        print(str)

def noise(array, n):
    if n > 0:
        aux = array
        for i in range(len( array)):
            rand = random.uniform(0, 1)
            if rand <= n:
                if aux[i] == -1:
                    aux[i] = 1
                elif aux[i] == 1:
                    aux[i] = -1
                else:
                    exit("error adding noise")
        return aux
    return array

def hopfield(n = 0):
    letters = chooseLetters()
    weights = getWeights(letters)
    aux = randLetterPattern(letters)
    print('Letra original sin ruido: ')
    printLetter(aux)
    original = noise(aux, n)
    value = randWithNoNoise(aux)
    prev = value
    actual = np.zeros(len(prev))

    while np.array_equal(prev,actual) == False:
        for i in range(0, len(value)):
            sum = 0
            for j in range(0, len(value)):
                if i != j:
                    sum += weights[i][j]*prev[j]
            h_i = int(np.sign(sum)) if sum != 0 else 0
            print("Estado actual:", actual)
            actual[i] = h_i
        if np.array_equal(prev,actual):
            break
        else:
            prev = actual
            actual = np.zeros(len(prev))
    actual = actual.astype(int)

    print('Letra según Hopfield: ')
    printLetter(actual)
    print('Letra original: ')
    printLetter(original)

    if np.array_equal(original,actual):
        print('Patrón de letra correcto')
    else:
        print('Patrón de letra incorrecto')

hopfield(0.1)
