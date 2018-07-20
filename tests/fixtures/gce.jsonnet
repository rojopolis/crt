local project = 'dev-000001';
local zone = 'us-central1-b';
local name = 'i' + std.native('uuidgen')();
local machine_type = 'projects/' + project + '/zones/' + zone + '/machineTypes/g1-small';
local image = 'global/images/family/rancheros';
local readfile = std.native('readfile');
{
    compute: {
        provider: 'gce',
        auth: {
            service_account_file: '/path/to/credential.json'
        },
        instance: {
            project: project,
            zone: zone,
            source_instance_template: null,
            machine_type: machine_type,
            name: name,
            description: name,
            can_ip_forward: false,
            scheduling: {
                preemptible: true
            },
            network_interfaces: [
                {
                    network: 'global/networks/default',
                    access_configs: [
                        {
                            type: 'ONE_TO_ONE_NAT',
                            name: 'External NAT'
                        },
                    ],
                }
            ],
            disks: [
                {
                    initialize_Params: {
                        source_image: image,
                        disk_size_gb: "10",
                        disk_type: 'zones/us-central1-b/diskTypes/pd-standard'
                    },
                    boot: true,
                    auto_delete: true,
                }
            ],
            metadata: {
                items: [
                    {
                        key: 'user-data',
                        value: readfile('tests/fixtures/cloud-config.yml')
                    }
                ],
            },
        },
        container: {
            provider: 'docker',
            port: 2376,
            tls_config: {
                ca_cert: 'tests/functional/ca.pem',
                client_cert: 'tests/functional/cert.pem',
                client_key: 'tests/functional/key.pem'
            },
            image: 'debian',
        },
    },
}