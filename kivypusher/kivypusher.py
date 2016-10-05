from jnius import autoclass, PythonJavaClass, java_method

_Pusher = autoclass("com.pusher.client.Pusher")
_PusherOptions = autoclass("com.pusher.client.PusherOptions")
# _Channel = jnius.autoclass("com.pusher.client.channel.Channel")
#_SubscriptionEventListener = jnius.autoclass("com.pusher.client.channel.SubscriptionEventListener")

def defaultcallback(event, channelName, eventName, data):
    print channelName
    print eventName
    print data

class SubscriptionEventListener(PythonJavaClass):
    __javainterfaces__ = ["com/pusher/client/channel/SubscriptionEventListener"]
    __javacontext__ = "app"

    onEventCallback = defaultcallback

    @java_method('(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V')
    def onEvent(self, channelName, eventName, data):
        print "==================="
        print "GOT EVENTS!"
        print "==================="
        self.onEventCallback(channelName, eventName, data)


class PusherOptions():
    #the options are a work in progress
    def __init__(self):
        self.pusheroptions = _PusherOptions()

    def set_cluster(self, cluster):
        self.pusheroptions.setCluster(cluster)

    def set_activity_timeout(self, activitytimeout):
        self.pusheroptions.setActivityTimeout(activitytimeout)

    def set_encrypted(self, encrypted):
        self.pusheroptions.setEncrypted(encrypted)

    def set_host(self, host):
        self.pusheroptions.setHost(host)

    def set_pong_timeout(self, timeout):
        self.pusheroptions.setPongTimeout(timeout)

    def set_ws_port(self, wsport):
        self.pusheroptions.setWsPort(wsport)

    def set_wss_port(self, wssport):
        self.pusheroptions.setWssPort(wssport)


class Pusher():
    def __init__(self, key):
        self.pusher = _Pusher(key)

    def connect(self):
        self.pusher.connect()

    def disconnect(self):
        self.pusher.disconnect()

    def bind_channel_simple(self, channel):
        self.channel = self.pusher.subscribe(channel)

    def bind_event(self, event, listener):
        self.channel.bind(event, listener)
