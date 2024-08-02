from aws_cdk import (
    Stack,
)
from aws_cdk import (
    aws_apigateway as apigateway,
)
from aws_cdk import (
    aws_lambda as _lambda,
)
from constructs import Construct


class InfraStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        fastapi_lambda = _lambda.DockerImageFunction(
            self,
            "FastAPILambda",
            code=_lambda.DockerImageCode.from_image_asset(
                "../app"
            ),
        )

        api = apigateway.LambdaRestApi(
            self, "FastAPIEndpoint", handler=fastapi_lambda, proxy=True
        )
