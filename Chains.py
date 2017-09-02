from copy import deepcopy


# make chains from a given mapping
def makeChains(mapping):
    chains = []
    for letter in mapping.keys():
        word = letter
        char = letter
        try:
            while True:
                word += mapping[char]
                char = mapping[char]
        except KeyError:
            chains.append(word)
    return thinChains(chains)


# keep only unique chains
def thinChains(chains):
    uniqueChains = deepcopy(chains)
    for chain in chains:
        if any(chain in test for test in chains if len(test) > len(chain)):
            uniqueChains.remove(chain)
    return uniqueChains
