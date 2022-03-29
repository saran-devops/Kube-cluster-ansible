variable "ingressrules" {
  type    = list(number)
  default = [80, 443, 22]
}

variable "vpc_id" {
  type    = string
  default = "vpc-bf097ed4"
}

