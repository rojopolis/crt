'''
Local Compute Driver
'''
from .instance import ComputeInstance
import logging

logger = logging.getLogger(__name__)


class LocalComputeInstance(ComputeInstance):
    '''
    Represents the localhost.  For dev/testing
    '''
    provider = 'local'

    def __init__(self):
        pass

    def _refresh_state(self):
        pass

    # Public interface
    @classmethod
    def create(cls, template, client=None):
        logger.debug('Creating local instance')
        return cls()

    def delete(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    @property
    def ready(self):
        return True

    @property
    def addresses(self):
        '''
        Dict of public and private ip addresses
        {'public': [],
         'private': []}
        '''
        public = []
        private = ['127.0.0.1']

        return {'private': private,
                'public': public}
