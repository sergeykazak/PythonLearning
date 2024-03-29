from dataclasses import dataclass

@dataclass
class User:
    firstName: str = None,
    lastName: str = None,
    fullName: str = None,
    phoneNumber: str = None
