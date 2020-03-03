""" AWS base utility. """
import boto3
from botocore import client

from datamegh import config


def get_aws_client(client_name: str):
    """
    Get a new AWS client instance.

    :param client_name: name of the AWS client
    :return: AWS client
    """
    session = boto3.Session(**config["aws"])
    client = session.client(client_name)

    return client
