import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-1cce9d0c-35f4-11ea-a657-76e5f2bf83fc'
pnconfig.publish_key = 'pub-c-4b7b21c8-c58f-46ef-8920-39f79c55492a'


CHANNELS = {
    'TEST': 'TEST',
    'BLOCK': 'BLOCK'
}


class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Channel: {message_object.channel} | Message: {message_object.message}')



class PubSub():
    """
    Handles the publish/subscribe layer of the application.
    Provides communication between the nodes of the blockchain network.
    """
    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener())
    
    def publish(self, channel, message):
        """
        Publish the message object to the channel.
        """
        self.pubnub.publish().channel(channel).message(message).sync()    

    def broadcast_block(self, block):
        """
        Broadcast block objects to all nodes.
        """
        self.publish(CHANNELS['BLOCK'], block.to_json())

def main():
    pubsub = PubSub()

    time.sleep(1)

    pubsub.publish(CHANNELS['TEST'], { 'foo': 'bar' })

if __name__ == '__main__':
    main()
