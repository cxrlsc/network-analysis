# remove all negative correlations and set them to 0
# MUTATING FUNCTION (no returns)
def remove_negatives(arr):
    counteri = 0 
    for i in arr:
        counterj = 0
        for j in i:
            if j < 0:
                arr[counteri][counterj] = 0
            counterj +=1
        counteri += 1

##################################### ~~~~ NETWORK MANIPULATION ~~~~ #####################################

# function that takes in a participant's correlation matrix and 
# returns 5 matrices at different thresholds
def threshold(arr, thresholds):
    #thresholding the array
    return [bct.threshold_proportional(arr, p, copy=True) for p in thresholds]

# binarizes the input matrix
def binarize(arr):
    return bct.weight_conversion(arr, wcm='binarize')

# generate NUM_RANDOMS randomize undirected, weighted networks (working)
def randomize(array, iterations, num_randoms):
    randomizedArrays = []
    for i in range(num_randoms):
        random_arr, eff = bct.randmio_und(array, iterations)
        randomizedArrays.append(random_arr)
    return randomizedArrays

# generate NUM_RANDOMS randomized directed, weighted networks (resting)
def randomize_d(arr, iterations, num_randoms):
    randomizedArrays = []
    for i in range(num_randoms):
        rarr, eff = bct.randmio_dir(arr, iterations)
        randomizedArrays.append(rarr)
    return randomizedArrays




##################################### ~~~~ NETWORK METRICS ~~~~ #####################################

# collect clustering coefficient accross different thresholds (10%-50%) for both 
# RESTING and WORKING state data
def get_clustering_coeff_avgs(states):
    clusters = [bct.clustering_coef_wu(arr) for arr in states]
    return [np.mean(i) for i in clusters]


def get_clustering_coeff(arr):
    return bct.clustering_coef_wu(arr)

def get_clustering_coeff_bin(arr):
    return bct.clustering_coef_bu(arr)

def charpath(array):
    
    # converting to lengths
    array = bct.weight_conversion(array, 'lengths')
    
    # turning into distance array 
    distance_array, other_arr = bct.distance_wei(array)
    
    return bct.charpath(distance_array)

def charpath_bin(array):
    # no need to be done, can be removed
    array = bct.weight_conversion(array, 'lengths')
    
    # turning to binarized distance array
    distance_array, other_array = bct.distance_bin(array)
    return bct.charpath(distance_array, 0, 1)

##################################### ~~~~ HELPER METHODS ~~~~ #####################################
# normalizing method to normalize network metrics
def normalize(arr1, mean):
    output = []
    for i in arr1:
        output.append(i/mean)
    return output

def normalized(val, mean):
    return val/mean

