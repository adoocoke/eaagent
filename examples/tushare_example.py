"""
Tushare 期货数据 + ReAct Agent 示例
使用前请确保已设置环境变量 TUSHARE_TOKEN
"""

from eaagent import ReActAgent
from eaagent.tools import get_futures_daily


def main():
    print("=== Tushare 期货数据 ReAct Agent 示例 ===\n")

    # 初始化 Agent
    agent = ReActAgent(
        model="grok-4.3",
        verbose=True,
        max_steps=10,
    )

    # 注册 Tushare 工具
    agent.add_tool(
        name="get_futures_daily",
        description="获取指定期货合约的日线数据，包括开盘价、最高价、最低价、收盘价、成交量、持仓量等",
        parameters={
            "type": "object",
            "properties": {
                "ts_code": {
                    "type": "string",
                    "description": "期货合约代码，例如：RB2405.SHF（螺纹钢）、I2409.DCE（铁矿石）、MA2409.CZC（甲醇）、CU2406.SHF（沪铜）"
                },
                "start_date": {
                    "type": "string",
                    "description": "开始日期，格式为 YYYYMMDD，例如 20240101"
                },
                "end_date": {
                    "type": "string",
                    "description": "结束日期，格式为 YYYYMMDD，默认为今天（可选）"
                }
            },
            "required": ["ts_code", "start_date"]
        },
        function=get_futures_daily,
    )

    # 示例问题
    questions = [
        "帮我查询一下螺纹钢 RB2405.SHF 从2024年3月1日到现在的日线数据",
        "铁矿石 I2409.DCE 最近一个月的行情怎么样？",
    ]

    for i, question in enumerate(questions, 1):
        print(f"\n{'='*60}")
        print(f"问题 {i}: {question}")
        print('='*60)

        try:
            answer = agent.run(question)
            print(f"\n最终答案:\n{answer}")
        except Exception as e:
            print(f"运行出错: {e}")

        print()


if __name__ == "__main__":
    main()