from google.cloud import storage
import io
from dotenv import load_dotenv
from google. cloud import videointelligence

client = storage.Client()
bucket = client.get_bucket('bucket_of_videos')
objects = bucket.list_blobs()

for blob in objects:
    #print(dir(blob))
    print(blob.metadata)


def main():
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.Feature.LABEL_DETECTION]


