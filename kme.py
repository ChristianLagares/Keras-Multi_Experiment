import ipyparallel as ipp


class WorkerServer(object):
    '''Docstring'''
    
    pass

class ParameterServer(object):
    '''
    ParameterServer

    This object has a master template for building models provide by the user
    and sends work to IPyParallel workers for execution, receives their results,
    queries Comet.ML parameter optimization API for new parameters and resubmits
    the loop.

    Interprocess comunication includes the traditional mechanisms provided by
    ZeroMQ (through IPyParallel) and file-based comunication for model loading.
    '''
    pass
