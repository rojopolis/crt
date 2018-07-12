'''
EC2 Compute Driver
'''
from .instance import ComputeInstance
import boto3
import datetime
import logging

logger = logging.getLogger(__name__)


class EC2ComputeInstance(ComputeInstance):
    '''
    Represents a Compute instance on AWS EC2
    '''
    provider = 'ec2'

    def __init__(self, iid, region):
        '''
        Initialize the provider library and fetch instance.
        '''
        self.id = iid
        self.region = region

        self._ec2 = boto3.client('ec2', region_name=region)

    def _refresh_state(self):
        '''
        Fetch state from provider
        '''
        try:
            response = self._ec2.describe_instances(InstanceIds=[self.id])
            logger.debug('describe_instances response: %s', response)
            if not len(response.get('Reservations', [])) == 1:
                logger.warn('Received %d Reservations. Should be exactly one.')
            if not len(response['Reservations'][0]['Instances']) == 1:
                logger.warn('Received %d Instances. Should be exactly one.')
            self._state = response['Reservations'][0]['Instances'][0]
            self._last_refresh = datetime.datetime.now()
        except Exception as exc:
            self._state = None
            logger.debug('Failed to fetch state', exc_info=exc)

    # Public interface
    @classmethod
    def create(cls, template, client=None):
        '''
        Create instance on EC2
        '''
        body = template.to_pascal()['compute']['instance']
        region = body.pop('region')
        if client is None:
            ec2 = boto3.client('ec2', region_name=region)
        else:
            ec2 = client
        response = ec2.run_instances(**body)
        logger.debug('run_instances response: %s', response)
        iid = response['Instances'][0]['InstanceId']
        return cls(iid, region)

    def delete(self):
        '''
        Stop and delete instance from provider
        '''
        self._ec2.terminate_instances(InstanceIds=[self.id])

    def start(self):
        '''
        Start instance
        '''
        self._ec2.start_instances(InstanceIds=[self.id])

    def stop(self):
        '''
        Stop instance
        '''
        self._ec2.stop_instances(InstanceIds=[self.id])

    @property
    def ready(self):
        '''
        True if the instance is booted and ready to accept work
        Note:  This method forces the state to refresh... it should be called
               sparingly
        '''
        self._refresh_state()
        status = self.state.get('State')
        return status['Name'] == 'running'

    @property
    def addresses(self):
        public = [x['Association']['PublicIp']
                  for x in self.state['NetworkInterfaces']]
        private = [x['PrivateIpAddress']
                   for x in self.state['NetworkInterfaces']]
        return {'public': public,
                'private': private}
