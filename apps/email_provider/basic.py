from abc import ABC, abstractmethod

from typing import Any, Self


class BasicEmailProvider(ABC):
    @abstractmethod
    def send_email(self: Self) -> Any:
        pass

    @abstractmethod
    def notify_users(self: Self) -> None:
        pass
