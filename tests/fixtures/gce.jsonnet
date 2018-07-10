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
            sourceInstanceTemplate: null,
            machineType: machine_type,
            name: name,
            description: name,
            canIpForward: false,
            networkInterfaces: [
                {
                    network: 'global/networks/default'
                }
            ],
            disks:[
                {
                    initializeParams: {
                        sourceImage: image,
                        diskSizeGb: "10",
                        diskType: 'zones/us-central1-b/diskTypes/pd-standard'
                    },
                    boot: true,
                    autoDelete: true,
                }
            ]
        },
    },
    container: {
        provider: 'docker'
    },
}