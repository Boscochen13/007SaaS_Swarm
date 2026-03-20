import os
import time
import subprocess
import re
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from dotenv import load_dotenv

# --- [著作者核心网络配置] ---
# 这里直接在系统层面锁定代理，让官方库强制走隧道
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def run_evolution(idea):
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            code = f.read()
        
        print(f"🧠 [集群进化] 正在调用 Gemini 2.0 (官方驱动版)...")
        
        # 使用官方 SDK 初始化模型，这种方式自带更强的重试机制
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        prompt = f"你是一个顶级前端专家。修改以下HTML实现：{idea}。只返回HTML代码，绝对不要Markdown标签。\n{code}"
        
        # 增加安全设置，防止因为内容审查导致的 404/拒绝
        safety_settings = {
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        }

        # 官方库自带内部重试，比 requests 手写循环更稳
        response = model.generate_content(prompt, safety_settings=safety_settings)
        
        if response.text:
            final_code = re.sub(r'```(?:html)?', '', response.text).strip()
            with open("index.html", "w", encoding="utf-8") as f:
                f.write(final_code)
            print("💾 [SUCCESS] 本地改写成功！")
            return True
        else:
            print("❌ API 返回内容为空")
            return False

    except Exception as e:
        # 如果还是报错，检查是不是配额问题
        if "429" in str(e):
            print("⏳ [QUOTA] 触发频率限制，建议手工休息 1 分钟再试。")
        else:
            print(f"❌ 系统抖动错误: {e}")
        return False

def sync_to_github():
    print("🌐 [GITHUB] 正在同步...")
    try:
        subprocess.run("git add index.html", shell=True)
        commit_msg = f"AI_Evolution_{time.strftime('%Y%m%d_%H%M%S')}"
        subprocess.run(f'git commit -m "{commit_msg}"', shell=True)
        # 推送时不再受 Python 内部代理影响，走 Git 自身配置
        subprocess.run("git push origin main", shell=True)
        print("✨ [SUCCESS] 进化已同步 GitHub！")
    except Exception as e:
        print(f"⚠️ Git 同步异常: {e}")

# --- 暴力启动测试版 ---
print("\n🔥 正在强制启动 007SaaS SWARM 引擎...")
try:
    idea = input("\n💡 请直接输入指令: ")
    if idea.strip():
        # 这里直接手动调用演化函数
        if run_evolution(idea):
            sync_to_github()
except Exception as e:
    print(f"❌ 启动过程崩溃: {e}")