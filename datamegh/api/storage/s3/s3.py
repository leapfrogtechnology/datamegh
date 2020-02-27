"""Class to access AWS S3 service extends base class AWS"""

from boto3.s3.transfer import S3Transfer
from boto3.exceptions import S3UploadFailedError
from botocore.exceptions import ClientError

from datamegh.commons.aws import AWS
from datamegh.util.logging import get_logger


class S3(AWS):
    def __init__(self):
        self.logger = get_logger("db")
        self.client = self.get_client("s3")

    def upload_to_s3(self, file_path, bucket_name, s3_object_name):
        """
        Method to upload file to s3 bucket
        :param file_path: file path
        :param bucket_name: s3 bucket name
        :param s3_object_name: name of file to be in s3 bucket
        """
        transfer = S3Transfer(self.client)
        # Upload the file to S3
        try:
            transfer.upload_file(file_path, bucket_name, s3_object_name)
        except FileNotFoundError:
            self.logger.error("File: {} was not found".format(file_path))
        except (ClientError, S3UploadFailedError) as se:
            self.logger.error(se)
        else:
            self.logger.info(
                "File : {} uploaded to {} bucket S3 successfully.".format(
                    file_path, bucket_name
                )
            )

    def download_from_s3(self, file_dir, file_name, bucket_name, s3_object_name):
        """
        Method to download file from s3
        :param file_dir: destination file directory eg:/home/destination/
        :param file_name: name of the file to be
        :param bucket_name: s3 bucket name
        :param s3_object_name: s3 file object name
        """
        file_path = file_dir + file_name
        try:
            self.client.download_file(bucket_name, s3_object_name, file_path)
        except ClientError as ce:
            self.logger.error(ce)
        else:
            self.logger.info(
                "File: {} downloaded successfully in the dir {}.".format(
                    file_name, file_dir
                )
            )
