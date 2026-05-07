from datetime import datetime
import urllib.request
import urllib.parse
import json


def calculator(expression: str) -> str:
    """গণিতের হিসাব করে"""
    try:
        result = eval(expression)
        return f"হিসাবের ফলাফল: {result}"
    except:
        return "হিসাবে সমস্যা হয়েছে"


def get_time(x: str = "") -> str:
    """এখন কয়টা বাজে বলে"""
    now = datetime.now()
    return f"এখন বাজে: {now.strftime('%H:%M:%S')}"


def search_web(query: str) -> str:
    """DuckDuckGo দিয়ে কিছু খোঁজে"""
    

    encoded = urllib.parse.quote(query)
    url = f"https://api.duckduckgo.com/?q={encoded}&format=json&no_html=1"

    try:
        with urllib.request.urlopen(url) as r:
            data = json.loads(r.read())
        result = data.get("AbstractText", "")
        return result if result else "কিছু পাওয়া যায়নি"
    except:
        return "Search-এ সমস্যা হয়েছে"


# সব tool এক জায়গায়
TOOLS = {
    "calculator": calculator,
    "get_time": get_time,
    "search_web": search_web,
}