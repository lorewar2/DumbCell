import random
import numpy as np

def get_softmax(raw_probs):
    softmax_probs = np.exp(raw_probs)
    softmax_probs /= np.sum(softmax_probs)
    return softmax_probs

def generate_test_set(num_of_variant_loc, depth, cell_num):
    # Generate a synthetic test set
    test_set = np.random.randint(0, 2, size=(cell_num, num_of_variant_loc, depth))
    return test_set

def expectation_step(test_set, cluster_probs):
    # Perform the E-step of the EM algorithm
    # Compute the responsibilities (expected cluster assignments) for each data point
    responsibilities = np.zeros_like(cluster_probs)
    
    return responsibilities

def maximization_step(test_set, responsibilities):
    # Perform the M-step of the EM algorithm
    # Update the parameters of the mixture model (cluster_probs)
    updated_cluster_probs = np.zeros_like(responsibilities)
    
    return updated_cluster_probs

def visualize():
    # Visualize the results
    pass

def main():
    # seed this
    random.seed(3)
    np.random.seed(2)
    
    # variables
    variant_num = 20
    cluster_num = 2
    cell_num = 2
    
    # Initialize cluster probabilities array randomly
    cluster_probs = np.random.rand(cell_num, variant_num, cluster_num)
    cluster_probs = np.apply_along_axis(get_softmax, axis=-1, arr=cluster_probs)
    print("Initial cluster probabilities:")
    print(cluster_probs)
    
    # Generate a test set
    test_set = generate_test_set(num_of_variant_loc=variant_num, depth=10, cell_num=cell_num)
    print("\nGenerated test set shape:", test_set.shape)
    
    # EM iterations
    num_iterations = 5
    for i in range(num_iterations):
        # E-step
        responsibilities = expectation_step(test_set, cluster_probs)
        
        # M-step
        cluster_probs = maximization_step(test_set, responsibilities)
        
        print("\nIteration:", i+1)
        print("Updated cluster probabilities:")
        print(cluster_probs)

    # Visualize the results
    visualize()

if __name__ == "__main__":
    main()