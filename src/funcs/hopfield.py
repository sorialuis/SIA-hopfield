# import matplotlib.pyplot as plt
import numpy as np

def learn(pw, ph, patterns):
                           
    identity = np.identity(pw * ph)
    generalWeightMatrix = np.zeros((pw * ph, pw * ph))
  
    # identity = np.identity(max(pw, ph))
    # generalWeightMatrix = np.zeros((max(pw, ph), max(pw, ph)))

    for i in range(len(patterns)):
        generalWeightMatrix += np.dot(patterns[i].reshape(pw * ph, 1), patterns[i].reshape(1,pw * ph)) - identity
    return generalWeightMatrix

def searchPattern(patternFail, mgw):
    input = np.sign(np.dot(patternFail, mgw))
    #iterations = 0

    for _ in range(100000):
        input = np.sign(np.dot(input, mgw))

    # while iterations < 100000:
    #     input = np.sign(np.dot(input, mgw))
    #     iterations+=1

    return input