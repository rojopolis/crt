local project = 'dev-000001';
local zone = 'us-central1-b';
local name = 'pooper';
local machine_type = 'projects/' + project + '/zones/' + zone + '/machineTypes/f1-micro';
local image = 'global/images/family/rancheros';
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
            network_interfaces: [
                {
                    network: 'global/networks/default'
                }
            ],
            disks:[
                {
                    initialize_Params: {
                        source_image: image,
                        disk_size_gb: "10",
                        disk_type: 'zones/us-central1-b/diskTypes/pd-standard'
                    },
                    boot: true,
                    auto_delete: true,
                }
            ]
        },
    },
    container: {
        provider: 'docker'
    },
}