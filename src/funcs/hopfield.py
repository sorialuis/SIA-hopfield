import numpy as np

def learn(pw, ph, patterns):
    identity = np.identity(pw * ph)
    generalWeightMatrix = np.zeros((pw * ph, pw * ph))

    for i in range(len(patterns)):
        generalWeightMatrix += np.dot(patterns[i].reshape(pw * ph, 1), patterns[i].reshape(1,pw * ph)) - identity

    return generalWeightMatrix

def searchPattern(patternFail, mgw):
    print(patternFail)
    input = np.sign(np.dot(patternFail, mgw))

    for _ in range(100):
        input = np.sign(np.dot(input, mgw))
    return input