import os
import time
import subprocess
import google.generativeai as genai
from dotenv import load_dotenv

# --- [著作者加速通道] ---
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'
# ----------------------

load_dotenv()

def run_gemini_dev(idea):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ [Error] 未发现 API Key")
        return False

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            current_code = f.read()

        prompt = f"你是开发 Agent。修改以下代码以实现：{idea}。要求：保持原有黑绿风格，直接返回完整 HTML，不要 Markdown 标签。\n\n代码如下：\n{current_code}"

        print(f"🧠 [MASTER] 正在强制进化指令: {idea}")
        
        response = model.generate_content(prompt)
        new_code = response.text.strip()

        # 核心清洗逻辑：防止 Markdown 格式破坏网页
        clean_code = new_code.replace("```html", "").replace("```", "").strip()

        # --- 著作者改动：取消确认，直接写入 ---
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(clean_code)
        print("💾 [SUCCESS] 核心代码已成功写入 index.html！")
        return True
            
    except Exception as e:
        print(f"❌ [进化失败]: {e}")
        return False

def main():
    print("\n--- 007SaaS SWARM 全自动进化启动 ---")
    
    # 强制获取指令
    idea = input("\n💡 著作者指令 (例如：在页面底部加一个红色霓虹按钮): ")
    
    if idea.strip():
        # 执行进化并写入
        run_gemini_dev(idea)
        
        # 写入成功后，立刻执行 Git 同步
        print("\n🌐 [MASTER] 正在同步至全球节点...")
        subprocess.run("git add .", shell=True)
        commit_msg = f"Auto-Evolution: {time.strftime('%Y%m%d-%H%M')}"
        subprocess.run(f'git commit -m "{commit_msg}"', shell=True)
        subprocess.run("git push origin main", shell=True)
        print(f"\n✨ [SUCCESS] 进化已同步！更新时间: {time.strftime('%H:%M:%S')}")
    else:
        print("⏩ 无指令输入，集群保持静默。")

if __name__ == "__main__":
    main()