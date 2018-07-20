import json
import pytest
import boto3
from botocore.stub import Stubber
from crt.compute.instance.ec2 import EC2ComputeInstance
from crt.template import Template


@pytest.fixture
def ec2_describe_instances_response():
    with open('tests/fixtures/ec2.describe_instances.response.json') as f:
        data = f.read()
    return json.loads(data)


@pytest.fixture
def ec2_run_instances_response():
    with open('tests/fixtures/ec2.run_instances.response.json') as f:
        data = f.read()
    return json.loads(data)


@pytest.fixture
def ec2_instance(ec2_describe_instances_response):
    instance = EC2ComputeInstance(iid='123456', region='us-east-1')
    stubber = Stubber(instance._ec2)
    stubber.add_response('describe_instances', ec2_describe_instances_response)
    with stubber:
        instance._refresh_state()
    return (instance, stubber)


def test_get(ec2_instance):
    instance, _ = ec2_instance
    state = instance.state
    assert state['InstanceId'] == 'i-00cf013697cc3bc02'


# def test_ready(ec2_instance):
#    instance, stubber = ec2_instance
#    with stubber:
#        assert instance.ready


# def test_start(ec2_instance):
#    instance, stubber = ec2_instance
#    with stubber:
#        assert instance.start()


# def test_stop(ec2_instance):
#    ec2_instance.stop()


# def test_delete(ec2_instance):
#    ec2_instance.delete()


def test_addresses(ec2_instance):
    instance, _ = ec2_instance
    assert instance.addresses['private'][0] == '172.31.10.182'


def test_create(ec2_run_instances_response):
    client = boto3.client('ec2', region_name='us-east')
    stubber = Stubber(client)
    stubber.add_response('run_instances', ec2_run_instances_response)
    with stubber:
        inst = EC2ComputeInstance.create(
            Template(path='tests/fixtures/ec2.jsonnet'),
            client=client)
    assert isinstance(inst, EC2ComputeInstance)
