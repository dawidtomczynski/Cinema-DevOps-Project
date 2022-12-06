provider "aws" {
  region = "eu-west-3"
}

terraform {

  backend "s3" {
    bucket = "dawid-cinema"
    key    = "eks/terraform.tfstate"
    region = "eu-west-3"
  }
  
  required_providers {
    kubectl = {
      source  = "gavinbunney/kubectl"
      version = ">= 1.14.0"
    }
    helm = {
      source  = "hashicorp/helm"
      version = ">= 2.6.0"
    }
  }

  required_version = "~> 1.0"
}
