from apps.email_provider.basic import BasicEmailProvider
from apps.email_provider.ses import AWSSes
from apps.identity_provider.basic import BasicIdentityProvider
from apps.identity_provider.cognito import AWSCognito


def get_identity_provider(cloud_client: str) -> BasicIdentityProvider:
    match cloud_client:
        case "aws":
            return AWSCognito()
        case _:
            raise NotImplementedError(
                f"Identity Provider not implemented for Cloud Client {cloud_client}"
            )


def get_email_provider(cloud_client: str) -> BasicEmailProvider:
    match cloud_client:
        case "aws":
            return AWSSes()
        case _:
            raise NotImplementedError(
                f"Email Provider not implemented for Cloud Client {cloud_client}"
            )
