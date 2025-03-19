provider "aws" {
    region = "us-east-1"
}

# 1. Create a VPC (Mother Network)
resource "aws_vpc" "vpc_1" {
    cidr_block = "14.0.0.0/16"

    tags = {
      Name = "Mother Netwk"
    }
}

# 2. Create an Internet Gateway
resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.vpc_1.id
}

# 3. Create a custom Route Table
resource "aws_route_table" "main-route" {
  vpc_id = aws_vpc.vpc_1.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }

  route {
    ipv6_cidr_block        = "::/0"
    egress_only_gateway_id = aws_internet_gateway.gw.id
  }

  tags = {
    Name = "main-route"
  }
}

# 4. Create a Subnet
resource "aws_subnet" "subnet_1" {
  vpc_id     = aws_vpc.vpc_1.id
  cidr_block = "14.0.1.0/24"
  availability_zone = "us-east-1a"

  tags = {
    Name = "Subnet_1"
  }
}

# 5. Associate Subnet with route Table
resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.subnet_1.id
  route_table_id = aws_route_table.main-route.id
}

# 6. Create Security Group to allow port 22, 80, 443
resource "aws_security_group" "allow_web" {
  name        = "allow_web_traffic"
  description = "Allow web inbound traffic"
  vpc_id      = aws_vpc.vpc_1.id

  ingress {
    description = "HTTPS"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "allow_web"
  }
}

# 7. Create a Network Interface
resource "aws_network_interface" "web-server-NIC" {
  subnet_id       = aws_subnet.subnet_1.id
  private_ips     = ["14.0.1.50"]
  security_groups = [aws_security_group.allow_web.id]

  # attachment {
  #   instance     = aws_instance.test.id
  #   device_index = 1
  # }
}

# 8. Attach elastic IP to NIC in step 7
resource "aws_eip" "one" {
  # vpc                       = true
  network_interface         = aws_network_interface.web-server-NIC.id
  associate_with_private_ip = "14.0.1.50"
  depends_on = [aws_internet_gateway.gw]
}

# 9. Create Ubuntu Server and Install/enable Apache2
resource "aws_instance" "server_1" {
    ami           = "ami-04b4f1a9cf54c11d0"
    instance_type = "t2.micro"
    availability_zone = "us-east-1a"
    key_name = "main-KP"

    network_interface {
      network_interface_id = aws_network_interface.web-server-NIC.id
      device_index = 0
    }

    tags = {
        Name = "ubuntu instance"
    }

    user_data = <<EOF
                #!/bin/bash
                sudo apt update -y
                sudo apt install apache2 -y
                sudo systemctl start apache2
                sudo bash -c 'echo your first web server > /var/www/html/index.html'
                EOF
}


# variable "xyx" {
#   type = string
# }

# module "vpc_module" {
  
# }