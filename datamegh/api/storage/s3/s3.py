"""Class to access AWS S3 service extends base class AWS"""

from boto3.s3.transfer import S3Transfer
from boto3.exceptions import S3UploadFailedError
from botocore.exceptions import ClientError

from datamegh.commons.aws import get_aws_client
from datamegh.util.logging import get_logger

logger = get_logger("storage:s3")


def upload_to_s3(file_path, bucket_name, s3_object_name):
    """
    Method to upload file to s3 bucket
    :param file_path: file path
    :param bucket_name: s3 bucket name
    :param s3_object_name: name of file to be in s3 bucket
    """
    s3_client = get_aws_client("s3")
    transfer = S3Transfer(s3_client)
    # Upload the file to S3
    try:
        transfer.upload_file(file_path, bucket_name, s3_object_name)
    except FileNotFoundError:
        logger.error("File: {} was not found".format(file_path))
    except (ClientError, S3UploadFailedError) as se:
        logger.error(se)
    else:
        logger.info(
            "File : {} uploaded to {} bucket S3 successfully.".format(
                file_path, bucket_name
            )
        )


def download_from_s3(file_dir, file_name, bucket_name, s3_object_name):
    """
    Method to download file from s3
    :param file_dir: destination file directory eg:/home/destination/
    :param file_name: name of the file to be
    :param bucket_name: s3 bucket name
    :param s3_object_name: s3 file object name
    """
    file_path = file_dir + file_name
    s3_client = get_aws_client("s3")
    try:
        s3_client.download_file(bucket_name, s3_object_name, file_path)
    except ClientError as ce:
        logger.error(ce)
    else:
        logger.info(
            "File: {} downloaded successfully in the dir {}.".format(
                file_name, file_dir
            )
        )
