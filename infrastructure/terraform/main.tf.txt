provider "aws" {
  region = var.region
}

resource "aws_vpc" "banking_vpc" {
  cidr_block = var.vpc_cidr
  enable_dns_support = true
  enable_dns_hostnames = true
  tags = {
    Name = "banking-vpc"
  }
}

resource "aws_eks_cluster" "banking_cluster" {
  name     = var.cluster_name
  role_arn = aws_iam_role.eks_role.arn
  vpc_config {
    subnet_ids = aws_subnet.banking_subnet.*.id
  }
  depends_on = [aws_iam_role_policy_attachment.eks_policy]
}

resource "aws_iam_role" "eks_role" {
  name = "eks-role"
  assume_role_policy = data.aws_iam_policy_document.eks_assume_role_policy.json
}

data "aws_iam_policy_document" "eks_assume_role_policy" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["eks.amazonaws.com"]
    }
  }
}

resource "aws_subnet" "banking_subnet" {
  count                   = var.subnet_count
  vpc_id                  = aws_vpc.banking_vpc.id
  cidr_block              = element(var.subnet_cidrs, count.index)
  availability_zone      = element(var.availability_zones, count.index)
  map_public_ip_on_launch = true
  tags = {
    Name = "banking-subnet-${count.index}"
  }
}

resource "aws_eks_node_group" "banking_node_group" {
  cluster_name    = aws_eks_cluster.banking_cluster.name
  node_group_name = "${var.cluster_name}-node-group"
  node_role_arn   = aws_iam_role.node_role.arn
  subnet_ids      = aws_subnet.banking_subnet.*.id
  scaling_config {
    desired_size = var.desired_capacity
    max_size     = var.max_size
    min_size     = var.min_size
  }
}

resource "aws_iam_role" "node_role" {
  name = "node-role"
  assume_role_policy = data.aws_iam_policy_document.node_assume_role_policy.json
}

data "aws_iam_policy_document" "node_assume_role_policy" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["ec2.amazonaws.com"]
    }
  }
}

output "cluster_endpoint" {
  value = aws_eks_cluster.banking_cluster.endpoint
}

output "cluster_name" {
  value = aws_eks_cluster.banking_cluster.name
}

output "node_group_id" {
  value = aws_eks_node_group.banking_node_group.id
}