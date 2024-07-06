terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "us-east-1"
}

resource "aws_instance" "app_server" {
  ami           = "ami-06c68f701d8090592"
  instance_type = "t2.micro"

  tags = {
    Name = "ExampleAppServerInstance"
  }
}

#resource "aws_s3_bucket" "my_bucket" {
#  bucket = "mi-bucket-unico"  # Nombre único para tu bucket de S3
#  acl    = "private"  # Control de acceso predeterminado (opcional)
  
#  tags = {
#    Name        = "mi-bucket-unico"
#    Environment = "Dev"
#  }
#}