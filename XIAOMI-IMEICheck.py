import time
import requests

def query_mi_device_status():
    imei = input("请输入 IMEI：").strip()

    timestamp = int(time.time() * 1000)
    url = f"https://i.mi.com/support/anonymous/status?ts={timestamp}&id={imei}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.138 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://i.mi.com/find/device/activationlock?_locale=zh_CN",
        "X-Requested-With": "by.qixishunzi",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-ch-ua": "\"Chromium\";v=\"112\", \"Not-A.Brand\";v=\"99\", \"Microsoft Edge\";v=\"112\"",
        "sec-ch-ua-mobile": "?0",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": "uLocale=zh_CN; certification=; iplocale=zh_CN; i.mi.com_slh=xxx; i.mi.com_ph=xxx; i.mi.com_istrudev=true; csrfToken=xxx; ..."
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()

        if data.get("code") == 0:
            locked = data.get("data", {}).get("locked")
            if locked:
                print("设备已开启‘查找设备’功能。")
            else:
                print("设备未开启‘查找设备’功能。")
        else:
            print(f"查询失败，错误信息: {data.get('description', '未知错误')}")
    except requests.RequestException as e:
        print("请求失败：", e)
    except ValueError:
        print("返回内容不是有效的 JSON。")

if __name__ == "__main__":
    query_mi_device_status()