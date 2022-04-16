# CatTownGen
Small network to generate Catalan sounding town names

The dataset consist of a collection of town names from Spain, France, China, and the Catalan speaking regions of Spain. 

It uses unicode encoding of the letters as integers to feed as zero-padded one-dimensional arrays into the network. The sizes of the datasets have been altered, as the sets were quite unbalanced. 

# results

A simple fully connected-network and a simple convolutional network have been tested, both yielding fairly unsatisfying results (the best result so far being around 34% accuracy for the fully connected-network). The network seems to suffer largely from overfitting, introducing dropout layers has not improved this issue. obtaining a larger dataset (through augmentation or other means) might improve this issue.
