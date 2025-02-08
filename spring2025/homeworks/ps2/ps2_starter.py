# Starter code for Homework 2.
import numpy as np
import pandas as pd


# Problem setup

# Update to point to the dataset on your machine
data: pd.DataFrame = pd.read_csv("https://raw.githubusercontent.com/opendp/cs208/refs/heads/main/spring2025/data/fake_healthcare_dataset_sample100.csv")

# names of public identifier columns
pub = ["age", "sex", "blood", "admission"]

# variable to reconstruct
target = "result"


def execute_subsetsums_exact(predicates):
    """Count the number of patients that satisfy each predicate.
    Resembles a public query interface on a sequestered dataset.
    Computed as in equation (1).

    :param predicates: a list of predicates on the public variables
    :returns a 1-d np.ndarray of exact answers the subset sum queries"""
    return data[target].values @ np.stack([pred(data) for pred in predicates], axis=1)


def make_random_predicate():
    """Returns a (pseudo)random predicate function by hashing public identifiers."""
    prime = 2003
    desc = np.random.randint(prime, size=len(pub))
    # this predicate maps data into a 1-d ndarray of booleans
    #   (where `@` is the dot product and `%` modulus)
    return lambda data: ((data[pub].values @ desc) % prime % 2).astype(bool)


if __name__ == "__main__":
    # EXAMPLE: writing and using predicates
    num_female_patients, num_emergency_admits = execute_subsetsums_exact([
        lambda data: data['sex'] == 1,      # "is-female" predicate
        lambda data: data['admission'] == 2,  # "had emergency admission" predicate
    ])

    print(num_female_patients)
    print(num_emergency_admits)
    # EXAMPLE: making and using a random predicate
    example_predicate = make_random_predicate()
    num_patients_that_matched_random_predicate = execute_subsetsums_exact([example_predicate])
    print(num_patients_that_matched_random_predicate)

    # The boolean mask from applying the example predicate to the data:
    example_predicate_mask = example_predicate(data)


# TODO: Write the reconstruction function!
def reconstruction_attack(data_pub, predicates, answers):
    """Reconstructs a target column based on the `answers` to queries about `data`.

    :param data_pub: data of length n consisting of public identifiers
    :param predicates: a list of k predicate functions
    :param answers: a list of k answers to a query on data filtered by the k predicates
    :return 1-dimensional boolean ndarray"""
    pass
