from typing import Optional
from uuid import UUID
import pymongo
from app.core.security import get_password_hash, verify_password
from app.models.user_models.user_model import UserModel
from app.models.enrolluser_models.enrolluser_model import EnrollUserModel
from app.schemas.enrolluser_schema import EnrollUserSchema
from fastapi import HTTPException,Response, status
from fastapi.responses import HTMLResponse

import requests
import ssl
from requests.adapters import HTTPAdapter
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Define the URL of the website you want to access
url = 'https://mpki.paci.gov.kw/services/MinistryofDefenseKAFInformationCenter/client/userEnrollNS.htm'

# Create a custom SSL context with the desired cipher suite TLS_RSA_WITH_AES_256_CBC_SHA
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
ssl_context.set_ciphers('AES256-SHA')


# Create a session and mount a custom adapter with the custom SSL context
session = requests.Session()
adapter = HTTPAdapter(pool_connections=1, pool_maxsize=1, pool_block=True)
adapter.init_poolmanager(connections=1, maxsize=1, block=True, ssl_context=ssl_context)
session.mount('https://', adapter)

# POST URL
post_url = "https://mpki.paci.gov.kw/services/MinistryofDefenseKAFInformationCenter/cgi-bin/sophia.exe"

class EnrollUserService:
    # POST endpoint to handle user enrollment
    @staticmethod
    async def enroll_user(user_data: EnrollUserSchema, user: UserModel):
        """
        :param user_data:
        :return:
        """
        print('I am EnrollUser')

        """ 
        user_in = EnrollUserModel(
            operation= user_data.operation,
            form_file= user_data.form_file,
            mail_firstName= user_data.mail_firstName,
            mail_lastName= user_data.mail_lastName,
            mail_email= user_data.mail_email,
            cert_corp_company= user_data.cert_corp_company,
            cert_org_unit= user_data.cert_org_unit,
            jobTitle= user_data.jobTitle,
            employeeID= user_data.employeeID,
            mailStop= user_data.mailStop,
            additional_field4= user_data.additional_field4,
            additional_field5= user_data.additional_field5,
            locality= user_data.locality,
            state= user_data.state,
            country= user_data.country,
            challenge= user_data.challenge,
            keyLength= user_data.keyLength,
            additional_field3= user_data.additional_field3,
            public_key= user_data.public_key,
            )
        """

        

        # Initialize Jinja2 environment
        env = Environment( #"./"
            #loader=FileSystemLoader('templates'),
            loader=FileSystemLoader("./"),  # Directory containing your HTML templates
            autoescape=select_autoescape(['html', 'xml'])
        )

        payload = {
                    "operation": user_data.operation,
                    "form_file": user_data.form_file,
                    "mail_firstName": user_data.mail_firstName,
                    "mail_lastName": user_data.mail_lastName,
                    "mail_email": user_data.mail_email,
                    "cert_corp_company": user_data.cert_corp_company,
                    "cert_org_unit": user_data.cert_org_unit,
                    "jobTitle": user_data.jobTitle,
                    "employeeID": user_data.employeeID,
                    "mailStop": user_data.mailStop,
                    "additional_field4": user_data.additional_field4,
                    "additional_field5": user_data.additional_field5,
                    "locality": user_data.locality,
                    "state": user_data.state,
                    "country": user_data.country,
                    "challenge": user_data.challenge,
                    "keyLength": user_data.keyLength,
                    "additional_field3": user_data.additional_field3,
                    "public_key": user_data.public_key
                }

        try:
            if not user:
                raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not authen",
        )
            # Send POST request with the custom SSL context
            response = session.post(post_url, data=payload, verify=False)

            # Print the response content
            print(f"I am response: {response.text}")

            #template = env.get_template('response_enroll.html')
            #html_content = template.render(response_text=response.text)

            html_content = """
                        <html>
                            <head>
                                <title>Some HTML in here</title>
                            </head>
                            <body>
                                <h1>Look ma! HTML!</h1>
                            </body>
                        </html>
                        """

            #return HTMLResponse(content=html_content)

            return HTMLResponse(content=response.text, status_code=200)

        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=500, detail=f"External request failed: {str(e)}")




        
    