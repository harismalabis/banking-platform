# Microservices-Based Banking Platform on AWS EKS

🎯 Ideal for DevOps Interviews and Resume Showcases  
📂 Real-world microservices architecture with clean folder structure  
☁️ Deployed on AWS using EKS, Terraform, and CI/CD pipelines  
🔗 GitHub Repository: [github.com/harismalabis/banking-platform](https://github.com/harismalabis/banking-platform)

---

👨‍💻 Project Author: Haris Shaikh  
📌 Designed for demonstrating end-to-end DevOps lifecycle using industry-grade tools.


🏦 Microservices-Based Banking Platform on Kubernetes (EKS)
A real-world DevOps project built using Python Flask microservices deployed on AWS EKS with complete CI/CD, observability, and infrastructure automation using Terraform, Jenkins, Docker, and Prometheus-Grafana.

🚀 Overview
This project demonstrates a fully containerized microservices-based banking application with modular services like:

Accounts Service – Manages user accounts

Transactions Service – Handles fund transfers

Notifications Service – Sends real-time alerts

All services are:

Built using Python Flask

Containerized with Multi-Stage Dockerfiles

Deployed using Terraform-managed EKS

Managed through Jenkins CI/CD pipelines

Monitored with Prometheus & Grafana

🔧 Tools & Technologies Used
Category	Tools Used
🛠️ Infrastructure	AWS EKS, Terraform, VPC, IAM, EC2, S3
🐳 Containers	Docker, Docker Compose, Multi-stage Dockerfiles
☸️ Orchestration	Kubernetes (EKS), kubectl, EBS CSI Driver
⚙️ CI/CD	Jenkins, GitHub Webhooks, Jenkinsfile pipelines
📈 Monitoring	Prometheus, Grafana, Node Exporter
🔐 Security	AWS IAM Roles, Security Groups, Secrets

🧱 Architecture Diagram

📦 Microservices Breakdown
Each microservice is isolated in its own directory:

1. 🧾 Accounts Service
Manages customer details and account registration

Built with Flask + MongoDB

REST APIs for user creation, retrieval

2. 💸 Transactions Service
Handles debit/credit operations

Ensures idempotent transfer processing

Uses internal service communication

3. 🔔 Notification Service
Sends SMS/email alerts on transactions

Mocked with Flask background jobs

🐳 Docker Setup
Each microservice uses a Multi-Stage Dockerfile to optimize image size:

Dockerfile
Copy
Edit
# Stage 1 - Builder
FROM python:3.9-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Stage 2 - Runtime
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.9 /usr/local/lib/python3.9
COPY . .
CMD ["python", "app.py"]
To build and run locally:

bash
Copy
Edit
docker build -t accounts-service ./services/accounts
docker run -p 5000:5000 accounts-service
☸️ Kubernetes on AWS EKS
Cluster provisioning via Terraform

Each service has its own:

Deployment YAML

Service YAML

ConfigMap/Secret

EBS CSI Driver integrated for Persistent Volume Claims (PVCs)

⚙️ CI/CD Pipeline (Jenkins)
✅ Jenkins pipeline triggered on GitHub push

🐳 Docker image built and pushed to Docker Hub

☸️ Kubectl deploys updated image to EKS cluster

Jenkinsfile Highlights:

groovy
Copy
Edit
pipeline {
  agent any
  stages {
    stage('Build Docker Image') {
      steps {
        sh 'docker build -t harismalabis/accounts-service ./services/accounts'
      }
    }
    stage('Push to Docker Hub') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', ...)]) {
          sh 'docker push harismalabis/accounts-service'
        }
      }
    }
    stage('Deploy to EKS') {
      steps {
        sh 'kubectl apply -f k8s/accounts-deployment.yaml'
      }
    }
  }
}
📊 Monitoring & Observability
Prometheus + Grafana deployed using Helm Charts.

Metrics Tracked:
CPU, Memory (Node Exporter)

App-level logs via stdout

Custom HTTP metrics endpoints (optional)

Dashboards include:

Live Pod health

Resource usage

Service uptime

📄 Resume Description
✅ Project Title:
End-to-End Deployment of a Microservices Banking App on AWS EKS with CI/CD & Monitoring

📘 Description:
Designed and deployed a production-grade microservices banking platform using Python Flask, Docker, and Kubernetes (EKS). Automated deployments with Jenkins pipelines and implemented full-stack monitoring with Prometheus and Grafana.

🔑 Key Responsibilities:
Created AWS infrastructure using Terraform (VPC, EKS, IAM, Security Groups)

Built multi-stage Docker images for Python Flask services

Designed Jenkins CI/CD pipelines for automated testing and deployment

Deployed microservices on EKS with high availability

Set up Prometheus and Grafana dashboards for observability

🏆 Achievements:
Reduced Docker image size by 70% using multi-stage builds

Achieved zero-downtime deployments via Kubernetes Rolling Updates

Real-time monitoring of production workloads using Prometheus + Grafana

🧪 How to Run Locally
bash
Copy
Edit
git clone https://github.com/harismalabis/banking-platform.git
cd banking-platform

# Using Docker Compose
docker-compose up --build

📂 Folder Structure
banking-platform/
├── 📂 infrastructure/
│ ├── 📁 terraform/ # 🔧 AWS EKS, VPC, IAM provisioning
│ └── 📁 jenkins/ # ⚙️ CI/CD pipelines & Jenkinsfiles
│
├── 📂 services/ # 🧩 All Python Flask Microservices
│ ├── 📁 accounts/ # 💼 Account Service (Dockerized)
│ ├── 📁 user/ # 👤 User Service
│ ├── 📁 payment/ # 💳 Payment Service
│ ├── 📁 transaction/ # 🔁 Transaction Service
│ ├── 📁 notification/ # 🔔 Notification Service
│ └── 📁 gateway/ # 🌐 API Gateway (Ingress Controller)
│
├── 📄 docker-compose.yml # 🐳 Local dev & testing orchestration
├── 📄 .env # 🔐 Environment Variables
└── 📄 README.md # 📘 Project Documentation

📸 Screenshots













## 🔗 Connect with Me

I'm open to discussing DevOps roles, cloud projects, or strategic collaborations.

- 📧 Email: harisshaikh11112@gmail.com  
- 💼 LinkedIn: [linkedin.com/in/harisshaikh11112](https://www.linkedin.com/in/harisshaikh11112)  
- 💻 GitHub: [github.com/harismalabis](https://github.com/harismalabis)
