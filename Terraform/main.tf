provider "aws" {
    region=us-east-1
}

resource "aws_instance" "example" {
    instance_type = "m3.small"
    ami = "jbvieruchnreui"
    security_groups = "jcknehfkjxhebjf"
  
}

resource "aws_api_gateway_api_key" "example" {
  name = "example"
<<<<<<< Updated upstream
=======
  tags = {
    name: "Instance"
  }
}

resource "aws_security_group" "allow_tls" {
  name        = "allow_tls"
  description = "Allow TLS inbound traffic and all outbound traffic"
  vpc_id      = aws_vpc.main.id

  tags = {
    Name = "allow_tls"
  }
>>>>>>> Stashed changes
}
