local image_id = 'ami-1e63797e';
{
    compute: {
        provider: 'ec2',
        auth: {
            access_key: '12345',
            secret_key: '67890',
            region: 'us-west-2',
        },
        instance: {
            region: 'us-west-1',
            ImageId: image_id,
            MinCount: 1,
            MaxCount: 1,
        },
    },
}
