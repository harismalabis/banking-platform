output "eks_cluster_endpoint" {
  value = aws_eks_cluster.banking_platform.endpoint
}

output "eks_cluster_name" {
  value = aws_eks_cluster.banking_platform.name
}

output "node_group_names" {
  value = aws_eks_node_group.banking_platform_node_group.*.node_group_name
}

output "node_group_arns" {
  value = aws_eks_node_group.banking_platform_node_group.*.arn
}

output "vpc_id" {
  value = aws_vpc.banking_platform_vpc.id
}