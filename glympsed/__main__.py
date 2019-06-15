import sys
import scipy
from scipy import stats
from scipy import special
import numpy as np
import pandas as pd

from .create_sim_data.simulate_counts import *
from .sample_models.run_random_data import *
from .sample_models.pca_kmeans import *
from .sample_models.run_unsupervised import *

def main(args = None):
    """Main - serves project"""
    if args is None:
        args = sys.argv[1:]

    ## Run with simulated data (reflecting biological data)
    #simulated_counts()

    ## Run with random generated data
    #do_random_data()

    ## Run with Pseudomon. data
    main_execute()

if __name__ == "__main__":
    main()
