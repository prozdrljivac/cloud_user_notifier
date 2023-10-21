import boto3
import time

from typing import Any, Dict, List, Self

from apps.email_provider.basic import BasicEmailProvider


class AWSSes(BasicEmailProvider):
    def __init__(self) -> None:
        self.__client = boto3.client("ses")

    def send_email(
        self: Self,
        source: str,
        destination: Dict,
        message: Dict,
        **kwargs,
    ) -> Any:
        return self.__client.send_email(
            Source=source,
            Destination=destination,
            Message=message,
            **kwargs,
        )

    def notify_users(self, emails: List[str]) -> None:
        for index, email in enumerate(emails):
            try:
                self.send_email(
                    source="test@test.com",
                    destination={
                        "ToAddresses": [email],
                    },
                    message={
                        "Subject": {
                            "Data": "Test Subject",
                        },
                        "Body": {
                            "Html": {
                                "Data": "<b>This is a test</b>",
                            },
                        },
                    },
                )
                print(f"Sent {index+1} of {len(emails)}")
            except Exception as e:
                print(f"Email was not sent to {email}")
            # Slowed down requests so SES can process them easily
            time.sleep(0.5)
