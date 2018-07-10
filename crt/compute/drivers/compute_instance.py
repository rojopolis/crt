from abc import ABCMeta, abstractmethod


class ComputeInstance(object):
    '''
    ComputeInstance represents provider compute instance
    '''
    __metaclass__ = ABCMeta
    # _state should contain the data structure returned from the provider
    # when GET is called on the resource
    _state = None

    @abstractmethod
    def _refresh_state(self):
        '''
        Fetch state from provider
        '''
        pass

    # Context manager interface
    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.delete()

    # Public interface
    @classmethod
    def create(cls, spec):
        '''
        Create instance on provider
        '''
        pass

    @abstractmethod
    def delete(self):
        '''
        Stop and delete instance from provider
        '''
        pass

    @abstractmethod
    def start(self):
        '''
        Start instance
        '''
        pass

    @abstractmethod
    def stop(self):
        '''
        Stop instance
        '''

    @property
    def state(self):
        self._refresh_state()
        return self._state
