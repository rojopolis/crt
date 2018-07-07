'''
GCE Compute Driver
'''
from compute_instance import ComputeInstance
import googleapiclient.discovery
from googleapiclient.errors import HttpError
import logging

logger = logging.getLogger(__name__)


# pylint: disable=no-member
class GCEComputeInstance(ComputeInstance):
    '''
    Represents a Compute Instance on Google Compute Engine
    https://cloud.google.com/compute/docs/reference/rest/v1/instances
    '''
    def __init__(self, id, project, zone):
        '''
        Initialize the provider library and fetch instance.
        '''
        self.id = id
        self.project = project
        self.zone = zone

        self._gce = googleapiclient.discovery.build('compute', 'v1')
        self._refresh_state()

    def _refresh_state(self):
        '''
        Fetch state from provider
        '''
        request = self._gce.instances().get(
            project=self.project,
            zone=self.zone,
            instance=self.id
            )
        try:
            self._state = request.execute()
        except HttpError as exc:
            self._state = None
            logger.debug('Failed to fetch state', exc_info=exc)

    # Public interface
    @classmethod
    def create(cls, name, project, zone, template=None, spec=None):
        '''
        Create instance on provider
        https://cloud.google.com/compute/docs/reference/rest/v1/instances/insert
        '''
        gce = googleapiclient.discovery.build('compute', 'v1')
        body = {}
        if spec is not None:
            body.update(spec)
        body['name'] = name
        request = gce.instances().insert(
            project=project,
            zone=zone,
            body=body,
            sourceInstanceTemplate=template
        )
        op = request.execute()
        logger.debug(op)
        return cls(name, project, zone)

    def delete(self):
        '''
        Stop and delete instance from provider
        '''
        request = self._gce.instances().delete(
            project=self.project,
            zone=self.zone,
            instance=self.id
        )
        request.execute()

    def start(self):
        '''
        Start instance
        '''
        request = self._gce.instances().start(
            project=self.project,
            zone=self.zone,
            instance=self.id
        )
        request.execute()

    def stop(self):
        '''
        Stop instance
        '''
        request = self._gce.instances().stop(
            project=self.project,
            zone=self.zone,
            instance=self.id
        )
        request.execute()

    @property
    def state(self):
        self._refresh_state()
        return self._state
