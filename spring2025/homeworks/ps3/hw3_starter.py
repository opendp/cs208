import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

data: pd.DataFrame = pd.read_csv("https://raw.githubusercontent.com/opendp/cs208/refs/heads/main/spring2025/data/fake_patient_dataset.csv")

# names of public identifier columns
pub = ["id", "age", "sex", "blood"]

# variable to reconstruct
target = "invoice"


# Returns the ULP in base-2 of a floating-point number
def get_ulp_base2(x):
    return math.log2(math.ulp(x))

# Release a DP sum over the invoice column for patients in the dataset with ID = id
# Fill in the sensitivity and scale parameters
def release_dp_sum(id, epsilon):
    sensitivity = 
    scale = 
    sensitive_sum = data.loc[data['id'] == id, 'invoice'].sum()
    return sensitive_sum + np.random.laplace(loc=0.0, scale=scale)


# Implement the hypothesis test!
def hypothesis_test(observed):
    pass

epsilon = 0.1
num_experiments = 10000

# Run the experiments
for _ in range(num_experiments):
    # Randomly choose a patient ID
    id = np.random.randint(0, len(data))

    # Receive a DP sum over the patient's invoice value
    observed = release_dp_sum(id, epsilon)

    # 1 = reject null, 0 otherwise
    decision = hypothesis_test(observed)


# estimate the TPR and FPR of your attack
