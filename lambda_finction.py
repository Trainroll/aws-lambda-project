import json



def lambda_handler(event, context):

# Generate messagee from using key events 

    message = 'Hello {} {}! Keep being awesome!!!' .format(event['first_name'], event['last_name'])


## Print Message to Cloudwatch 

    print(message)


###  Return the response payload 
    return { 

        'message' : message

    }

#### Code Tested locally on my terminal before deployment 


if __name__ == "__main__":

	test_event= {
		'first_name' : 'Rul3',
		'last_name' : 'Doe'

    }
print(lambda_handler((test_event), None))  
