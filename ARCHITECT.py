import json
import os
import re

# ==========================================
# 007SaaS Swarm - 深度架构师 (v0.2.0)
# 著作者: Chen Changxing (chenchangxing52@gmail.com)
# ==========================================

def analyze_code_logic(file_path):
    """简单的代码逻辑提取器"""
    if not os.path.exists(file_path): return "未探测到逻辑"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        # 提取注释和函数名作为逻辑线索
        functions = re.findall(r'def\s+(\w+)', content)
        return f"包含核心函数: {', '.join(functions)}"

def run_architect():
    print("🧠 [Architect] 正在进行深度逻辑扫描...")
    
    report_path = "SENSE_REPORT.json"
    if not os.path.exists(report_path): return

    with open(report_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 深度分析：解析 Sense 和 Master 的内部逻辑
    sense_logic = analyze_code_logic("SENSE.py")
    master_logic = analyze_code_logic("MASTER.py")

    manifesto_content = f"""# 007SaaS SWARM - 集群主权宣言 (深度演化版)

> **著作者认证**: {data["sovereignty_mark"]["creator"]}
> **集群大脑**: Python 3.14.3 + Distributed Logic

## 📡 逻辑地图 (Logic Map)
- **SENSE (感知层)**: {sense_logic}
- **MASTER (控制层)**: {master_logic}

## 💎 著作者思路固化
本项目核心在于“意志集群”而非单体。当前的感知列表涵盖了 {len(data["environment_scan"]["items"])} 个活跃节点。

---
*Deep Analysis Completed by ARCHITECT Agent*
"""

    with open("SWARM_MANIFESTO.md", "w", encoding="utf-8") as f:
        f.write(manifesto_content)
    print("✅ [SUCCESS] 深度宣言已生成。")

if __name__ == "__main__":
    run_architect()