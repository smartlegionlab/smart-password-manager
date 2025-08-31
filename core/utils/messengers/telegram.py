import json
import urllib.request
import urllib.error
import urllib.parse

from core.models import SiteConfig


class TelegramMessenger:
    def __init__(self, token):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{self.token}/"

    def send_message(self, chat_id, message):
        url = f"{self.base_url}sendMessage"
        data = {
            'chat_id': chat_id,
            'text': message
        }

        data_bytes = json.dumps(data).encode('utf-8')

        try:
            request = urllib.request.Request(
                url,
                data=data_bytes,
                headers={'Content-Type': 'application/json'}
            )
            with urllib.request.urlopen(request) as response:
                return json.loads(response.read().decode('utf-8'))

        except urllib.error.HTTPError as e:
            error_message = e.read().decode('utf-8')
            raise Exception(f"HTTP Error {e.code}: {error_message}")
        except Exception as e:
            raise Exception(f"Error sending message: {str(e)}")

def send_telegram_message(telegram_id, message):
    site_config = SiteConfig.objects.first()
    tg_messenger = TelegramMessenger(site_config.telegram_bot_token)
    status = tg_messenger.send_message(chat_id=telegram_id, message=message)
    return status
