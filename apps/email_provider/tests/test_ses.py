import unittest
from unittest.mock import Mock, patch

from apps.email_provider.ses import AWSSes


class TestAWSSes(unittest.TestCase):
    def test_send_email(self):
        aws_ses = AWSSes()

        with patch.object(aws_ses._AWSSes__client, "send_email") as mock_send_email:
            expected_source = "no-reply@ai8.io"
            expected_destination = {"ToAddresses": ["recipient@example.com"]}
            expected_message = {
                "Subject": {
                    "Data": "Test Subject",
                },
                "Body": {
                    "Html": {
                        "Data": "Test Body",
                    },
                },
            }
            aws_ses.send_email(
                source=expected_source,
                destination=expected_destination,
                message=expected_message,
            )
            mock_send_email.assert_called_with(
                Source=expected_source,
                Destination=expected_destination,
                Message=expected_message,
            )

    def test_notify_users(self):
        aws_ses = AWSSes()
        emails = ["user1@example.com", "user2@example.com", "user3@example.com"]
        aws_ses.send_email = Mock()
        aws_ses.notify_users(emails)
        self.assertEqual(aws_ses.send_email.call_count, len(emails))


if __name__ == "__main__":
    unittest.main()
