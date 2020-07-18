# Aim #
The aim of the project is to observe Effective Connectivity during motor imagery tasks and compare it with neuroscientific literature. Normalised Transfer Entropy and Partial Directed Coherence are used to generate information flow graphs. The information flow graphs are evaluated with those of Transfer Entropy and Granger Causality using Graph Similarity Metrics.

## Dataset Description ##

Dataset used for the study is [BCI iv 2a](http://www.bbci.de/competition/iv/) consisting of EEG data from 9 subjects. Cue-based BCI paradigm consisted of imagination of 4 movements i.e Left Hand(1.0), Right Hand(2.0), Both feet(3.0), tongue(4.0). Each subject consisted of training session and evaluation session with around 288 trials per each session.

## Preprocessing ##

Data is preprocessed by calling the [preprocess](preprocess.py) function. Preprocessing involves two phases:
  1. Averaging the data over all trials to eliminate noise and bias
  2. Passing the signal through a bandpass filter

## Effective Connectivity ##

[NTE](NTE.py), [Partial Directed Coherence](PDC.py) returns adjacency matrix graph estimated by NTE and PDC respectively. Similarly information flwo graphs of Transfer Entropy and Granger Causality can be obtained by running the corresponding scripts. [Graph Similarity](GED.py) estimates graph edit distance between two adjacency matrices.

# Report #
For detailed analysis and conclusion kindly look at [my project report](Report.txt)

