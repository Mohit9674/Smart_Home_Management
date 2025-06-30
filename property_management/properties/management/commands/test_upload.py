# properties/management/commands/test_upload.py
from django.core.management.base import BaseCommand
from django.conf import settings
import boto3
from botocore.exceptions import ClientError

class Command(BaseCommand):
    help = 'Test DigitalOcean Spaces upload'

    def handle(self, *args, **options):
        session = boto3.session.Session()
        client = session.client('s3',
                                region_name=settings.AWS_S3_REGION_NAME,
                                endpoint_url=settings.AWS_S3_ENDPOINT_URL,
                                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

        # Test file details
        bucket_name = settings.AWS_STORAGE_BUCKET_NAME
        test_key = 'media/test_direct.txt'  # Using 'media' prefix
        test_content = b'Direct upload test content'

        try:
            # Test upload
            client.put_object(
                Bucket=bucket_name,
                Key=test_key,
                Body=test_content,
                ACL='public-read',
                ContentType='text/plain'
            )
            self.stdout.write(self.style.SUCCESS('✅ File uploaded successfully!'))
            
            # Generate public URL
            public_url = f"https://{bucket_name}.{settings.AWS_S3_REGION_NAME}.digitaloceanspaces.com/{test_key}"
            self.stdout.write(f"Public URL: {public_url}")
            
            # Verify existence
            response = client.head_object(Bucket=bucket_name, Key=test_key)
            self.stdout.write(self.style.SUCCESS('✅ File verified in Spaces'))
            self.stdout.write(f"Metadata: {response['ResponseMetadata']['HTTPHeaders']}")
            
            # Test public access
            import requests
            r = requests.get(public_url)
            if r.status_code == 200:
                self.stdout.write(self.style.SUCCESS('✅ Public access confirmed'))
            else:
                self.stdout.write(self.style.WARNING(f'⚠️ Public access failed: HTTP {r.status_code}'))
            
        except ClientError as e:
            self.stdout.write(self.style.ERROR(f'❌ Upload failed: {e}'))
            # Detailed error diagnostics
            error_code = e.response.get('Error', {}).get('Code')
            error_msg = e.response.get('Error', {}).get('Message')
            self.stdout.write(self.style.ERROR(f'❌ AWS Error: {error_code} - {error_msg}'))