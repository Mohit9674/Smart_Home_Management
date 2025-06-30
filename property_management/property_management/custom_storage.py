# custom_storage.py
from storages.backends.s3boto3 import S3Boto3Storage

class DigitalOceanMediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False
    default_acl = 'public-read'
    custom_domain = None  # Uses AWS_S3_CUSTOM_DOMAIN from settings
    
    def get_default_settings(self):
        settings = super().get_default_settings()
        settings.update({
            'endpoint_url': 'https://lon1.digitaloceanspaces.com',
            'region_name': 'lon1',
        })
        return settings