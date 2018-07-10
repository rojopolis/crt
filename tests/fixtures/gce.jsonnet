local project_id = 'dev-000001';
local zone = 'us-central1-b';
local machine_type = 'f1-micro';
{
    compute: {
        provider: 'gce',
        auth: {
            service_account_file: '/path/to/credential.json'
        },
        instance: {
            machine_type: 'zones/' + zone + '/machineTypes/' + machine_type,
            name: 'pooty',
            networkInterfaces: [
                {
                    network: 'global/networks/default',
                    access_configs: [
                        {
                            type: 'ONE_TO_ONE_NAT',
                            name: 'NAT'
                        }
                    ]
                }
            ],
            disks: [
                {
                    boot: true,
                    initialize_params: {
                        sourceImage: 'projects/debian-cloud/global/images/family/debian-9',
                        disk_size_gb: 10,
                        disk_type: 'projects/' + project_id + '/zones/us-central1-b/diskTypes/pd-standard'
                },
                auto_delete: true
                }
            ]
        },
    },
}