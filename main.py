import argparse
import sys

from apps.identity_provider.utils import get_email_provider, get_identity_provider

argument_parser = argparse.ArgumentParser(
    description="Sends email to all users on specified cloud provider",
)
argument_parser.add_argument(
    "cloud_provider",
    help="Identifies what cloud provider will be used for the script",
)

try:
    args = argument_parser.parse_args()
except argparse.ArgumentError as e:
    print("Error: Missing required argument")
    argument_parser.print_help()
    sys.exit(1)


def main():
    cloud_client = args.cloud_provider
    identity_provider = get_identity_provider(cloud_client=cloud_client)
    email_provider = get_email_provider(cloud_client=cloud_client)
    users = identity_provider.list_all_users()
    user_emails = identity_provider.get_user_emails(users=users)
    email_provider.notify_users(emails=user_emails)


if __name__ == "__main__":
    main()
