

# 理论概述

**是什么？LangChain是一个框架，就是一套把大模型和外部世界连接起来的工具代码。**

学习LangChain有六大金刚：

1. Models(模型)
2. Memory(记忆)
3. Retrieval(检索)
4. Chains(链)
5. Agents(智能体)
6. Callback(回调)


# 调用API

**大模型调用三件套：**

1. Api-key
2. 模型名
3. baseUrl


示例代码：调用千问大模型

```python
# LangChain1.0+版本使用方式,目前主流

# 1.导入依赖
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# 2.实例化模型
# 什么是关键字参数 k1=v1 ,k2 = v2
model = init_chat_model(
    model="qwen3.5-plus",
    model_provider="openai",
    api_key="XXXXXXX",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 3.调用模型
print(model.invoke("你是谁").content)
```
