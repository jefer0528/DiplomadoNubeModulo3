import boto3

#crear cliente para dynamo
dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')

tabla = dynamodb.Table('tabla-Jeffersson-Rodriguez')

#leer un elemento de la tabla
response = tabla.get_item(Key={'ID':'1'})

print(response['Item'])

#leer todos los elementos de la tabla
response = tabla.scan()

print(response['Items'])

#insertar nuevo registro
New = {
    "ID":"3",
    "ciudad":"Cali",
    "nombre":"Mariangel"
}

#inserta el nuevo registro en la tabla en aws
tabla.put_item(Item=New)


response = tabla.get_item(Key={'ID':'3'})

print(response['Item'])

New = {
    "ID":"3",
    "Tel":"12345678888",
    "ciudad":"Cali",
    "nombre":"Mariangel"
}

#inserta el nuevo registro en la tabla en aws
tabla.put_item(Item=New)



response = tabla.update_item(
    Key={
        'ID': '3'  
    },
    UpdateExpression='SET Tel = :val1',  # Expresión de actualización
    ExpressionAttributeValues={
        ':val1': '348888'  # Nuevo valor para atributo2
    }
)

response = tabla.get_item(Key={'ID':'3'})

print(response['Item'])

