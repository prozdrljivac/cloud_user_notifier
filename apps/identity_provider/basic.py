from abc import ABC, abstractmethod
from typing import Any, List, Self


class BasicIdentityProvider(ABC):
    @abstractmethod
    def list_users(self: Self) -> Any:
        pass

    @abstractmethod
    def list_all_users(self: Self) -> Any:
        pass

    @abstractmethod
    def get_user_emails(self: Self) -> List[str]:
        pass
