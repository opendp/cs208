import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

data: pd.DataFrame = pd.read_csv("https://raw.githubusercontent.com/opendp/cs208/refs/heads/main/spring2025/data/fake_patient_dataset.csv")

# names of public identifier columns
pub = ["id", "age", "sex", "blood"]

# variable to reconstruct
target = "invoice"

epsilon = 0.1

# Returns the ULP in base-2 of a floating-point number
def get_ulp_base2(x):
    return math.log2(math.ulp(x))

# Release a DP count over the invoice column for patients in the dataset with ID = id
def release_dp_count(query):
    sensitivity = 1
    scale = sensitivity/epsilon
    sensitive_count = query(data)
    return sensitive_count + np.random.laplace(loc=0.0, scale=scale)

# Implement the hypothesis test!
def hypothesis_test(observed):
    pass

num_experiments = 10000

# Run the experiments
for _ in range(num_experiments):

    # Randomly choose a patient ID
    id = np.random.randint(0, len(data))

    # Example counting query...
    # counts the number of individuals in the dataset patient ID = id and invoice amount = 1000
    # you'll want to update this!
    observed = release_dp_count(
        lambda data: (data.loc[data['id'] == id, 'invoice'] == 1000).sum()
    )

    # 1 = reject null, 0 otherwise
    decision = hypothesis_test(observed)


# estimate the TPR and FPR of your attack
