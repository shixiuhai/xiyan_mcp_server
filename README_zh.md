以下是您提供的文本的中文翻译：

---

[💻 XiYan-mcp-server](https://github.com/XGenerationLab/xiyan_mcp_server) | 
[💻 XiYan-SQL](https://github.com/XGenerationLab/XiYan-SQL) |
[📖 Arxiv](https://arxiv.org/abs/2411.08599) | 
[📄 PapersWithCode](https://paperswithcode.com/paper/xiyan-sql-a-multi-generator-ensemble)

[![smithery badge](https://smithery.ai/badge/@XGenerationLab/xiyan_mcp_server)](https://smithery.ai/server/@XGenerationLab/xiyan_mcp_server)

[English](https://github.com/XGenerationLab/xiyan_mcp_server)  | [中文](https://github.com/XGenerationLab/xiyan_mcp_server/blob/main/README_zh.md)

# XiYan MCP 服务器

一个模型上下文协议（MCP）服务器，支持通过自然语言查询数据库，使用 [XiYanSQL](https://github.com/XGenerationLab/XiYan-SQL) 作为文本到 SQL 的技术。

我们目前支持 MySQL 数据库，更多方言即将推出。

## 1. 特性
- 通过 [XiYanSQL](https://github.com/XGenerationLab/XiYan-SQL) 以自然语言获取数据
- 列出可用的 MySQL 表作为资源
- 读取表内容

## 2. 工具预览
- 工具 ``get_data_via_natural_language`` 提供了一个自然语言接口，从数据库中检索数据。该服务器将输入的自然语言转换为 SQL，并调用数据库返回查询结果。

- ``mysql://{table_name}`` 资源允许在指定特定 `table_name` 的情况下，从数据库中获取部分样本数据，以供模型参考。
- ``mysql://`` 资源将列出当前数据库的名称。

## 3. 安装
### 3.1 从 pip 安装

需要 Python 3.11 或更高版本。 
您可以通过 pip 安装该服务器，它将安装最新版本。

```bash
pip install xiyan-mcp-server
```

安装后，您可以直接运行服务器：
```bash
python -m xiyan-mcp-server
```
但是在完成以下配置之前，它不会提供任何功能。您将获得一个 yml 文件。之后，您可以通过以下方式运行服务器：
```yaml
env YML=path/to/yml python -m xiyan-mcp-server
```

### 3.2 从 Smithery.ai 安装
查看 [@XGenerationLab/xiyan_mcp_server](https://smithery.ai/server/@XGenerationLab/xiyan_mcp_server)

未进行全面测试。

## 4. 配置

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

### 4.1 关于 LLM
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
最后，我们推荐使用 XiYanSQL-qwencoder-32B (https://github.com/XGenerationLab/XiYanSQL-QwenCoder)，这是文本到 SQL 的 SOTA 模型，而且我们将其开源了。
我们将模型部署在 DashScope 上，因此您需要设置以下环境变量：
请联系我们以获取 ``key``。( godot.lzl@alibaba-inc.com )


```yaml
model:
  name: "pre-xiyan_multi_dialect_v3"
  key: "KEY"
  url: "https://poc-dashscope.aliyuncs.com/compatible-mode/v1"
database:
```

当然你也可以自己部署XiYanSQL-qwencoder-32B在任何有足够GPU配置的机器上，并以openai sdk的方式对外提供服务，就可以接入本MCP server

#### 本地 LLM
未来将支持。

### 4.2 关于数据库
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

## 5. 引用
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