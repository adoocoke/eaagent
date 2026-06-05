"""
ReActAgent Memory 功能测试（A计划）
"""

import pytest
from eaagent import ReActAgent


def test_remember_and_recall():
    agent = ReActAgent(verbose=False, require_api_key=False)
    agent.remember("铁矿石趋势", "目前处于下降通道")
    agent.remember("螺纹钢支撑位", "3720附近")

    memory = agent.recall()
    assert "铁矿石趋势" in memory
    assert memory["铁矿石趋势"] == "目前处于下降通道"


def test_recall_specific_key():
    agent = ReActAgent(verbose=False, require_api_key=False)
    agent.remember("关键价位", "3800是重要阻力")
    assert agent.recall("关键价位") == "3800是重要阻力"


def test_recall_nonexistent_key():
    agent = ReActAgent(verbose=False, require_api_key=False)
    assert agent.recall("不存在的记忆") == ""


def test_memory_in_system_prompt():
    agent = ReActAgent(verbose=False, max_steps=1, require_api_key=False)
    agent.remember("测试记忆", "这是一个测试记忆")
