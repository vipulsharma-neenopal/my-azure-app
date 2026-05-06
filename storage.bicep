resource stg 'Microsoft.Storage/storageAccounts@2022-09-01' = {
  name: 'mystoragevipul12345'
  location: resourceGroup().location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {}
}