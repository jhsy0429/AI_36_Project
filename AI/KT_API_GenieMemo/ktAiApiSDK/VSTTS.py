import json
import os
import HttpUtils

HttpUtils = HttpUtils.HttpUtils()

try:
    # Python 3.x
    from configparser import ConfigParser
except ImportError:
    # Python 2.x
    from ConfigParser import SafeConfigParser as ConfigParser
config = ConfigParser()
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'server.config'))
config.read(config_path)

# Decorator
def constant(func):
    def func_set(self, value):
        raise TypeError

    def func_get(self):
        return func()
    return property(func_get, func_set)

class VSTTS:
    @constant
    def VERSION_MAJOR():
        return 1

    @constant
    def VERSION_MINOR():
        return 0

    @constant
    def VERSION_BUILD():
        return 0

    @constant
    def URL_VS_TTS():
        return "/v2/voicestudio/voiceSynthesis"

    def CODE_NAME(self):
        return "VSTTS" + str(self.VERSION_MAJOR) + "." + str(self.VERSION_MINOR) + "." + str(self.VERSION_BUILD)

    def TAG(self):
        return self.CODE_NAME()

    def __init__(self):
        self.service_url = ""
        self.client_key = ""
        self.timestamp = ""
        self.signature = ""
        strUrl = "https://" + config.get('server', 'host') + ":" + config.get('server', 'http_port')
        self.setServiceURL(strUrl)

    def setServiceURL(self, entrypoint):
        self.service_url = entrypoint

    def setAuth(self, clientKey, clientId, clientSecret):

        if not clientKey or not clientId or not clientSecret:
            return

        self.client_key = clientKey
        self.timestamp = HttpUtils.getTimestamp()
        self.signature = HttpUtils.makeSignature(self.timestamp, clientId, clientSecret)

    def requestVSTTS(self, text, speaker, voiceName, pitch, speed, volume, emotion, language, encoding, channel, sampleRate, sampleFmt):

        try:
            metdata_json_object = {}
            metdata_json_object["text"] = text
            metdata_json_object["speaker"] = speaker
            metdata_json_object["voiceName"] = voiceName
            metdata_json_object["pitch"] = pitch
            metdata_json_object["speed"] = speed
            metdata_json_object["volume"] = volume
            metdata_json_object["emotion"] = emotion
            metdata_json_object["language"] = language
            metdata_json_object["encoding"] = encoding
            metdata_json_object["channel"] = channel
            metdata_json_object["sampleRate"] = sampleRate
            metdata_json_object["sampleFmt"] = sampleFmt

            if encoding.lower() == "wav":
                encodingOptObject = {}
                encodingOptObject["channel"] = channel
                encodingOptObject["sampleRate"] = sampleRate
                encodingOptObject["sampleFmt"] = sampleFmt
                metdata_json_object["encodingOpt"] = encodingOptObject

            strUrl = self.service_url + self.URL_VS_TTS

            json_object = {}
            json_object[HttpUtils.REQUEST_PARAMETER_X_CLIENT_KEY] = self.client_key
            json_object[HttpUtils.REQUEST_PARAMETER_X_AUTH_TIMESTAMP] = self.timestamp
            json_object[HttpUtils.REQUEST_PARAMETER_X_CLIENT_SIGNATURE] = self.signature

            response = HttpUtils.requestPost(strUrl, json_object, metdata_json_object)
            responseObj = json.loads(response)

            if responseObj[HttpUtils.RESPONSE_STATUS_CODE] == 301:
                entrypoint = HttpUtils.setHttpEntrypoint(json.loads(responseObj[HttpUtils.RESPONSE_RESULT]))
                self.setServiceURL('https://' + entrypoint)
                strUrl = self.service_url + self.URL_VS_TTS
                return HttpUtils.requestPost(strUrl, json_object, metdata_json_object)
            else:
                return response

        except Exception as e:
            return