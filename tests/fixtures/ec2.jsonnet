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
            image_id: image_id,
            instance_type: 't2.small',
            min_count: 1,
            max_count: 1,
            user_data: '#cloud-config
write_files:
  - path: /etc/docker/tls/ca.pem
    permissions: "0755"
    owner: root
    content: |
      -----BEGIN CERTIFICATE-----
      MIIClDCCAXwCCQCP+wg4uUcExzANBgkqhkiG9w0BAQsFADAMMQowCAYDVQQDDAEq
      MB4XDTE4MDcxNzIyMzEzNloXDTIyMDcxNjIyMzEzNlowDDEKMAgGA1UEAwwBKjCC
      ASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAKujGaxtT2PFf3Y/08khnEnk
      dYzp0E9cBbpbuuAC/ARzdvKEw8lX6TWhBh7KHvGB7pdV76AqeT0gfLvLjPO/nm5r
      s28SZQbv2FkNqXoETm2RU0wwVvs1MgPLTztp/SJLXaeNW2qTlZXo6rKxw2gLwYao
      QOhXu2j1s7U1pjgZ/0n5B+O5TG1reYmixQFJOVCWyclgRIkAHufoqnGdAQNXDs99
      REyAWY4FB9pQX/Y1MXLAmOahfRTSmUqhYp5Vj215lmViuM1YOAwCF19oj8ZgLLIW
      BtGzgbIr1oVHOzAGpnaA398R94tVdwd1xsHQPzWnywbfS/Z+UcaUXIbOGxq2uZMC
      AwEAATANBgkqhkiG9w0BAQsFAAOCAQEAIiorm7hq+3WwRJp6xEh4kEwXYaNu0jrU
      bC15BOx4/PH3Bau0xBNlzJ+MMH1gLlot+ngZXQu53Ui+Qk5HKMx9BEnBaHIfcmVH
      JQHboxwHR3x5TfDenhKFbpLjjd1Qs58kogIKZYByc+VpDJz4m+TRiI0Z56XVA2Em
      S96dJ3l5zrXN7xuL8HmqTEVabaSedpmohdq3ctutEVBdnmAwdcLKGzQzG8H60byC
      xMJuyUMMlbc9psbSDuRYEO+3OZ4FTOrCX6Y/W8iX0gBhyF7kWbTTbIaK+uFGVpXM
      ieUddIG69CCAxxSOj1f0LmBA6y5wzeO7e1FPhkHFvk0m17tYazAnxQ==
      -----END CERTIFICATE-----
  - path: /etc/docker/tls/server-cert.pem
    permissions: "0755"
    owner: root
    content: |
      -----BEGIN CERTIFICATE-----
      MIICjDCCAXQCAQIwDQYJKoZIhvcNAQEFBQAwDDEKMAgGA1UEAwwBKjAeFw0xODA3
      MTcyMjMxMzdaFw0yMjA3MTYyMjMxMzdaMAwxCjAIBgNVBAMMASowggEiMA0GCSqG
      SIb3DQEBAQUAA4IBDwAwggEKAoIBAQDUf9X7Tvrcd9Zcrk4ZcU2jg1LzlqUq2wRG
      yTk+5X0KQlT7tsTVYezM9b6hMguIhHUdLqXS1zecqzIFyeReGXHCnZLKuPu6WKdB
      J0ybAKE1Rn/neIpoVC/PTMPruXeWVyWuSBVt9REczCvzGlANq9MMrP8MpDGVe+hK
      ybzBa8c4bU+B2yOUhSc3S/gskEcOuggL958NdKrjbWpc5kf7EhSJCaN49HYAniJM
      NM4wYOeD1iPrZT6lNqK5NSUfw5QkqoRFHKi0Lmyvad7CAWnd1aVh547uTgYAaIp2
      eopIxsbLSU423kylTwc1CyX/p6hId1HRFbD0TPRxxH3XAYBIisUXAgMBAAEwDQYJ
      KoZIhvcNAQEFBQADggEBABcM6WQU55/bDEbY/iCT41S3D/s1vm5S2v/izEw+E7fS
      qO9An/mzXRG2+Hegg0c+DFwFViT9sWuJKGXYPu69znxewWRUqx5M/N9KBlnn0QN2
      lxSEjgyCjGL8W3JtW2krnft2xtIpBfW7dPlc4+ABydA9hJyfsn7VLJyJ3aPPQPq8
      ebnbOap0BFW9ZkzJJeIh11+HtwJHCAWJobD1UQvktBDStvt2hU9YHhC4uYFv1jlu
      IN7O1+qZ5MmpJf1yU23MwUuJ9RVG1Rry2+e+6TFYQbUkbE0hIlmywbuuIy/6guyi
      U+SJHVeT2j01DWnxLg9TC89tYqmsF77IsI70BxHkZI0=
      -----END CERTIFICATE-----
  - path: /etc/docker/tls/server-key.pem
    permissions: "0600"
    owner: root
    content: |
      -----BEGIN RSA PRIVATE KEY-----
      MIIEpQIBAAKCAQEA1H/V+0763HfWXK5OGXFNo4NS85alKtsERsk5PuV9CkJU+7bE
      1WHszPW+oTILiIR1HS6l0tc3nKsyBcnkXhlxwp2Syrj7ulinQSdMmwChNUZ/53iK
      aFQvz0zD67l3llclrkgVbfURHMwr8xpQDavTDKz/DKQxlXvoSsm8wWvHOG1Pgdsj
      lIUnN0v4LJBHDroIC/efDXSq421qXOZH+xIUiQmjePR2AJ4iTDTOMGDng9Yj62U+
      pTaiuTUlH8OUJKqERRyotC5sr2newgFp3dWlYeeO7k4GAGiKdnqKSMbGy0lONt5M
      pU8HNQsl/6eoSHdR0RWw9Ez0ccR91wGASIrFFwIDAQABAoIBAGKgBl+CM5o5oGsZ
      lzPly2P1on1d0MDIL/7ui7wuZM9rI+hD1q02quIhuF02TfYJjBWEPgBSVQRIzIm1
      P2GRK6Ro3+Vo36SIWvA5XiueqjOAygJThuGPGTV8an4wcVl8jweJezCyikO0Wz2U
      W81Mj0KV1DY4yq6XeKOlaA7Zh/geoyWeLzuo42ibCCM/7uBNsyWFMk712z1KUHoc
      bcgRtUM8MeFQjjhGCAIv3k0LEeXL/g0IzmgxtYaDYbR4ymtRGefHXljQMr1uGFLh
      JWTnED1OPiSLfolSd/EJgm0VcEsD/3aCxPVmbF0OGB/pFRjaarbSJ9hIrVbI/l3w
      zVbSwyECgYEA8R1S6VzU1ED9lVywaRYklSdjtbZaBZh1WZtok3ALPY+k08quFwEx
      vEV2NPIPcpSlE+oGhdK70XEHyAQOC8b6UwKwHe4VKrL0jKvJsNU/WdWJinwYGLIy
      VZsq18A57mQJBpCkjwjw5qOjWkJQojsmQzXO7SHhOEyLHvG0VP3w1ccCgYEA4Z5D
      9rPyWYf4/MuMQg5k5B/ih68e77NV4EHbofBSXYBlhGrhrGVaCB1rUJPTPMGgYN6P
      qu9qB31gsXMd+v7mI6sHSLIQK/9UY7pILs+9PqjnLL7RvPSEyaUfgonUojK/WrD0
      VeUOc5/4ZUVDHnFxCvXUOKVDQ49+mAbDbulXVjECgYEAuhoAHM7iFtHy6I4aO4Iz
      ykwU0fRll1wNd5RUKziX9HQirLYLmQX69W5HxqXu9ml04OIJFtGI1id/8gnvLXfv
      TpMMjI1vGP33c3xEuJBfzV7cQl912dnwr9KMRuq/zBi6Pq711ND534r+UnRM+Grf
      JZEqni1AQMwTtVap8c/vS5ECgYEAss4+KK+WGvSTFK2we81ykgTfAA9+ohNrtK4d
      BWszq5yNV/No5LryLko6eYKeP6FonDzmeV8Cler8jcWg9gG7nHr369oKzQOu+tZw
      TIEhBx7PD3wvNuRGtJRjs43OcblsQ9DH46cD3Ajk0EWjGuZm43vN9BKti0aW2p9J
      lYXiTJECgYEAmF1/LS4tMgdNSPC+apCUFhi72p6EININccQSkmIMzBQOvQ1pDxub
      bqfxxS/4LHOnr0+n7KoPBCfvJ1VOvs9PEv9azU5qgLJvyzDB56CRBKU6lnyzGDF3
      665uRd3AnNVeT6FoVU8KkjFqw7gko1pIfHIF9pOyCaxwsOAyFS8h/KU=
      -----END RSA PRIVATE KEY-----
rancher:
  docker:
    tls: true
    tls_args:
    - --tlsverify
    - --tlscacert=/etc/docker/tls/ca.pem
    - --tlscert=/etc/docker/tls/server-cert.pem
    - --tlskey=/etc/docker/tls/server-key.pem
    - -H=0.0.0.0:2376'
        },
    },
}
