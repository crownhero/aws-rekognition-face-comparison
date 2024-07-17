import json
import boto3

def lambda_handler(event, context):
    rekognition = boto3.client('rekognition')
    s3 = boto3.client('s3')

    # Get image keys from the request
    source_image_key = event['sourceImageKey']
    target_image_key = event['targetImageKey']

    # Bucket names
    source_bucket = 'uyu-kyc-documents'
    target_bucket = 'uyu-kyc-selfies'

    try:
        # Get source image from S3
        source_image = s3.get_object(Bucket=source_bucket, Key=source_image_key)['Body'].read()

        # Get target image from S3
        target_image = s3.get_object(Bucket=target_bucket, Key=target_image_key)['Body'].read()

        # Compare faces
        response = rekognition.compare_faces(
            SourceImage={'Bytes': source_image},
            TargetImage={'Bytes': target_image},
            SimilarityThreshold=70
        )

        if response['FaceMatches']:
            similarity = response['FaceMatches'][0]['Similarity']
            return {
                'statusCode': 200,
                'body': json.dumps({'match': True, 'similarity': similarity})
            }
        else:
            return {
                'statusCode': 200,
                'body': json.dumps({'match': False})
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

