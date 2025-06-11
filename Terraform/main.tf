provider "aws" {
    region=us-east-1
}

resource "aws_instance" "example" {
    instance_type = "m3.small"
    ami = "jbvieruchnreui"
    security_groups = "jcknehfkjxhebjf"
  
}