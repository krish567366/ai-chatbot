terraform {
	required_providers {
		aws = {
			source  = "hashicorp/aws"
			version = "~> 5.50"
		}
	}
	required_version = ">= 1.6.0"
}

provider "aws" {
	region = var.region
}

module "vpc" {
	source  = "terraform-aws-modules/vpc/aws"
	version = "5.7.1"
	name = "ai-calling-vpc"
	cidr = "10.0.0.0/16"
	azs  = ["${var.region}a","${var.region}b","${var.region}c"]
	public_subnets  = ["10.0.1.0/24","10.0.2.0/24","10.0.3.0/24"]
	private_subnets = ["10.0.11.0/24","10.0.12.0/24","10.0.13.0/24"]
}

resource "aws_db_subnet_group" "main" {
	name       = "ai-calling-db-subnets"
	subnet_ids = module.vpc.private_subnets
}

resource "aws_db_instance" "postgres" {
	identifier              = "ai-calling-postgres"
	engine                  = "postgres"
	engine_version          = "15.6"
	instance_class          = "db.t3.medium"
	allocated_storage       = 50
	username                = "app"
	password                = var.db_password
	db_subnet_group_name    = aws_db_subnet_group.main.name
	vpc_security_group_ids  = [module.vpc.default_security_group_id]
	skip_final_snapshot     = true
	publicly_accessible     = false
}