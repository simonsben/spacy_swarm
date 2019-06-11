# Spacy load balencer

This is a utility project meant to make it easy to launch a set of [SpaCy](https://spacy.io/) containers.
As the current (version 2) goal for SpaCy is to optimize the single-core efficiency, this project is meant to leverage multi-core machines.

**NOTE:** the code was written for windows systems (i.e. I wrote .bat utility scripts instead of .sh ones)

The code is based on the code found [here](https://docs.docker.com/get-started/part3/).
