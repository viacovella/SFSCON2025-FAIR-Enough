import numpy as np
import pandas as pd
import sys

target_path = sys.argv[1]

# Generic categories
all_categories = np.array(["A","B","C","D","E","F","G","H"])

### Simulation control panel

# number of trials shown
nrepetitions = 100
# number of discrimination categories
ncategories = 4
# percentage of simulated error
perc_errors = 5
# percentage of simulated misses
perc_misses = 2

# number of errors according to trial size
nerrors=int(nrepetitions*perc_errors/100)

# number of misses according to trial size
nmisses=int(nrepetitions*perc_misses/100)

# number of expected different objects
diff_obs = int(nrepetitions / ncategories)

# Average reaction time
avgrt = 0.3

### Correct Responses, Actual responses

# create random permutations of the n categories
perm_idxs=np.random.default_rng().permutation(nrepetitions)
num_trials=np.repeat(np.arange(ncategories),diff_obs)[perm_idxs]

# connect permutations to categories and build correct and actual responses vectors
trials = np.array([all_categories[i] for i in num_trials])
responses = np.array([all_categories[i] for i in num_trials])

# initialize a responses vector assuming all the responses are correct
print(sum([responses[i] == trials[i] for i in np.arange(nrepetitions)]))

# introduce response errors into responses vector
error_and_misses_idxs=np.random.default_rng().permutation(nrepetitions)[np.arange(nerrors + nmisses)]
responses[error_and_misses_idxs[np.arange(nerrors)]] = responses[np.arange(nerrors)]

# introduce misses into responses vector
responses[error_and_misses_idxs[np.arange(nerrors,nerrors+nmisses)]] = "0"

print(sum([responses[i] == trials[i] for i in np.arange(nrepetitions)]))

## Reaction times
rt = np.random.normal(avgrt,0.05,nrepetitions)
rt[error_and_misses_idxs[np.arange(nerrors,nerrors+nmisses)]] = 0

# Create a DataFrame to hold the synthetic data
adf = pd.DataFrame(columns=["trial","response","rt"])
adf["trial"] = trials
adf["response"] = responses
adf["rt"] = rt

adf.to_csv(target_path, sep="\t", index=False)