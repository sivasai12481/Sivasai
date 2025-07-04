provider "aws" {
    region=us-east-1
}

resource "aws_instance" "example" {
    instance_type = "m3.small"
    ami = "jbvieruchnreui"
    security_groups = "jcknehfkjxfrcdfcdhebjf"
    tags = {
      name: "ec2-instance"
      owner: "OPF-TEAM"
      release: "25.36.STD0.RC1"
      previousrelease: "24.50.STD0.RC1"
    }
  
}

resource "aws_api_gateway_api_key" "example" {
  name = "example"
  tags = {
    name: "Instance"
    team: "OPF-Team"
    release: "25.36.STD0.RC1"
    previousrelease: "24.50.STD0.RC1"
  }
}

resource "aws_security_group" "allow_tls" {
  name        = "allow_tls"
  description = "Allow TLS inbound traffic and all outbound traffic"
  vpc_id      = aws_vpc.main.id

  tags = {
    Name = "allow_tls"
  }
}


#just for a comment
