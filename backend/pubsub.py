import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-1cce9d0c-35f4-11ea-a657-76e5f2bf83fc'
pnconfig.publish_key = 'pub-c-4b7b21c8-c58f-46ef-8920-39f79c55492a'

pubnub = PubNub(pnconfig)

TEST_CHANNEL = 'TEST_CHANNEL'

pubnub.subscribe().channels([TEST_CHANNEL]).execute()

class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Incoming message object: {message_object}')

pubnub.add_listener(Listener())

def main():
    time.sleep(1)

    pubnub.publish().channel(TEST_CHANNEL).message({ 'foo': 'bar' }).sync()

if __name__ == '__main__':
    main()
