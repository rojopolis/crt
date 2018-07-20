'''
GCE Compute Driver
'''
from .instance import ComputeInstance
import googleapiclient.discovery
import datetime
import logging

logger = logging.getLogger(__name__)


# pylint: disable=no-member
class GCEComputeInstance(ComputeInstance):
    '''
    Represents a Compute Instance on Google Compute Engine
    https://cloud.google.com/compute/docs/reference/rest/v1/instances
    '''
    provider = 'gce'

    def __init__(self, iid, project, zone):
        '''
        Initialize the provider library and fetch instance.
        '''
        self.id = iid
        self.project = project
        self.zone = zone

        self._gce = None

    def _refresh_state(self):
        '''
        Fetch state from provider
        '''
        if self._gce is None:
            self._gce = googleapiclient.discovery.build('compute', 'v1')
        request = self._gce.instances().get(
            project=self.project,
            zone=self.zone,
            instance=self.id
            )
        try:
            self._state = request.execute()
            logger.debug('instances.get response: %s', self._state)
            self._last_refresh = datetime.datetime.now()
        except Exception as exc:
            self._state = None
            logger.debug('Failed to fetch state', exc_info=exc)

    # Public interface
    @classmethod
    def create(cls, template, client=None):
        '''
        Create instance on GCE
        https://cloud.google.com/compute/docs/reference/rest/v1/instances/insert
        '''
        if client is None:
            gce = googleapiclient.discovery.build('compute', 'v1')
        else:
            gce = client
        body = template.to_camel()['compute']['instance']
        iid = body.get('name')
        project = body.pop('project', None)
        zone = body.pop('zone', None)
        template = body.pop('sourceInstanceTemplate', None)
        request = gce.instances().insert(
            project=project,
            zone=zone,
            body=body,
            sourceInstanceTemplate=template
        )
        op = request.execute()
        logger.debug('instances.insert response: %s', op)
        return cls(iid, project, zone)

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
    def ready(self):
        '''
        True if the instance is booted and ready to accept work
        Note:  This method forces the state to refresh... it should be called
               sparingly.
        '''
        self._refresh_state()
        status = self.state.get('status')
        return status == 'RUNNING'

    @property
    def addresses(self):
        '''
        Dict of public and private ip addresses
        {'public': [],
         'private': []}
        '''
        public = [[y.get('natIP') for y in x['accessConfigs']][0]
                  for x in self.state['networkInterfaces']]

        private = [x['networkIP'] for x in self.state['networkInterfaces']]

        return {'private': private,
                'public': public}
