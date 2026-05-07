import json
import os

MEMORY_FILE = "agent_memory.json"

def save_memory(key: str, value: str):
    memory = load_all_memory()
    memory[key] = value
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)

def load_all_memory() -> dict:
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}

def get_memory_context() -> str:
    memory = load_all_memory()
    if not memory:
        return "কোনো memory নেই।"
    return "\n".join([f"- {k}: {v}" for k, v in memory.items()])