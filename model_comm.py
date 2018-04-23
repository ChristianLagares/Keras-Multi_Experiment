'''
Model Comunication Module

This file is used for file based comunication.

A worker can load functions for this module thus enabling file based
comunication. This design paradigm was selected due to the difficulty of
passing certain objects through IPyParallel's comunication interface. Currently,
we default to ZeroMQ, but it would be interesting to explore an MPI backend.
'''
