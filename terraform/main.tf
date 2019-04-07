terraform {
  backend "s3" { }
}

provider "aws" {
  access_key = "${var.access_key}"
  secret_key = "${var.secret_key}"
  region     = "${var.region}"
}

locals {
  item_suffix = "${join("-", list(var.user, var.project, var.environment))}"
}

resource "aws_ecr_repository" "ecr_azure_agent_repository" {
  name = "${local.item_suffix}/azure_agent"
}

