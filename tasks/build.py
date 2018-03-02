"""
Generic build tasks
"""
from invoke import task

@task
def get_aws_key_id(ctx):
    """
    A build utility to get the access key id from the profile
    """
    access_key_id, secret_access_key = get_keys_from_profile(ctx)

    print(access_key_id)

@task
def get_aws_secret(ctx):
    """
    A build utility to get the access key id from the profile
    """
    access_key_id, secret_access_key = get_keys_from_profile(ctx)

    print(secret_access_key)

def get_keys_from_profile(ctx):
    import urllib2
    import json
    aws_security_url = "http://169.254.169.254/latest/meta-data/iam/security-credentials/"
    res = urllib2.urlopen(aws_security_url, timeout=5)
    if res.code >= 400:
        raise "Status Code"
    profile_name = res.read()
    res = urllib2.urlopen(aws_security_url + profile_name, timeout=5)
    if res.code >= 400:
        raise "Status Code"

    res_body = json.loads(res.read())

    access_key_id = res_body['AccessKeyId']
    secret_access_key = res_body['SecretAccessKey']
    return access_key_id, secret_access_key
