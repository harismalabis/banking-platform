# Helm Charts for Banking Platform

This directory contains the Helm charts used for deploying the banking application on AWS EKS.

## Overview

Helm is a package manager for Kubernetes that allows you to define, install, and upgrade even the most complex Kubernetes applications. The charts in this directory are designed to simplify the deployment of the banking platform's microservices.

## Structure

The Helm charts are located in the `charts` directory. Each microservice has its own chart, which includes:

- **Chart.yaml**: Contains metadata about the Helm chart.
- **values.yaml**: Defines the default configuration values for the chart.
- **templates/**: Contains the Kubernetes resource templates that will be rendered into manifests.

## Usage

To install the Helm charts, follow these steps:

1. Ensure you have Helm installed on your local machine.
2. Navigate to the `charts` directory.
3. Use the following command to install a chart:

   ```
   helm install <release-name> ./<chart-name>
   ```

   Replace `<release-name>` with a name for your release and `<chart-name>` with the name of the chart you want to install (e.g., `banking-app`).

4. To customize the deployment, you can modify the `values.yaml` file or pass custom values using the `--set` flag.

## Updating

To update an existing release, use the following command:

```
helm upgrade <release-name> ./<chart-name>
```

## Uninstalling

To uninstall a release, run:

```
helm uninstall <release-name>
```

## Monitoring

After deployment, you can monitor the application using Prometheus and Grafana, which are configured in the monitoring directory of the project.

For further details on each microservice and its specific configurations, refer to the respective chart directories.