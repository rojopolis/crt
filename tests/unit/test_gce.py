# pylint: disable=import-error
import pytest
from apiclient.discovery import build_from_document
from apiclient.http import HttpMockSequence
from crt.compute.driver.gce import GCEComputeInstance
from crt.template import Template


@pytest.fixture
def gce_discovery_service():
    with open('tests/fixtures/gce.discovery.response.json') as f:
        return f.read()


@pytest.fixture
def gce_instance_get_service(gce_discovery_service):
    with open('tests/fixtures/gce.instances.get.response.json') as f:
        request = f.read()
    http = HttpMockSequence([
        ({'status': '200'}, request)
    ])
    service = build_from_document(gce_discovery_service, http=http)
    return service


@pytest.fixture
def gce_operation(gce_discovery_service):
    with open('tests/fixtures/gce.instances.insert.response.json') as f:
        request = f.read()
    http = HttpMockSequence([
        ({'status': '200'}, request)
    ])
    service = build_from_document(gce_discovery_service, http=http)
    return service


@pytest.fixture
def gce_instance(gce_instance_get_service):
    instance = GCEComputeInstance(
        iid='test-12345',
        project='dev-000001',
        zone='us-central1-b'
    )
    instance._gce = gce_instance_get_service
    return instance


def test_get(gce_instance):
    state = gce_instance.state
    assert state['name'] == 'test-instance'


def test_ready(gce_instance):
    assert gce_instance.ready


def test_start(gce_instance):
    gce_instance.start()


def test_stop(gce_instance):
    gce_instance.stop()


def test_delete(gce_instance):
    gce_instance.delete()


def test_addresses(gce_instance):
    assert gce_instance.addresses['private'][0] == '10.138.0.2'


def test_create(gce_operation):
    inst = GCEComputeInstance.create(
        Template(path='tests/fixtures/gce.jsonnet'),
        client=gce_operation)
    assert isinstance(inst, GCEComputeInstance)
