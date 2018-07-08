'''
Azure Resource Manager Driver
'''
from .compute_instance import ComputeInstance
import logging

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient

logger = logging.getLogger(__name__)


class ARMComputeInstance(ComputeInstance):
    '''
    Represents a Compute instance on Azure
    '''
    def __init__(self, id, resource_group,
                 subscription_id, application_id,
                 authentication_key, tenant_id):
        '''
        Initialize the provider library and fetch instance.
        '''
        self.id = id
        self.resource_group = resource_group
        self._credential = ServicePrincipalCredentials(
            client_id=application_id,
            secret=authentication_key,
            tenant=tenant_id
        )

        self._compute_client = ComputeManagementClient(
            self._credential,
            subscription_id
        )

    def _refresh_state(self):
        '''
        Fetch state from provider
        '''
        try:
            instance = self._compute_client.virtual_machines.get(
                self.resource_group,
                self.id,
                expand='instanceView'
            )
            self._state = instance.as_dict()
        except Exception as exc:
            self._state = {}
            logger.warn('Failed to fetch state', exc_info=exc)

    @classmethod
    def create(cls, name, resource_group,
               subscription_id, application_id,
               authentication_key, tenant_id,
               template=None, spec=None):
        '''
        Create instance on ARM
        '''
        pass

    def delete(self):
        '''
        Stop and delete instance from provider
        '''
        self._compute_client.virtual_machines.deallocate(
            self.resource_group,
            self.id
        )

    def start(self):
        '''
        Start instance
        '''
        self._compute_client.virtual_machines.start(
            self.resource_group,
            self.id
        )

    def stop(self):
        '''
        Stop instance
        '''
        self._compute_client.virtual_machines.power_off(
            self.resource_group,
            self.id
        )
