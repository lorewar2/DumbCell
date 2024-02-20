import random
import numpy as np

def get_softmax(raw_probs):
    softmax_probs = np.array(raw_probs)
    for i in range(len(softmax_probs)):
        softmax_probs[i] = np.exp(softmax_probs[i])
    sum = np.sum(softmax_probs)
    for i in range(len(softmax_probs)):
        softmax_probs[i] = softmax_probs[i] / sum
    return softmax_probs

def generate_test_set(num_of_variant_loc, depth, cell_num):

    return

def expectation_step():
    return

def maximization_step():
    return

def visualize():
    # give random y to visualize better in 2d i guess?

    return

def main():
    # seed this
    random.seed(3)
    np.random.seed(2)
    # variables 
    variant_num = 20
    cluster_num = 2
    cell_num = 2
    cluster_probs = np.empty((cell_num, variant_num, cluster_num))
    # cluster prob array initialize randomly
    for cell in range(cell_num):
        for variant in range(variant_num):
            random_probs = [random.random() for variant in range(cluster_num)]
            softmax_probs = get_softmax(random_probs)
            cluster_probs[cell][variant] = softmax_probs
    print(cluster_probs)
    # make a test set

    return





if __name__ == "__main__":
    main()