import os
import boto3
import pytest
import json
from moto import mock_s3
from datamegh.api.storage import s3


@pytest.fixture()
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "test_aws_access_key_id"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "test_aws_secret_access_key"


@pytest.fixture()
def s3_client(aws_credentials):
    BUCKET = "test_bucket"
    with mock_s3():
        s3_client = boto3.client("s3")
        s3_client.create_bucket(Bucket=BUCKET)
        yield s3_client


def test_upload(s3_client):
    # Arrange
    file_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = "{}/sample/test_file.json".format(file_dir)
    bucket_name = "test_bucket"
    s3_object_name = "test_file.json"
    with open(file_path) as file:
        test_data = json.load(file)
    # Act
    s3.upload(file_path, bucket_name, s3_object_name)
    s3_object = json.loads(
        s3_client.get_object(Bucket=bucket_name, Key="test_file.json")["Body"]
        .read()
        .decode("utf-8")
    )
    # Assert
    assert type(s3_object) == dict
    assert s3_object == test_data


def test_download(s3_client):
    # Arrange
    file_dir = os.path.dirname(os.path.abspath(__file__)) + "/sample/"
    bucket_name = "test_bucket"
    file_name = "test_file_download.json"
    file_body = json.dumps({"name": "John", "age": 30, "car": None})
    s3_object_name = "s3_test_file.json"
    s3_client.put_object(Bucket=bucket_name, Key=s3_object_name, Body=file_body)
    # Act
    s3.download(file_dir, file_name, bucket_name, s3_object_name)
    s3_object = json.loads(
        s3_client.get_object(Bucket=bucket_name, Key=s3_object_name)["Body"]
        .read()
        .decode("utf-8")
    )

    with open(file_dir + file_name) as file:
        test_data = json.load(file)

    # Assert
    assert type(test_data) == dict
    assert test_data == s3_object
