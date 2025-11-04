from aws_cdk import (
    Stack,
    aws_ec2 as ec2
)
from constructs import Construct

class AwsCdkPythonDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a VPC
        vpc = ec2.Vpc(self, "DemoVPC",
                      max_azs=2,
                      nat_gateways=1,
                      cidr="10.0.0.0/16")

        # Create a Security Group
        sg = ec2.SecurityGroup(self, "DemoSG",
                               vpc=vpc,
                               description="Allow SSH and HTTP",
                               allow_all_outbound=True)

        sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(22), "Allow SSH")
        sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(80), "Allow HTTP")

        # Output VPC ID
        self.vpc_id = vpc.vpc_id

