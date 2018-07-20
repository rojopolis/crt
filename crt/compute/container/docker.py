from __future__ import absolute_import
from .container import ComputeContainer
import docker
import logging

logger = logging.getLogger(__name__)


class DockerContainer(ComputeContainer):
    provider = 'docker'

    def __init__(self, container):
        self._container = container

    def _refresh_state(self):
        '''
        Fetch state from provider
        '''
        self._container.reload()
        self._state = dict(self._container.__dict__)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.delete()

    @classmethod
    def create(cls, template, host=None, client=None):
        '''
        Create container
        '''
        body = dict(template).get('compute').get('container')
        provider = body.pop('provider', None)
        logger.debug('Create container: %s', provider)
        if client is None:
            client = cls.get_client(
                host=host,
                port=body.pop('port', None),
                tls_config=body.pop('tls_config', None),
            )
        client.images.pull(body.get('image'))
        container = client.containers.create(**body)
        return cls(container=container)

    def start(self):
        self._container.start()

    def stop(self):
        self._container.stop()

    def delete(self):
        self._container.remove()

    @staticmethod
    def get_client(host, port=None, tls_config=None):
        if port is None:
            if tls_config is not None:
                port = 2376
            else:
                port = 2375

        if tls_config is not None:
            tls_config = docker.tls.TLSConfig(
                ca_cert=tls_config.get('ca_cert'),
                client_cert=(
                    tls_config.get('client_cert'),
                    tls_config.get('client_key'),
                )
            )

        return docker.DockerClient(
            base_url='tcp://{}:{}'.format(host, port),
            tls=tls_config
        )


create_container = ComputeContainer.create
