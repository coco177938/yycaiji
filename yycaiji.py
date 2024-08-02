import requests
import time

def visit_url():
    url = "http://18av.us.kg/api.php/timming/index.html?enforce=1&name=yy"
    try:
        response = requests.get(url)
        response.raise_for_status()
        time.sleep(10)  # 停留10秒钟
        return f"Visited URL successfully, Status Code: {response.status_code}"
    except requests.RequestException as e:
        return f"Failed to visit URL: {str(e)}"

def send_telegram_message(message):
    bot_token = "7383665841:AAE_RBf5P2zFA3LA2tZ0AkrvoTn13kr1FtM"
    chat_id = "6264072063"
    send_text = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
    try:
        response = requests.get(send_text)
        response.raise_for_status()
        return f"Message sent successfully, Status Code: {response.status_code}"
    except requests.RequestException as e:
        return f"Failed to send message: {str(e)}"

if __name__ == "__main__":
    result = visit_url()
    print(result)
    telegram_result = send_telegram_message(result)
    print(telegram_result)
