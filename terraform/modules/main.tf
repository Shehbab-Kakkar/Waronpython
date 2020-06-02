provider "aws" {
   region = "us-west-2"
}
resource "aws_vpc" "module_vpc" {
  cidr_block = ""
}
