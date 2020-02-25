"""Class to access AWS S3 service extends base class AWS"""

from boto3.s3.transfer import S3Transfer

from datamegh.commons.aws import AWS
from datamegh.util.logging import get_logger


class S3(AWS):
    def __init__(self):
        self.logger = get_logger("db")

    def upload_to_s3(self, file_path, bucket_name, file_name):
        """
        Method to upload file to s3 bucket
        :param file_path: file path
        :param bucket_name: s3 bucket name
        :param file_name: name of file to be in s3 bucket
        """
        s3_client = self.get_client("s3")
        transfer = S3Transfer(s3_client)
        # Upload the file to S3
        transfer.upload_file(file_path, bucket_name, file_name)
        self.logger.info(
            "File : {} uploaded to {} bucket S3 successfully.".format(
                file_path, bucket_name
            )
        )

    def download_from_s3(self):
        # Todo
        pass
