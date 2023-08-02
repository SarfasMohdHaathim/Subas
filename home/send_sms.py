from twilio.rest import Client

def send_sms(random_integer,pnumber):
    phone_number =pnumber
    if not phone_number.startswith("+91"):
        phone_number = "+91" + phone_number
    print(phone_number)
    num=random_integer
    account_sid = "ACf905a165668481ea887320d714dd81fc"
    auth_token = "b0d21c7f26299538461c9a5f8cb758b5"
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=f"WELCOME, your otp is {num}",
                        from_='+17623394257',
                        to=f'{phone_number}'
                    )

    print('message send successfully')
