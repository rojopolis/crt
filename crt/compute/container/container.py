from abc import ABCMeta, abstractmethod
import datetime
import logging

logger = logging.getLogger(__name__)


class ComputeContainer(object):
    __metaclass__ = ABCMeta

    _state = None
    _last_refresh = datetime.datetime.min
    _state_duration = 60

    @abstractmethod
    def _refresh_state(self):
        '''
        Fetch state from provider
        '''
        raise NotImplementedError

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.delete()

    @classmethod
    def create(cls, template, host=None, client=None):
        '''
        Create container on instance
        '''
        for sc in cls.__subclasses__():
            if sc.provider == template['compute']['container']['provider']:
                return sc.create(template, host, client)

    @abstractmethod
    def start(self):
        raise NotImplementedError

    @abstractmethod
    def stop(self):
        raise NotImplementedError

    @abstractmethod
    def delete(self):
        raise NotImplementedError

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


create_container = ComputeContainer.create
