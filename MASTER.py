import subprocess
import time

# ==========================================
# 007SaaS Swarm - 集群总调度室 (MASTER v2.0)
# ==========================================

def run_step(command, description):
    print(f"\n🚀 [MASTER] 正在启动: {description}...")
    try:
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError:
        print(f"❌ [MASTER] {description} 失败")
        return False

def main():
    print("\n--- 007SaaS SWARM 全链路进化启动 ---")
    
    # 💡 步骤 0: 唤醒 Gemini 开发 Agent
    idea = input("\n💡 著作者，今天有什么激进的想法吗？(直接回车则跳过开发): ")
    if idea.strip():
        # 调用 DEV.py 并传递想法
        subprocess.run(f'python3.14 DEV.py "{idea}"', shell=True)

    # 1. 物理感知阶段
    run_step("python3.14 SENSE.py", "Agent: Sense (深度感知)")

    # 2. 架构演进阶段
    run_step("python3.14 ARCHITECT.py", "Agent: Architect (逻辑生成)")

    # 3. 全球同步阶段
    print("\n🌐 [MASTER] 正在同步至 GitHub Pages...")
    subprocess.run("git add .", shell=True)
    commit_msg = f"Evolution: {time.strftime('%Y%m%d-%H%M')}"
    subprocess.run(f'git commit -m "{commit_msg}"', shell=True)
    subprocess.run("git push origin main", shell=True)

    print("\n✨ [SUCCESS] 集群已完成进化并同步上线！")
    print("🔗 领地地址: https://boscochen13.github.io/007SaaS_Swarm/")

if __name__ == "__main__":
    main()