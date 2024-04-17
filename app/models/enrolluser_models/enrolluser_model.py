from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from beanie import Document, Indexed
from pydantic import EmailStr, Field

class EnrollUserModel(Document):
    mail_firstName: str
    mail_lastName: str
    mail_email: str
    cert_corp_company: str
    cert_org_unit: str
    jobTitle: str
    employeeID: str
    mailStop: str
    additional_field4: str
    additional_field5: str
    locality: str
    state: str
    country: str
    challenge: str
    keyLength: str
    additional_field3: str
    public_key: str


    class Collection:
        name = "enrollusers"
