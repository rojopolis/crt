import os
import uuid
from crt.template import Template


def test_native():
    os.environ['__JSONNET_TEST'] = '123456789'
    snippet = '''
    local env = std.native('getenv')();
    local uuidgen = std.native('uuidgen');
    {
        env_test: env.__JSONNET_TEST,
        uuid_test: uuidgen()
    }
    '''
    t = Template(body=snippet)
    assert t['env_test'] == '123456789'
    uuid.UUID(t['uuid_test'])


def test_jsonnet_file():
    t = Template(path='tests/fixtures/gce.jsonnet')
    assert t


def test_jsonnet_snippet():
    with open('tests/fixtures/gce.jsonnet', 'r') as f:
        t = Template(body=f.read())
    assert t


def test_json_file():
    t = Template(path='tests/fixtures/gce.instances.insert.response.json')
    assert t


def test_json_snippet():
    with open('tests/fixtures/gce.instances.insert.response.json') as f:
        t = Template(body=f.read())
    assert t
