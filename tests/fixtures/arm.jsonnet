{
    compute: {
        provider: 'arm',
        auth: {
            client_id: '063D4853-67E5-49B3-B8A2-331C12655F74',
            client_secret: '170B8F37-B1F1-4884-9413-EC9106453FEF',
            tennant_id: '0CE9D36A-81B0-43A4-A7DF-0713CCA5CAA9',
            subscription_id: '27B895F1-FFC3-4D36-92D7-7491B8DFF1D2'
        },
        instance: {
                "resources": [
                {
                    "name": "pooty",
                    "type": "Microsoft.Compute/virtualMachines",
                    "apiVersion": "2017-03-30",
                    "location": "eastus",
                    "dependsOn": [
                        "Microsoft.Network/networkInterfaces/ranchero2355"
                    ],
                    "properties": {
                        "osProfile": {
                            "computerName": "pooty",
                            "adminUsername": "rancher",
                            "linuxConfiguration": {
                                "disablePasswordAuthentication": "true",
                                "ssh": {
                                    "publicKeys": [
                                        {
                                            "path": "/home/luser/.ssh/authorized_keys",
                                            "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAw2ZFm8wbNm5pxBk1C2WyIpB8bo81lWUtSyPe1ZiCX3F5N5wNpJr83ithmtpCbf5+8RpYN4oHXNva7Po1jXiXXbWno3eh9nkvalLGVLWV2xA3kXtpWMxPKtYGKju414JLKYG0myAwEl4+JB6LMRU1WxniUNXgWpsKa0SD5gurWV0CDgR/+L3IykG32inEGguGMsM/p7HiazOhbs+rJulUt8OoW8P6iR3Zc9AYwLKJ6lfjVM1Q9rQAGAJ+576tlWRKtP+olfCHnm1Vfww3AVTOdyfS03qlJ+oXtP63sVOLt1bnkb8i/LLREy5c2zG/+MGC4bcSUtyxo5klem/LOuMuBQ=="
                                        }
                                    ]
                                }
                            }
                        },
                        "hardwareProfile": {
                            "vmSize": "Standard_B1s"
                        },
                        "storageProfile": {
                            "imageReference": {
                                "publisher": "rancher",
                                "offer": "rancheros",
                                "sku": "os",
                                "version": "latest"
                            },
                            "osDisk": {
                                "createOption": "fromImage",
                                "managedDisk": {
                                    "storageAccountType": "Premium_LRS"
                                }
                            },
                            "dataDisks": []
                        },
                        "networkProfile": {
                            "networkInterfaces": [
                                {
                                    "id": "Microsoft.Network/networkInterfaces/ranchero2355"
                                }
                            ]
                        },
                        "diagnosticsProfile": {
                            "bootDiagnostics": {
                                "enabled": true,
                                "storageUri": "[reference(resourceId('continuum', 'Microsoft.Storage/storageAccounts', parameters('diagnosticsStorageAccountName')), '2015-06-15').primaryEndpoints['blob']]"
                            }
                        }
                    },
                    "plan": {
                        "name": "os",
                        "publisher": "rancher",
                        "product": "rancheros"
                    }
                },
                {
                    "name": "continuumvnet887",
                    "type": "Microsoft.Network/virtualNetworks",
                    "apiVersion": "2018-02-01",
                    "location": "eastus",
                    "properties": {
                        "addressSpace": {
                            "addressPrefixes": [
                                "10.0.0.0/24"
                            ]
                        },
                        "subnets": [
                            {
                                "name": "default",
                                "properties": {
                                    "addressPrefix": "10.0.0.0/24"
                                }
                            }
                        ]
                    }
                },
                {
                    "name": "ranchero2355",
                    "type": "Microsoft.Network/networkInterfaces",
                    "apiVersion": "2018-04-01",
                    "location": "eastus",
                    "dependsOn": [
                        "Microsoft.Network/virtualNetworks/continuumvnet887",
                        "Microsoft.Network/publicIpAddresses/ranchero2-ip",
                        "Microsoft.Network/networkSecurityGroups/ranchero2-nsg"
                    ],
                    "properties": {
                        "ipConfigurations": [
                            {
                                "name": "ipconfig1",
                                "properties": {
                                    "subnet": {
                                        "id": "[variables('subnetRef')]"
                                    },
                                    "privateIPAllocationMethod": "Dynamic",
                                    "publicIpAddress": {
                                        "id": "[resourceId('continuum','Microsoft.Network/publicIpAddresses', parameters('publicIpAddressName'))]"
                                    }
                                }
                            }
                        ],
                        "networkSecurityGroup": {
                            "id": "[resourceId('continuum', 'Microsoft.Network/networkSecurityGroups', parameters('networkSecurityGroupName'))]"
                        }
                    }
                },
                {
                    "name": "[parameters('publicIpAddressName')]",
                    "type": "Microsoft.Network/publicIpAddresses",
                    "apiVersion": "2017-08-01",
                    "location": "[parameters('location')]",
                    "properties": {
                        "publicIpAllocationMethod": "[parameters('publicIpAddressType')]"
                    },
                    "sku": {
                        "name": "[parameters('publicIpAddressSku')]"
                    }
                },
                {
                    "name": "[parameters('networkSecurityGroupName')]",
                    "type": "Microsoft.Network/networkSecurityGroups",
                    "apiVersion": "2018-01-01",
                    "location": "[parameters('location')]",
                    "properties": {
                        "securityRules": [
                            {
                                "name": "SSH",
                                "properties": {
                                    "priority": 1010,
                                    "protocol": "TCP",
                                    "access": "Allow",
                                    "direction": "Inbound",
                                    "sourceApplicationSecurityGroups": [],
                                    "destinationApplicationSecurityGroups": [],
                                    "sourceAddressPrefix": "*",
                                    "sourcePortRange": "*",
                                    "destinationAddressPrefix": "*",
                                    "destinationPortRange": "22"
                                }
                            },
                            {
                                "name": "Docker_TLS",
                                "properties": {
                                    "priority": 1020,
                                    "protocol": "TCP",
                                    "access": "Allow",
                                    "direction": "Inbound",
                                    "sourceApplicationSecurityGroups": [],
                                    "destinationApplicationSecurityGroups": [],
                                    "sourceAddressPrefix": "*",
                                    "sourcePortRange": "*",
                                    "destinationAddressPrefix": "*",
                                    "destinationPortRange": "2376"
                                }
                            },
                            {
                                "name": "Rancher_IPsec",
                                "properties": {
                                    "priority": 1030,
                                    "protocol": "UDP",
                                    "access": "Allow",
                                    "direction": "Inbound",
                                    "sourceApplicationSecurityGroups": [],
                                    "destinationApplicationSecurityGroups": [],
                                    "sourceAddressPrefix": "*",
                                    "sourcePortRange": "*",
                                    "destinationAddressPrefix": "*",
                                    "destinationPortRange": "4500"
                                }
                            }
                        ]
                    }
                }
            ],
            "outputs": {
                "adminUsername": {
                    "type": "string",
                    "value": "[parameters('adminUsername')]"
                }
            }
        }
    }
}