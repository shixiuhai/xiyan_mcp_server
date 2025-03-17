[💻 XiYan-mcp-server](https://github.com/XGenerationLab/xiyan_mcp_server) | 
[💻 XiYan-SQL](https://github.com/XGenerationLab/XiYan-SQL) |
[📖 Arxiv](https://arxiv.org/abs/2411.08599) | 
[📄 PapersWithCode](https://paperswithcode.com/paper/xiyan-sql-a-multi-generator-ensemble)

[![smithery badge](https://smithery.ai/badge/@XGenerationLab/xiyan_mcp_server)](https://smithery.ai/server/@XGenerationLab/xiyan_mcp_server)

[English](https://github.com/XGenerationLab/xiyan_mcp_server)  | [中文](https://github.com/XGenerationLab/xiyan_mcp_server/README_zh.md)

# XiYan MCP 服务器

一个模型上下文协议（MCP）服务器，支持通过自然语言查询数据库，使用 [XiYanSQL](https://github.com/XGenerationLab/XiYan-SQL) 作为文本到 SQL 的技术。

我们目前支持 MySQL 数据库，更多方言即将推出。

## 特性
- 通过 [XiYanSQL](https://github.com/XGenerationLab/XiYan-SQL) 以自然语言获取数据
- 列出可用的 MySQL 表作为资源
- 读取表内容

## 安装

需要 Python 3.11 或更高版本。 
您可以通过 pip 安装该服务器，它将安装最新版本。

```bash
pip install xiyan-mcp-server
```

安装后，您可以直接运行服务器：
```bash
python -m xiyan-mcp-server
```
但在完成以下配置之前，它将不提供任何功能。您将获得一个 yml 文件。之后，您可以通过以下方式运行服务器：
```yaml
env YML=path/to/yml python -m xiyan-mcp-server
```

## 配置

您需要一个 yml 配置文件来配置服务器。
默认配置文件在 `config_demo.yml` 中提供，其内容如下：

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

### 关于 LLM
``Name`` 是要使用的模型名称，``key`` 是模型的 API 密钥，``url`` 是模型的 API 地址。我们支持以下模型。
#### 使用通用 LLM
如果您想使用通用 LLM，例如 gpt3.5，您可以直接如下配置：
```yaml
model:
  name: "gpt-3.5-turbo"
  key: "YOUR KEY"
  url: "https://api.openai.com/v1/chat/completions"
database:
```

如果您想使用阿里巴巴的 Qwen，例如 Qwen-max：
```yaml
model:
  name: "qwen-max"
  key: "YOUR KEY"
  url: "https://dashscope.aliyuncs.com/compatible-mode/v1"
database:
```

#### 使用文本到 SQL 的 SOTA 模型
最后，我们推荐使用 XiYanSQL-qwencoder-32B (https://github.com/XGenerationLab/XiYanSQL-QwenCoder)，这是text-to-SQL 的 SOTA 模型。
我们将模型部署在 DashScope 上，因此您需要设置以下环境变量：
请联系我们以获取 ``key``。
```yaml
model:
  name: "pre-xiyan_multi_dialect_v3"
  key: "KEY"
  url: "https://poc-dashscope.aliyuncs.com/compatible-mode/v1"
database:
```

#### 本地 LLM

未来将支持。

### 关于数据库
``host``, ``port``, ``user``, ``password``, ``database`` 是 MySQL 数据库的连接信息。

您可以使用本地或任何远程数据库。现在我们支持 MySQL（即将支持更多方言）。

```yaml
database:
  host: "localhost"
  port: 3306
  user: "root"
  password: ""
  database: ""
```

## 引用
如果您觉得我们的工作有帮助，请随意引用我们。
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