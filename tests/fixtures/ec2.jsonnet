{
    compute: {
        provider: 'ec2',
        auth: {
            access_key: '12345',
            secret_key: '67890',
            region: 'us-west-2',
        },
        instance: {
            block_device_mapping: [
                {
                    device_name: 'string',
                    virtual_name: 'string',
                    ebs: {
                        encrypted: true,
                        delete_on_termination: true,
                        iops: 123,
                        kms_key_id: 'string',
                        snapshot_id: 'string',
                        volume_size: 123,
                        volume_type: 'string'
                    },
                    no_device: 'string'
                },
            ],
            image_id: 'string',
            instance_type: 't1.micro',
            ipv6_address_count: 123,
            ipv6_addresses: [
                {
                    ipv6_address: 'string'
                },
            ],
            kernel_id: 'string',
            key_name: 'string',
            MaxCount: 1,
            MinCount: 1,
            monitoring: {
                enabled: true
            },
            placement: {
                availability_zone: 'string',
                affinity: 'string',
                group_name: 'string',
                host_id: 'string',
                tenancy: 'default',
                SpreadDomain: 'string'
            },
            ramdisk_id: 'string',
            security_group_ids: [
                'string',
            ],
            security_groups: [
                'string',
            ],
            subnet_id: 'string',
            user_data: 'string',
            additional_info: 'string',
            client_token: 'string',
            disable_api_termination: true,
            dry_run: true,
            ebs_optimized: true,
            iam_instance_profile: {
                arn: 'string',
                name: 'string'
            },
            instance_initiated_shutdown_behavior: 'terminate',
            network_interfaces: [
                {
                    associate_public_ip_address: true,
                    delete_on_termination: true,
                    description: 'string',
                    device_index: 123,
                    groups: [
                        'string',
                    ],
                    ipv6_address_count: 123,
                    ipv6_addresses: [
                        {
                            ipv6_address: 'string'
                        },
                    ],
                    network_interface_id: 'string',
                    private_ip_address: 'string',
                    private_ip_addresses: [
                        {
                            primary: true,
                            private_ip_address: 'string'
                        },
                    ],
                    secondary_private_ip_address_count: 123,
                    subnet_id: 'string'
                },
            ],
            private_ip_address: 'string',
            elastic_gpu_specification: [
                {
                    type: 'string'
                },
            ],
            tag_specifications: [
                {
                    resource_type: 'instance',
                    tags: [
                        {
                            key: 'string',
                            value: 'string'
                        },
                    ]
                },
            ],
            launch_template: {
                launch_template_id: 'string',
                launch_template_name: 'string',
                version: 'string'
            },
            instance_market_options: {
                market_type: 'spot',
                spot_options: {
                    max_price: 'string',
                    spot_instance_type: 'one-time',
                    block_duration_minutes: 123,
                    valid_until: 'string',
                    instance_interruption_behavior: 'terminate'
                }
            },
            credit_specification: {
                cpu_credits: 'string'
            },
            cpu_options: {
                core_count: 123,
                threads_per_core: 123
            }
        },
    },
}
