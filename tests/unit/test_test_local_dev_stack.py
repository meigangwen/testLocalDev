import aws_cdk as core
import aws_cdk.assertions as assertions

from test_local_dev.test_local_dev_stack import TestLocalDevStack

# example tests. To run these tests, uncomment this file along with the example
# resource in test_local_dev/test_local_dev_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TestLocalDevStack(app, "test-local-dev")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
