#  demonstrate membership attacks of Homer et al. (2008) and of Dwork, Smith, Steinke, Ullman, Vadhan (2015).
#  mS, jH 2022.2.02
import math

import numpy as np

## PARAMETERS
np.random.seed(123)

k_attributes = 100
n_sims = 10000
n_samples = 10
null_sims = 1000

# Generate underlying population attributes
population_prob = np.random.uniform(size=k_attributes)
population_mean = 2 * population_prob - 1.  # Because we are recoding to {-1,1} in next function


# A utility function to create data from the population
def rmvbernoulli(p, n=1):
    x = np.random.binomial(n=len(p), p=p, size=(n, len(p)))
    x[x == 0] = -1
    return x


## TEST STATISTICS
def test_homer(alice, sample_mean, population_mean, _referent):
    """Calculates the Homer test statistic"""
    test_statistic = sum(abs(alice - population_mean) - abs(alice - sample_mean))
    return test_statistic


def test_dwork(alice, sample_mean, population_mean, _referent):
    """Calculates the Dwork et al. test statistic using the population means"""
    return sum(alice * sample_mean) - sum(population_mean * sample_mean)


def test_dwork_referent(alice, sample_mean, _population_mean, referent):
    """Calculates the Dwork et al. test using only a single individual from the population as a referent"""
    return sum(alice * sample_mean) - sum(referent * sample_mean)


def null_distribution(fun, population_prob, null_sims=1000, alpha=0.05):
    """Simulates the null distribution"""
    # A null distribution and critical value generator
    population_mean = 2 * (population_prob - 0.5)
    hold = []

    for i in range(null_sims):
        # TODO: double check axis. apply(sample, MARGIN=2, ...) to columns
        sample_mean = rmvbernoulli(p=population_prob, n=n_samples).mean(axis=1)
        null_alice = rmvbernoulli(p=population_prob)
        referent = rmvbernoulli(p=population_prob)

        hold.append(fun(null_alice, sample_mean, population_mean, referent))

    null_dist_vals = np.sort(hold)
    return {
        "nulldist": null_dist_vals,
        "critical_val": null_dist_vals[round(alpha * null_sims)]
    }


# Visualize the null distribution
# TODO: finish this func
def show_distribution(x, critical_value, main="", bw='nrd0'):
    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.kdeplot(x)
    plt.show()


# showdist  =  function(x,criticalvalue, main="", bw="nrd0"){
#     testdens  =  density(x, bw=bw)
#     plot(testdens, main=main, xlab="Test Statistic")
#     semi_blue  =  rgb(0,90,239,180,maxColorValue=255)          # Slightly transparent colors
#     semi_red   =  rgb(239,90,0,180,maxColorValue=255)
#     flag  =  testdens["x"] < criticalvalue
#     polygon( c(min(testdens["x"]), testdens["x"][flag], criticalvalue), y=c(0, testdens["y"][flag], 0), col=semi_blue)
#     polygon( c(criticalvalue, testdens["x"][!flag], max(testdens["x"])), y=c(0, testdens["y"][!flag], 0), col=semi_red)
#     abline(v=criticalvalue, lwd=1.5)
#     accept.frac  =  round(100*mean(x>criticalvalue))/100
#     text(x=criticalvalue, y=0.8*max(testdens["y"]), labels=paste("OUT "), pos=2)
#     text(x=criticalvalue, y=0.8*max(testdens["y"]), labels=paste(" IN"), pos=4)
#     text(x=criticalvalue, y=0.7*max(testdens["y"]), labels=paste(accept.frac), pos=4)
# }

# Find the null distribution for test1
output = null_distribution(fun=test_homer, population_prob=population_prob)
testdist = output["nulldist"]
criticalValue = output["critical_val"]
show_distribution(testdist, criticalValue, main="Null Distribution with Critical Value")

## Export graph to .pdf ##
# dev.copy2pdf(file="./figs/nullDistribution.pdf")


# Simulate

# of length n_sims, with 9 values in each
history = []

myalpha = 0.01
nullDist_Homer = null_distribution(fun=test_homer, population_prob=population_prob,
                                   alpha=myalpha)  # Find null distributions
nullDist_Dwork = null_distribution(fun=test_dwork, population_prob=population_prob, alpha=myalpha)

for i in range(n_sims):
    # Simulate data
    sample = rmvbernoulli(n=n_samples, p=population_prob)
    # TODO: verify that axis=1 is right
    sample_mean = sample.mean(axis=1)
    alice = sample[0]
    nullAlice = rmvbernoulli(n=1, p=population_prob)
    referent = rmvbernoulli(n=1, p=population_prob)

    # Conduct tests
    test_alice_homer = test_homer(alice=alice, sample_mean=sample_mean, population_mean=population_mean,
                                  referent=referent)
    test_alice_dwork = test_dwork(alice=alice, sample_mean=sample_mean, population_mean=population_mean,
                                  referent=referent)
    test_null_alice_homer = test_homer(alice=nullAlice, sample_mean=sample_mean, population_mean=population_mean,
                                       referent=referent)
    test_null_alice_dwork = test_dwork(alice=nullAlice, sample_mean=sample_mean, population_mean=population_mean,
                                       referent=referent)

    # Store simulated values

    history[i, 1] = i
    history[i, 2] = test_alice_homer
    history[i, 3] = test_alice_homer > nullDist_Homer["criticalVal"]
    history[i, 4] = test_null_alice_homer
    history[i, 5] = test_null_alice_homer > nullDist_Homer["criticalVal"]
    history[i, 6] = test_alice_dwork
    history[i, 7] = test_alice_dwork > nullDist_Dwork["criticalVal"]
    history[i, 8] = test_null_alice_dwork
    history[i, 9] = test_null_alice_dwork > nullDist_Dwork["criticalVal"]

## Export graph to .pdf ##

par(mfrow=c(2, 2))
show_distribution(history[:, 2], critical_value=nullDist_Homer["criticalVal"], main="Homer Alice", bw=0.5)
show_distribution(history[:, 4], critical_value=nullDist_Homer["criticalVal"], main="Homer Null", bw=0.5)
Tvalue = math.sqrt(8 * k_attributes * math.log(1 / myalpha))
show_distribution(history[:, 6], critical_value=nullDist_Dwork["criticalVal"], main="Dwork Alice", bw=0.5)
abline(v=Tvalue, col="red", lty=2)
show_distribution(history[:, 8], critical_value=nullDist_Dwork["criticalVal"], main="Dwork Null", bw=0.5)
abline(v=Tvalue, col="red", lty=2)

# Create a PDF: dev.copy2pdf(file="./figs/membershipAttack.pdf")
