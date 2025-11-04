#!/usr/bin/env python3
import aws_cdk as cdk
from aws_cdk_python_demo.aws_cdk_python_demo_stack import AwsCdkPythonDemoStack

app = cdk.App()

AwsCdkPythonDemoStack(
    app,
    "AwsCdkPythonDemoStack",
    env=cdk.Environment(
        account="466401257003",
        region="ap-south-1"
    ),
)

app.synth()

