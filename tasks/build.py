"""
Generic build tasks
"""
from invoke import task

@task
def get_access_key_id_from_profile(ctx):
    """
    Get the access key id from the profile
    """
    access_key_id, secret_access_key = get_keys_from_profile()

    return access_key_id

@task
def get_secret_access_key_from_profile(ctx):
    access_key_id, secret_access_key = get_keys_from_profile()

    return secret_access_key
