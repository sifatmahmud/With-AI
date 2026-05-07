from groq import Groq
from ai_agent.tools import TOOLS
import os
from dotenv import load_dotenv

load_dotenv()
groq_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=groq_key)


SYSTEM_PROMPT = """
তুমি একজন helpful AI Assistant।

তোমার কাছে এই tools আছে:
- calculator : গণিত করার জন্য। Input দিবি expression, যেমন: 2+2 বা 10*5
- get_time   : এখন কয়টা বাজে জানার জন্য। Input লাগে না।
- search_web : কিছু জানার জন্য। Input দিবি query।

যখন tool use করতে হবে, শুধু এভাবে লিখবি:
TOOL_CALL: tool_name | input

উদাহরণ:
TOOL_CALL: calculator | 25 * 4
TOOL_CALL: get_time |
TOOL_CALL: search_web | Bangladesh population

যখন সরাসরি উত্তর দিতে পারবি, tool ছাড়াই উত্তর দিবি।
"""


def run_agent(user_input: str):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_input}
    ]

    print(f"\n{'='*50}")
    print(f"👤 তুমি: {user_input}")
    print(f"{'='*50}")

    # সর্বোচ্চ ৫ step চেষ্টা করবে
    for step in range(5):

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages
        )

        reply = response.choices[0].message.content.strip()

        
        if "TOOL_CALL:" in reply:
            print(f"\n🔧 Step {step+1}: Tool use করছে...")

            
            tool_part = reply.split("TOOL_CALL:")[1].strip()
            parts = tool_part.split("|")
            tool_name = parts[0].strip()
            tool_input = parts[1].strip() if len(parts) > 1 else ""

            print(f"   Tool: {tool_name}")
            print(f"   Input: {tool_input}")

            
            if tool_name in TOOLS:
                result = TOOLS[tool_name](tool_input)
                print(f"   ফলাফল: {result}")

                
                messages.append({"role": "assistant", "content": reply})
                messages.append({"role": "user", "content": f"Tool result: {result}"})

            else:
                print(f"   ❌ Tool পাওয়া যায়নি: {tool_name}")
                break

        else:
            
            print(f"\n✅ Agent-এর উত্তর:\n{reply}")
            return reply

    return "উত্তর দিতে পারলাম না"


# চালু করার জন্য
if __name__ == "__main__":
    print("🤖 AI Agent চালু হয়েছে! (বের হতে 'quit' লিখ)\n")

    while True:
        user_input = input("তোমার প্রশ্ন: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "quit":
            print("Agent বন্ধ হয়ে গেল!")
            break

        run_agent(user_input)