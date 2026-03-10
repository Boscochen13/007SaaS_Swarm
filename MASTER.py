import subprocess
import time

# ==========================================
# 007SaaS Swarm - 集群总调度室 (MASTER)
# 著作者: Chen Changxing (chenchangxing52@gmail.com)
# ==========================================

def run_step(command, description):
    print(f"\n🚀 [MASTER] 正在启动: {description}...")
    try:
        # 使用 python3.14 执行脚本
        result = subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ [MASTER] {description} 失败: {e}")
        return False

def main():
    print("      ___   ___ _____ _____               ____  ")
    print("     / _ \\ / _ \\___  / ___| __ _  __ _  / ___| ")
    print("    | | | | | | | / /\\___ \\/ _` |/ _` | \\___ \\ ")
    print("    | |_| | |_| |/ /  ___) | (_| | (_| |  ___) |")
    print("     \\___/ \\___//_/  |____/ \\__,_|\\__,_| |____/ ")
    print("\n--- 007SaaS SWARM 集群调度系统启动 ---")
    
    # 1. 物理感知阶段
    if not run_step("python3.14 SENSE.py", "Agent: Sense (深度感知)"): return

    # 2. 架构演进阶段
    if not run_step("python3.14 ARCHITECT.py", "Agent: Architect (逻辑生成)"): return

    # 3. 全球同步阶段 (Git 自动化)
    print("\n🌐 [MASTER] 正在准备同步至 GitHub Pages...")
    run_step("git add .", "Git: 暂存变更")
    commit_msg = f"Swarm Pulse: {time.strftime('%Y-%m-%d %H:%M:%S')} Pulse by Master"
    run_step(f'git commit -m "{commit_msg}"', "Git: 签署主权快照")
    run_step("git push origin main", "Git: 全球领地同步")

    print("\n✨ [SUCCESS] 集群全链路演进完成！")
    print("🔗 请访问: https://boscochen13.github.io/007SaaS_Swarm/")

if __name__ == "__main__":
    main()