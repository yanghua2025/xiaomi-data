import requests
import datetime
import csv
import json

# 获取今日日期（香港时间）
today = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
trade_date = today.strftime("%Y-%m-%d")

# 港交所CSV链接（固定路径 + 日期）
hkex_url = "https://www1.hkex.com.hk/hkexwidget/data/getHKEXStockQuote?stockcode=1810&lang=chi"

# 发起请求（使用港交所公开接口）
response = requests.get(hkex_url, timeout=10)
data = response.json()

# 提取核心行情字段（使用港交所接口结构）
try:
    quote = data['stockQuote']['quote']
    open_price = float(quote['open'])
    high_price = float(quote['high'])
    low_price = float(quote['low'])
    close_price = float(quote['close'])

    output = {
        "symbol": "01810.HK",
        "date": trade_date,
        "open": open_price,
        "high": high_price,
        "low": low_price,
        "close": close_price
    }

    # 保存为 JSON 文件
    filename = f"xiaomi-{trade_date}.json"
    with open(filename, 'w') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print("✅ 数据抓取成功，文件已保存：", filename)

except Exception as e:
    print("❌ 抓取失败：", e)
