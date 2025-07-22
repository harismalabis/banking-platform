# Banking Platform

## Overview
This project is a microservices-based banking platform designed to run on AWS EKS (Elastic Kubernetes Service). It consists of multiple microservices that handle various banking functionalities, including accounts, payments, users, transactions, notifications, and a gateway service.

## Architecture
The architecture of the banking platform is based on microservices, allowing for scalability and maintainability. Each microservice is containerized using Docker and deployed on EKS. The platform also includes a CI/CD pipeline for automated deployment and monitoring solutions for observability.

## Technologies Used
- **Infrastructure**: Terraform, Helm
- **CI/CD**: Jenkins
- **Containerization**: Docker
- **Orchestration**: AWS EKS
- **Secrets Management**: Vault
- **Monitoring**: Prometheus, Grafana

## Getting Started

### Prerequisites
- AWS account
- Terraform installed
- Helm installed
- Docker installed
- Jenkins installed
- Vault installed

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd banking-platform
   ```

2. **Infrastructure Setup**
   - Navigate to the `infrastructure/terraform` directory.
   - Update the `variables.tf` file with your desired configuration.
   - Run the following commands to deploy the infrastructure:
     ```bash
     terraform init
     terraform apply
     ```

3. **Deploying Microservices**
   - Navigate to the `infrastructure/helm/charts/banking-app` directory.
   - Update the `values.yaml` file as needed.
   - Deploy the Helm chart:
     ```bash
     helm install banking-app .
     ```

4. **CI/CD Pipeline**
   - Configure Jenkins with the provided `Jenkinsfile` located in `infrastructure/jenkins`.
   - Set up the necessary credentials and environment variables in Jenkins.

5. **Monitoring Setup**
   - Configure Prometheus and Grafana using the provided configuration files in the `monitoring` directory.

## Monitoring
The platform includes a full monitoring stack with Prometheus for metrics collection and Grafana for visualization. The Grafana dashboard can be customized using the JSON configuration provided in the `monitoring/grafana/dashboards` directory.

## Conclusion
This banking platform provides a robust solution for managing banking operations with a focus on microservices architecture, scalability, and observability. For further details, refer to the documentation in the respective directories.