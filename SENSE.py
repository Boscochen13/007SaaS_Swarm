import os
import json

# 感知边界定义
PROJECT_PATH = "." # 仅限当前文件夹
SENSING_ID = "chenchangxing52-SENSE-01"

def perform_scan():
    # 只感知文件结构和 Git 状态，不读取文件内容（保护隐私）
    report = {
        "id": SENSING_ID,
        "files": os.listdir(PROJECT_PATH),
        "git_status": os.path.exists(".git"),
        "timestamp": "2026-03-09"
    }
    
    # 将感知结果导出为 JSON
    with open("SENSE_REPORT.json", "w") as f:
        json.dump(report, f, indent=4)
    
    print("✅ [Judge] 感知完成。报告已生成：SENSE_REPORT.json")
    print("⚠️  提示：您可以打开该文件查看，确认无隐私泄露后再发给 Architect。")

if __name__ == "__main__":
    perform_scan()