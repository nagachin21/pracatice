
if __name__ == '__main__':

    import jwt

    jwk_json = """{
            "use": "sig",
            "kid": "0cc175b9c0f1b6a831c399e269772661",
            "e": "AQAB",
            "kty": "RSA",
            "alg": "RS256",
            "n": "0bXcnrheJ2snfq1wv6Qz8-TEPDGKHCM0SsrQjxEFpXSEycL2_A-oW1ZGUzCuhz4HH4wkvc4CDJl25johSIUTVyo4mrFrJ0ab0QAhrWE7gMyWFIfraj9cksPAGyVAiXLCN9Ly2xuoJxFjCAZXw1VO8i7RTYK8ZP6dhcosiyzdhYt7C_65B5ikmCS4AymXIa83QQanCtjoGiwy4Cf2pLnn9zXMZEnqQ-wwSoGn32YExmap7GAtjOwHNWU5zpW3dwNMq-zkcln3ICEBwxDpWJhEZHZPBpPWgN-dQZDR2FiGHJgUFE3EM-CIcwxekrRBP-R3xEUeMFf5z1HeQNK8sjZeRw"
        }"""

    from jwt.algorithms import RSAAlgorithm

    public_key = RSAAlgorithm.from_jwk(jwk_json)

    id_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjBjYzE3NWI5YzBmMWI2YTgzMWMzOTllMjY5NzcyNjYxIn0.eyJpc3MiOiJodHRwczpcL1wvYXV0aC5sb2dpbi55YWhvby5jby5qcFwveWNvbm5lY3RcL3YyIiwic3ViIjoiWkFEWEkyTVJLRFEyV0I1RVVZN1gzQ0Q1R00iLCJhdWQiOlsiZGowMGFpWnBQVk4yY1hGUVR6Tk9iM1J0ZHlaelBXTnZibk4xYldWeWMyVmpjbVYwSm5nOU5ERS0iXSwiZXhwIjoxNTk1NTk3OTk0LCJpYXQiOjE1OTMxNzg3OTQsImFtciI6WyJwd2QiXSwibm9uY2UiOiJlZjNhMDkxOTI4ZDU0OTE2MjRjMGFjNTRkNjk3MTI0NDIyNzA1MDkyIiwiYXRfaGFzaCI6InRvMXBONlBGb0ZBR1h2SWRxWS1ORmcifQ.WfpfaAnWQs6nC__kXocEKJlRUe4BH9nMbVRjgoU2ZcjYn5CuhluPZVAIFsIpGptYdsj2FKMws37xLLEnAjoHHdlqlEaiU7pzTswREn4x9cIXBBi5D4en515AwOqYS5EC7ehZDKSvgKPXQHF-ZzVDflaCCCxtspvOhBzSzybXQWVtshU4W9QPj5d2UySJJliB9mLSs2ezF-6vWownpd3DxEgj74xdrliZy2pLxp45NBNwOEw9FOlYliu6pujjL5PfFmC-NgQEjIUxaRlFwjFIyUJfIOX5JHbBwVWI8sou381QlxuR6e7t07eIXerT0ANfmvImiasE6uWiohSZU9_lzw'
    client_secret = 'TwogazlflaTnaN4Xkq96hojB2acTZJ7zghR7GVbA'
    issuer = 'https://auth.login.yahoo.co.jp/yconnect/v2'
    client_id = 'dj00aiZpPVN2cXFQTzNOb3RtdyZzPWNvbnN1bWVyc2VjcmV0Jng9NDE-'

    claims = jwt.decode(id_token,
                        public_key,
                        issuer=issuer,
                        audience=client_id,
                        algorithms=["RS256"])

    print(claims)
