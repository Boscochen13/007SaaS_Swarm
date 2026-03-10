import os
import time
import subprocess
import google.generativeai as genai
from dotenv import load_dotenv

# --- [著作者加速通道] ---
# 已根据您的 Mihomo Party 设置对齐混合端口 7890
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
        # 读取当前领地代码
        with open("index.html", "r", encoding="utf-8") as f:
            current_code = f.read()

        # 构造进化的 Prompt
        prompt = f"""
        你是 Chen Changxing (chenchangxing52@gmail.com) 的 AI 开发 Agent。
        当前 HTML 代码如下：
        {current_code}
        
        著作者最新指令：{idea}
        
        要求：
        1. 必须在代码中添加该功能（如按钮、样式等）。
        2. 保持原有的霓虹黑绿风格和主权认证信息。
        3. 直接返回完整的 HTML 代码，不要包含 ```html 等 Markdown 格式。
        """

        print(f"🧠 [MASTER] 正在通过 7890 隧道唤醒 Gemini 执行进化...")
        
        # 使用流式传输防止长时间卡顿
        response = model.generate_content(prompt, stream=True)
        new_code = ""
        print("📥 正在接收信号: ", end="")
        for chunk in response:
            print("▋", end="", flush=True)
            new_code += chunk.text
        print("\n✅ 信号接收完毕！")

        # 强制清洗可能存在的 Markdown 标签
        clean_code = new_code.replace("```html", "").replace("```", "").strip()

        # 著作者确权环节
        print(f"\n--- 📝 进化方案预览 (前 150 字) ---\n{clean_code[:150]}...")
        confirm = input("\n🧪 著作者，是否授权此激进想法并写入 index.html？(y/n): ")
        
        if confirm.lower() == 'y':
            with open("index.html", "w", encoding="utf-8") as f:
                f.write(clean_code)
            print("💾 [SUCCESS] 核心代码已注入 index.html")
            return True
        else:
            print("⏩ 著作者拒绝授权，放弃本次代码改动。")
            return False
            
    except Exception as e:
        print(f"❌ [连线中断/写入失败]: {e}")
        return False

def run_step(command, description):
    print(f"\n🚀 [MASTER] 正在启动: {description}...")
    try:
        subprocess.run(command, shell=True, check=True)
        return True
    except Exception as e:
        print(f"❌ [MASTER] {description} 执行异常: {e}")
        return False

def main():
    print("\n--- 007SaaS SWARM 全链路进化启动 ---")
    print("著作者认证: chenchangxing52@gmail.com")
    
    # 1. 核心进化阶段 (Gemini)
    idea = input("\n💡 今天有什么激进的想法吗？(如：加一个霓虹红色按钮，回车跳过): ")
    if idea.strip():
        run_gemini_dev(idea)
    else:
        print("⏩ 跳过代码生成阶段。")

    # 2. 物理感知与架构生成 (本地 Agent)
    run_step("python3.14 SENSE.py", "Agent: Sense (深度感知)")
    run_step("python3.14 ARCHITECT.py", "Agent: Architect (逻辑生成)")
    
    # 3. 全球同步阶段 (Git)
    print("\n🌐 [MASTER] 正在同步至 GitHub Pages...")
    subprocess.run("git add .", shell=True)
    commit_msg = f"Evolution: {time.strftime('%Y%m%d-%H%M')}"
    subprocess.run(f'git commit -m "{commit_msg}"', shell=True)
    subprocess.run("git push origin main", shell=True)

    print(f"\n✨ [SUCCESS] 集群已完成进化！同步时间: {time.strftime('%H:%M:%S')}")
    print("🔗 领地地址: [https://boscochen13.github.io/007SaaS_Swarm/](https://boscochen13.github.io/007SaaS_Swarm/)")

if __name__ == "__main__":
    main()