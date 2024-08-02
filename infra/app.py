#!/usr/bin/env python3
import aws_cdk as cdk

from infra.infra_stack import InfraStack

app = cdk.App()
InfraStack(
    app,
    "InfraStack",
    env=cdk.Environment(account="123456789012", region="us-east-1"),
)

app.synth()
