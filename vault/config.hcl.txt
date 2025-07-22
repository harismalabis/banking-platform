# Vault Configuration for Banking Platform

# This file configures the Vault server for managing secrets in the banking platform.

# Enable the KV secrets engine at the path "secret/"
path "secret/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}

# Define policies for different microservices
# Accounts service policy
path "secret/accounts/*" {
  capabilities = ["create", "read", "update", "delete"]
}

# Payments service policy
path "secret/payments/*" {
  capabilities = ["create", "read", "update", "delete"]
}

# Users service policy
path "secret/users/*" {
  capabilities = ["create", "read", "update", "delete"]
}

# Transactions service policy
path "secret/transactions/*" {
  capabilities = ["create", "read", "update", "delete"]
}

# Notifications service policy
path "secret/notifications/*" {
  capabilities = ["create", "read", "update", "delete"]
}

# Gateway service policy
path "secret/gateway/*" {
  capabilities = ["create", "read", "update", "delete"]
}

# Enable the AppRole authentication method
auth "approle" {
  type = "approle"
}

# Define the AppRole for the banking application
role "banking-app" {
  policies = ["default", "accounts", "payments", "users", "transactions", "notifications", "gateway"]
}