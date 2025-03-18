<h1 align="center">XiYan MCP服务器</h1>
<p align="center">
  <a href="https://github.com/XGenerationLab/XiYan-SQL"><img alt="MCP Playwright" src="https://raw.githubusercontent.com/XGenerationLab/XiYan-SQL/main/xiyanGBI.png" height="60"/></a>
</p>
<p align="center">
  <b>一个模型上下文协议（MCP）服务器，能够通过自然语言查询数据库</b></br>
  <sub>由 <a href="https://github.com/XGenerationLab/XiYan-SQL">XiYan-SQL</a> 提供支持，这是开放基准上的文本到SQL的最新技术</sub>
</p>

<p align="center">
💻 <a href="https://github.com/XGenerationLab/xiyan_mcp_server">XiYan-mcp-server</a> | 
🌐 <a href="https://github.com/XGenerationLab/XiYan-SQL">XiYan-SQL</a> |
📖 <a href="https://arxiv.org/abs/2411.08599"> Arxiv</a> | 
📄 <a href="https://paperswithcode.com/paper/xiyan-sql-a-multi-generator-ensemble">PapersWithCode</a> <br />
  <a href="https://smithery.ai/server/@XGenerationLab/xiyan_mcp_server"><img alt="Smithery Installs" src="https://smithery.ai/badge/@XGenerationLab/xiyan_mcp_server" height="20"/></a><br />
<a href="https://github.com/XGenerationLab/xiyan_mcp_server">英文</a> | <a href="https://github.com/XGenerationLab/xiyan_mcp_server/blob/main/README_zh.md"> 中文 </a>
</p>


## 目录

- [功能](#features)
- [工具预览](#tool-preview)
- [安装](#installation)
  - [通过pip安装](#installing-from-pip)
  - [通过Smithery.ai安装](#installing-from-smitheryai)
- [配置](#configuration)
  - [LLM配置](#llm-configuration)
    - [通用LLMs](#general-llms)
    - [文本到SQL的最新技术模型](#text-to-sql-sota-model)
    - [本地LLMs](#local-llms)
  - [数据库配置](#database-configuration)
- [启动](#launch)
  - [Claude桌面](#claude-desktop)
- [引用](#citation)


## 功能
- 🌐 通过 [XiYanSQL](https://github.com/XGenerationLab/XiYan-SQL) 使用自然语言获取数据
- 🖱️ 列出可用的MySQL表作为资源
- 🔧 阅读表内容

## 工具预览
 - 工具 ``get_data_via_natural_language`` 提供了一个自然语言接口，用于从数据库中检索数据。该服务器将输入的自然语言转换为SQL，并调用数据库返回查询结果。

 - 资源 ``mysql://{table_name}`` 允许在指定特定表名时从数据库获取一部分示例数据以供模型参考。
- 资源 ``mysql://`` 将列出当前数据库的名称

## 安装
### 通过pip安装

需要Python 3.11或更高版本。
您可以通过pip安装服务器，它将安装最新版本。

```bash
pip install xiyan-mcp-server
```

之后您可以通过以下命令直接运行服务器：
```bash
python -m xiyan_mcp_server
```
但在您完成以下配置之前，它不会提供任何功能。
您将获得一个yml文件。之后您可以通过以下命令运行服务器：
```yaml
env YML=path/to/yml python -m xiyan_mcp_server
```

### 通过Smithery.ai安装
请参阅 [@XGenerationLab/xiyan_mcp_server](https://smithery.ai/server/@XGenerationLab/xiyan_mcp_server)

未完全测试。

## 配置

您需要一个yml配置文件来配置服务器。
在config_demo.yml中提供了默认配置文件，内容如下：

```yaml
model:
  name: "pre-xiyan_multi_dialect_v3"
  key: ""
  url: "https://poc-dashscope.aliyuncs.com/compatible-mode/v1"

database:
  host: "localhost"
  port: 3306
  user: "root"
  password: ""
  database: ""
```

### LLM配置
``Name``是要使用的模型名称，``key``是模型的API密钥，``url``是模型的API网址。我们支持以下模型。
#### 通用LLMs
如果您想使用通用LLMs，例如gpt3.5，您可以直接配置如下：
```yaml
model:
  name: "gpt-3.5-turbo"
  key: "YOUR KEY"
  url: "https://api.openai.com/v1/chat/completions"
database:
```

如果您想使用阿里巴巴的Qwen，例如Qwen-max，
```yaml
model:
  name: "qwen-max"
  key: "YOUR KEY"
  url: "https://dashscope.aliyuncs.com/compatible-mode/v1"
database:
```

#### 文本到SQL的最新技术模型
最后，我们推荐XiYanSQL-qwencoder-32B (https://github.com/XGenerationLab/XiYanSQL-QwenCoder)，这是文本到SQL的最新模型。
我们在阿里巴巴云DashScope上部署了该模型，因此您需要设置以下环境变量：
请与我们联系以获取 ``key``。 ( godot.lzl@alibaba-inc.com )
```yaml
model:
  name: "pre-xiyan_multi_dialect_v3"
  key: "KEY"
  url: "https://poc-dashscope.aliyuncs.com/compatible-mode/v1"
database:
```

或者，您也可以在自己的服务器上部署模型（XiYanSQL-qwencoder-32B）。

#### 本地LLMs
未来将提供支持。

### 数据库配置
``host``, ``port``, ``user``, ``password``, ``database`` 是MySQL数据库的连接信息。

您可以使用本地或任何远程数据库。现在我们支持MySQL（更多方言即将推出）。

```yaml
database:
  host: "localhost"
  port: 3306
  user: "root"
  password: ""
  database: ""
```

## 启动
### Claude desktop
在您的claude桌面配置文件中添加以下内容：
```json
{
    "mcpServers": {
        "xiyan-mcp-server": {
            "command": "python",
            "args": [
                "-m",
                "xiyan_mcp_server"
            ],
            "env": {
                "YML": "PATH/TO/YML"
            }
        }
    }
}
```

## 引用
如果您觉得我们的工作有帮助，欢迎引用我们的文章。
```bib
@article{xiyansql,
      title={A Preview of XiYan-SQL: A Multi-Generator Ensemble Framework for Text-to-SQL}, 
      author={Yingqi Gao and Yifu Liu and Xiaoxia Li and Xiaorong Shi and Yin Zhu and Yiming Wang and Shiqi Li and Wei Li and Yuntao Hong and Zhiling Luo and Jinyang Gao and Liyu Mou and Yu Li},
      year={2024},
      journal={arXiv preprint arXiv:2411.08599},
      url={https://arxiv.org/abs/2411.08599},
      primaryClass={cs.AI}
}
```