

https://auth.login.yahoo.co.jp/yconnect/v2/authorization?
response_type=code
&client_id=dj00aiZpPVN2cXFQTzNOb3RtdyZzPWNvbnN1bWVyc2VjcmV0Jng9NDE-
&redirect_uri=http://example.com/
&state=xyz
&scope=openid+profile
&nonce=ef3a091928d5491624c0ac54d697124422705092



curl -d \
"grant_type=authorization_code&\
client_id=dj00aiZpPVN2cXFQTzNOb3RtdyZzPWNvbnN1bWVyc2VjcmV0Jng9NDE-&\
client_secret=TwogazlflaTnaN4Xkq96hojB2acTZJ7zghR7GVbA&\
code=SEBZnjPM&\
redirect_uri=http://example.com/" \
https://auth.login.yahoo.co.jp/yconnect/v2/token

#basic認証を利用してリクエストする場合 >>
echo -n "<client_id:client_secret> | base64" #authorization headerへ入れる情報作成

curl -H 'Authorization: Basic ZGowMGFpWnBQVk4yY1hGUVR6Tk9iM1J0ZHlaelBXTnZibk4xYldWeWMyVmpjbVYwSm5nOU5ERS06VHdvZ2F6bGZsYVRuYU40WGtxOTZob2pCMmFjVFpKN3pnaFI3R1ZiQQ==' \
-d "grant_type=authorization_code&\
code=suNDO5EF&\
redirect_uri=http://example.com/" \
https://auth.login.yahoo.co.jp/yconnect/v2/token
# <<


echo '<ID token header> or <ID token payload>'| base64 --decode

echo 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjBjYzE3NWI5YzBmMWI2YTgzMWMzOTllMjY5NzcyNjYxIn0' | base64 --decode
> {"typ":"JWT","alg":"RS256","kid":"0cc175b9c0f1b6a831c399e269772661"}



curl  https://auth.login.yahoo.co.jp/yconnect/v2/jwks
>
{
  "keys": [
  {
    "kid": "0cc175b9c0f1b6a831c399e269772661",
    "kty": "RSA",
    "alg": "RS256",
    "use": "sig",
    "n": "0bXcnrheJ2snfq1wv6Qz8-TEPDGKHCM0SsrQjxEFpXSEycL2_A-oW1ZGUzCuhz4HH4wkvc4CDJl25johSIUTVyo4mrFrJ0ab0QAhrWE7gMyWFIfraj9cksPAGyVAiXLCN9Ly2xuoJxFjCAZXw1VO8i7RTYK8ZP6dhcosiyzdhYt7C_65B5ikmCS4AymXIa83QQanCtjoGiwy4Cf2pLnn9zXMZEnqQ-wwSoGn32YExmap7GAtjOwHNWU5zpW3dwNMq-zkcln3ICEBwxDpWJhEZHZPBpPWgN-dQZDR2FiGHJgUFE3EM-CIcwxekrRBP-R3xEUeMFf5z1HeQNK8sjZeRw",
    "e": "AQAB"
  },




curl -H 'Authorization: Bearer {access_token}' https://userinfo.yahooapis.jp/yconnect/v2/attribute?schema=openid


print(b'\u4f91\u8cb4'.decode('unicode-escape'))
