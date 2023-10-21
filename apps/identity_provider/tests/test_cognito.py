import unittest
from unittest.mock import Mock

from apps.identity_provider.cognito import AWSCognito


class TestAWSCognito(unittest.TestCase):
    def setUp(self):
        self.cognito_client = Mock()
        self.cognito_client.list_users.return_value = {
            "Users": [
                {"Attributes": [{"Name": "email", "Value": "user1@example.com"}]},
                {"Attributes": [{"Name": "email", "Value": "user2@example.com"}]},
            ],
            "PaginationToken": None,
        }

        self.aws_cognito = AWSCognito()
        self.aws_cognito._AWSCognito__client = self.cognito_client

    def test_list_all_users(self):
        users = self.aws_cognito.list_all_users()
        self.assertEqual(len(users), 2)

    def test_get_user_emails(self):
        users = [
            {
                "Attributes": [
                    {
                        "Name": "email",
                        "Value": "user1@example.com",
                    },
                ],
            },
            {
                "Attributes": [
                    {
                        "Name": "email",
                        "Value": "user2@example.com",
                    },
                ],
            },
        ]
        emails = self.aws_cognito.get_user_emails(users)
        self.assertEqual(emails, ["user1@example.com", "user2@example.com"])


if __name__ == "__main__":
    unittest.main()
