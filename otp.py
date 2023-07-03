# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import time


def otp():
  account_sid = "AC99a81d21e965ed6872119b5f622fa915"
  auth_token = "f560c0603a3f921d3b3913e9460ab201"
  verify_sid = "VA8f0c5484e146c568d18bbe64e8408976"
  verified_number = "+919129093900"

  client = Client(account_sid, auth_token)

  verification = client.verify.v2.services(verify_sid) \
    .verifications \
    .create(to=verified_number, channel="sms")
  print(verification.status)


  otp_code = input("OTP : ")

  verification_check = client.verify.v2.services(verify_sid) \
    .verification_checks \
    .create(to=verified_number, code=otp_code)
  if verification_check.status == "approved" :
    return True
  else:
    return False
