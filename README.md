# AWS Lambda Greeting Function

A Python AWS Lambda function that accepts `first_name` and `last_name`, generates a greeting, logs it to CloudWatch, and returns the message.

## Function

```python
def lambda_handler(event, context):

    message = 'Hello {} {}! Keep being awesome!'.format(
        event['first_name'],
        event['last_name']
    )

    print(message)

    return {
        'message': message
    }
```

## Test Event

```json
{
    "first_name": "Rul3",
    "last_name": "Doe"
}
```

## Local Testing

The function was also tested locally using:

```python
if __name__ == "__main__":
    test_event = {
        "first_name": "Rul3",
        "last_name": "Doe"
    }

    print(lambda_handler(test_event, None))
```

Run with:

```bash
python3 lambda_function.py
```

Output:

```text
Hello Rul3 Doe! Keep being awesome!
```

## AWS

* **Lambda** — function execution
* **CloudWatch** — execution logs
* **IAM** — Lambda execution role

## Skills

`Python` `AWS Lambda` `CloudWatch` `IAM` `JSON` `Git`

<<<<<<< HEAD
- Creating Lambda functions
- Lambda execution roles
- Testing Lambda functions
- CloudWatch logging
- Serverless architecture
=======
>>>>>>>
