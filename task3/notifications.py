import time
from dataclasses import dataclass


@dataclass
class EmailMessage:
    to: str
    subject: str
    body: str


class EmailGateway:
    """External email sender (imagine it talks to an SMTP server)."""

    def send_email(self, message: EmailMessage) -> None:
        """
        Sends an email.

        Real implementation would connect to an external SMTP server.
        It is intentionally left unimplemented here.
        """
        raise NotImplementedError("This should talk to a real SMTP server")


def send_password_reset(email_gateway: EmailGateway, user_email: str) -> EmailMessage:
    """
    Generates a password reset token based on the current timestamp,
    sends it via EmailGateway, and returns the EmailMessage object.
    """
    timestamp = int(time.time())
    token = f"RESET-{timestamp}"
    subject = "Reset your password"
    body = f"Use this token to reset your password: {token}"

    message = EmailMessage(to=user_email, subject=subject, body=body)
    email_gateway.send_email(message)
    return message
