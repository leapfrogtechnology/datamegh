"""Base class to configure AWS"""
import boto3

from settings import AWS_CONFIG


class AWS:
    def __get_session(self):
        """
        Private method to generate AWS session
        :return: session
        """
        session = boto3.Session(**AWS_CONFIG)
        return session

    def get_client(self, client_name):
        """
        Method to get AWS client object
        :param client_name: name of the AWS client
        :return: AWS client
        """
        client = self.__get_session().client(client_name)
        return client
