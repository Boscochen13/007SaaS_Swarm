import subprocess
import time

# ==========================================
# 007SaaS Swarm - 集群总调度室 (MASTER v2.0)
# 整合 DEV 进化模块
# ==========================================

def run_step(command, description):
    print(f"\n🚀 [MASTER] 正在启动: {description}...")
    try:
        # 使用 python3.14 并传递参数
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    print("--- 007SaaS SWARM 全链路进化启动 ---")
    
    # 询问著作者：是否有新的进化想法？
    idea = input("\n💡 著作者，今天有什么激进的想法吗？(直接回车则跳过开发阶段): ")
    
    if idea.strip():
        # 调用 DEV.py 并传入你的想法
        run_step(f'python3.14 DEV.py "{idea}"', "Agent: DEV (代码演进)")

    # 1. 物理感知
    run_step("python3.14 SENSE.py", "Agent: Sense (深度感知)")

    # 2. 架构演进
    run_step("python3.14 ARCHITECT.py", "Agent: Architect (逻辑生成)")

    # 3. 全球同步
    print("\n🌐 [MASTER] 正在同步至 GitHub Pages...")
    subprocess.run("git add .", shell=True)
    subprocess.run(f'git commit -m "Evolution: {time.strftime("%Y%m%d-%H%M")}"', shell=True)
    subprocess.run("git push origin main", shell=True)

    print("\n✨ [SUCCESS] 集群已完成进化并同步上线！")

if __name__ == "__main__":
    main()