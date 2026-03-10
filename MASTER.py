import os
import time
import subprocess
import google.generativeai as genai
from dotenv import load_dotenv

# --- [著作者加速通道] ---
# 已根据您的 Mihomo Party 设置对齐端口
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'
# ----------------------

load_dotenv()

def run_gemini_dev(idea):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ [Error] 未发现 API Key，请检查 .env 文件")
        return False

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            current_code = f.read()

        prompt = f"你是 Chen Changxing 的 AI Agent。修改此代码以实现：{idea}。要求：保留主权认证，保持黑绿霓虹风格。直接返回完整 HTML 代码，不要 Markdown。"

        print("🧠 [MASTER] 正在通过 7890 隧道唤醒 Gemini...")
        
        # 使用流式传输，这样你可以看到进度
        response = model.generate_content(prompt, stream=True)
        new_code = ""
        print("📥 正在接收信号: ", end="")
        for chunk in response:
            print("▋", end="", flush=True)
            new_code += chunk.text
        print("\n✅ 信号接收完毕！")

        print("\n--- 📝 进化方案预览 (前 100 字) ---")
        print(new_code[:100] + "...")
        
        confirm = input("\n🧪 著作者，是否授权此激进想法并写入文件？(y/n): ")
        if confirm.lower() == 'y':
            with open("index.html", "w", encoding="utf-8") as f:
                f.write(new_code)
            print("💾 代码已写入 index.html")
            return True
    except Exception as e:
        print(f"❌ [Error] 连线中断: {e}")
    return False

def main():
    print("\n--- 007SaaS SWARM 全链路进化启动 ---")
    idea = input("\n💡 著作者，今天有什么激进的想法吗？(回车跳过): ")
    
    if idea.strip():
        run_gemini_dev(idea)

    # 运行后续 Agent
    subprocess.run("python3.14 SENSE.py", shell=True)
    subprocess.run("python3.14 ARCHITECT.py", shell=True)
    
    print("\n🌐 同步至 GitHub...")
    subprocess.run("git add .", shell=True)
    subprocess.run(f'git commit -m "Evolution: {time.strftime("%Y%m%d-%H%M")}"', shell=True)
    subprocess.run("git push origin main", shell=True)
    print("\n✨ 集群进化完成！")

if __name__ == "__main__":
    main()