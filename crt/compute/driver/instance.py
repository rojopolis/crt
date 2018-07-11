from abc import ABCMeta, abstractmethod, abstractproperty
import datetime
import logging
import time

logger = logging.getLogger(__name__)


class ComputeInstance(object):
    '''
    ComputeInstance represents provider compute instance
    '''
    __metaclass__ = ABCMeta
    # _state should contain the data structure returned from the provider
    # when GET is called on the resource

    # TODO: should these be class vars?
    _state = None
    _last_refresh = datetime.datetime.min
    _state_duration = 60

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
    def create(cls, template):
        '''
        Create instance on provider
        '''
        for sc in cls.__subclasses__():
            if sc.provider == template['compute']['provider']:
                return sc.create(template)

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
        pass

    def wait_for_ready(self, timeout=600):
        '''
        Block until self.ready==True or timeout is excceeded
        '''
        while not self.ready and timeout > 0:
            time.sleep(10)
            timeout -= 10
            logger.debug('Waiting... timeout in %d seconds', timeout)

    @property
    def state(self):
        now = datetime.datetime.now()
        age = now - self._last_refresh
        if age.seconds > self._state_duration:
            logger.debug('Refreshing state.')
            self._refresh_state()
            self._last_refresh = now
        else:
            logger.debug('Returning cached state.')
        return self._state

    @abstractproperty
    def ready(self):
        '''
        True if the instance is booted and ready to accept work
        '''
        pass

    @abstractproperty
    def addresses(self):
        '''
        Dict of public and private ip addresses
        {'public': [],
         'private': []}
        '''
        pass


create_instance = ComputeInstance.create
