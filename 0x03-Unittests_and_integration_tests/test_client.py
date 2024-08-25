#!/usr/bin/env python3
""" Parameterized and patch as deco """

from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
import json
import unittest
from unittest.mock import patch, PropertyMock, Mock


class TestGithubOrgClient(unittest.TestCase):
    """ Class for Testing GHO Client """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mock_dt):
        """ Test that GHO.org returns the correct value """
        test = GithubOrgClient(input)
        test.org()
        mock_dt.assert_called_once_with(f'https://api.github.com/orgs/{input}')

    def test_public_repos_url(self):
        """ Test the result of public repos url is expected one """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_dt:
            payload = {"repos_url": "https://api.github.com/orgs/myorg/repos"}
            mock_dt.return_value = payload
            cl = GithubOrgClient('myorg')
            res = cl._public_repos_url
            self.assertEqual(res, payload["repos_url"])


if __name__ == "__main__":
    unittest.main()
