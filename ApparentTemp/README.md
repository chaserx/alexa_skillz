# Apparent Temp

## Motivation

My lovely wife would rather know what the heat index or wind chill is rather than the actual temperature outside. That's fair. The Accuweather service calls this Real Feel&reg;, however, here we're not using that service. We're using the venerable Dark Sky service for simplicity and amenable terms of use. 

## Requirements 

You'll need a plain text API string as a parameter in AWS System Manger in us-east-1 (or wherever your lambda runs that's also compatible with Alexa) named 'darkskyAPIKey'. 

The AWS CLI invocation for that is something like the following:

`aws ssm set-parameter --name darkskyAPIKey --value KEY --region us-east-1`

There are other ways to store this key, but this will work for now. 

## Deployment

Using the Serverless framework

`serverless deploy`

## Serverless Plugins

Using the `serverless-python-requirements` plugin to handle the installation and Linux compilation of required Python modules (see requirements.txt) namely the Requests library. You'll need to have Docker for Mac installed and running. 

`serverless plugin install --name serverless-python-requirements`

## References

[Managing secrets, API keys and more with Serverless](https://serverless.com/blog/serverless-secrets-api-keys/)

[You should use SSM Parameter Store over Lambda env variables](https://hackernoon.com/you-should-use-ssm-parameter-store-over-lambda-env-variables-5197fc6ea45b)

[How to make an Alexa Skill with Python](https://medium.com/@mr_rigden/how-to-make-an-alexa-skill-with-python-cb8a6a6c4d85)

[How to Handle your Python packaging in Lambda with Serverless plugins](https://serverless.com/blog/serverless-python-packaging/)

[Use the Skill Builder (Beta) to Define Intents, Slots, and Dialogs](https://developer.amazon.com/docs/custom-skills/use-the-skill-builder-beta-to-define-intents-slots-and-dialogs.html#launch-ux)

## Acknowledgements 

[Powered by Dark Sky](https://darksky.net/poweredby/)
