'''
EC2 Compute Driver
'''
from .compute_instance import ComputeInstance
import boto3
import logging

logger = logging.getLogger(__name__)


class EC2ComputeInstance(ComputeInstance):
    '''
    Represents a Compute instance on AWS EC2
    '''
    def __init__(self, id, region):
        '''
        Initialize the provider library and fetch instance.
        '''
        self.id = id
        self.region = region

        self._ec2 = boto3.client('ec2', region_name=region)

    def _refresh_state(self):
        '''
        Fetch state from provider
        '''
        try:
            self._state = self._ec2.describe_instances(InstanceIds=[self.id])
        except Exception as exc:
            self._state = {}
            logger.warn('Failed to fetch state', exc_info=exc)

    # Public interface
    @classmethod
    def create(cls, name, region, template=None, spec=None):
        '''
        Create instance on EC2
        '''
        ec2 = boto3.client('ec2', region_name=region)
        args = {}
        if spec is not None:
            args.update(spec)
        if template is not None:
            args['LaunchTemplate'] = template
        response = ec2.run_instances(MinCount=1, MaxCount=1, **args)
        logger.debug(response)
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
