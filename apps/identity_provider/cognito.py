import boto3

from typing import Dict, List, Self

from settings import AWS_COGNITO_USER_POOL_ID

from apps.identity_provider.basic import BasicIdentityProvider


class AWSCognito(BasicIdentityProvider):
    def __init__(self: Self) -> None:
        self.__client = boto3.client("cognito-idp")
        self.__user_pool_id = AWS_COGNITO_USER_POOL_ID

    def list_users(
        self: Self,
        **kwargs,
    ) -> Dict:
        return self.__client.list_users(
            UserPoolId=self.__user_pool_id,
            **kwargs,
        )

    def list_all_users(
        self: Self,
        **kwargs,
    ) -> List[Dict]:
        users = kwargs.get("users")
        token = kwargs.get("token")

        idp_response = self.list_users(
            AttributesToGet=["email"],
            **{"PaginationToken": token} if token else {},
        )
        tkn = idp_response.get("PaginationToken")

        all_users = (
            [*users, *idp_response["Users"]] if users else [*idp_response["Users"]]
        )

        if not tkn:
            return all_users

        return self.list_all_users(
            users=all_users,
            token=tkn,
        )

    def get_user_emails(self: Self, users: List[Dict]) -> List[str]:
        return [user["Attributes"][0]["Value"] for user in users]
