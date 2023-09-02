# MainWebsite-API

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- api - Code for the Lambda function.
- events - Events that you can use to invoke the function.
- tests - Unit tests for the application code. 
- template.yaml - Template that defines the AWS resources.


## Build a local API and running tests

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community) *RECOMMENDED


To test functions:

You can either run functions locally and invoke them, which doesn't require building with Docker:

```bash
sam local invoke MainWebsiteFunction --event events/event.json
```

Or use the SAM CLI, which can emulate your application's API on port 3000.

```bash
sam build --use-container
sam local start-api
```

The SAM CLI installs dependencies defined in `api/requirements.txt`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

Now if you try to access any endpoint on the local address you hosted, you should get a result:

```bash
curl http://localhost:3000/
```

The SAM CLI reads the application template to determine the API's routes and the functions that they invoke.

```yaml
      Events:
        HelloWorld:
          Type: Api
          Properties:
            Path: /hello
            Method: get
```

## Tests

It is **highly recommended** you use good testing practices by using tests that you defined in the `tests` folder in this project. Use PIP to install the test dependencies and run tests.

```bash
pip install -r tests/requirements.txt --user

# unit test
python -m pytest tests/unit -v

# integration test, requiring deploying the stack first.
# First create the env variable AWS_SAM_STACK_NAME=MainWebsite-API
python -m pytest tests/integration -v
```

Although you should do this for testing, feel free to unit test your API with any other resource, such as [Postman](https://www.postman.com/downloads/), which is a highly popular tool for API testing. The integration testing is really a formality, because any issues with the CloudFormation will be obvious and will usually break on deployment, stopping your merge request. 

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for more info.
