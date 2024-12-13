import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    bucket_name = 'test-bucket-dataobrii'
    object_key = '0028~(02-15-2018)~processed.txt'
    download_path = '/tmp/example.txt'

    try:
        s3.download_file(bucket_name, object_key, download_path)
        logger.info(f"File '{object_key}' downloaded to '{download_path}'")

        with open(download_path, 'r') as file:
            content = file.read()
            logger.info("File content:")
            logger.info(content)

        return {"status": "success", "content": content}

    except Exception as e:
        logger.error(f"Error: {e}")
        return {"status": "error", "message": str(e)}
