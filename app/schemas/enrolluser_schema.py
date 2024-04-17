from typing import Optional
from uuid import UUID
from pydantic import BaseModel

# User Response Model
class EnrollUserSchema(BaseModel):
        operation: Optional[str] = None
        form_file:Optional[str] = None
        mail_firstName: Optional[str] = None
        mail_lastName: Optional[str] = None
        mail_email: Optional[str] = None
        cert_corp_company: Optional[str] = None
        cert_org_unit: Optional[str] = None
        jobTitle:Optional[str] = None
        employeeID: Optional[str] = None
        mailStop: Optional[str] = None
        additional_field4: Optional[str] = None
        additional_field5: Optional[str] = None
        locality: Optional[str] = None
        state: Optional[str] = None
        country: Optional[str] = None
        challenge: Optional[str] = None
        keyLength: Optional[str] = None
        additional_field3: Optional[str] = None
        public_key: Optional[str] = None
