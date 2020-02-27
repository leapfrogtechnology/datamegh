"""Base class to configure AWS"""
import boto3

from settings import AWS_CONFIG


def get_aws_client(client_name):
    """
    Method to get AWS client object
    :param client_name: name of the AWS client
    :return: AWS client
    """
    session = boto3.Session(**AWS_CONFIG)
    client = session.client(client_name)
    return client
