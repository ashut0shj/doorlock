# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import time


def otp():
  account_sid = "ACed6b1e94e3ceebbeaddeda9fb0b98281"
  auth_token = "9bf10b1804ae9b87aed1467668cea709"
  verify_sid = "VAa0ccb5d858bee075ca760059ee641591"
  verified_number = "+919434776497"

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
