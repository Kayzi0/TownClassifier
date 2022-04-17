# TownClassifier
Attempt to classify the location of a town based only on the name using a neural network 

The dataset consist of a collection of town names from Spain, France, China, and the Catalan speaking regions of Spain. 

It uses unicode encoding of the letters as integers to feed as zero-padded one-dimensional arrays into the network. The sizes of the datasets have been altered, as the sets were quite unbalanced. Data augmentation (in this case, doubling the data through using both upper and lower case) has been applied.

# Results

A simple fully connected-network and a simple convolutional network have been tested. The convolutional network yields around 60% test accuracy so far. The net architecture is likely the main bottleneck at the moment, as data augmentation improved the accucary, but not significantly.
