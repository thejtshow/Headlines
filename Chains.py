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
    return chains


# keep only unique chains
def thinChains(chains):
    uniqueChains = []
    return uniqueChains
