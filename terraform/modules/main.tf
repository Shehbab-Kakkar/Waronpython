provider "aws" {
   region = "us-west-2"
}
resource "aws_vpc" "module_vpc" {
  cidr_block = var.vpc_cidr_block
}
resource "aws_subnet" "public_subnet" {
  cidr_block = ""
  vpc_id = "$aws_vpc.module_vpc.id"
}

