<h1 align="center">XiYan MCP Server</h1>
<p align="center">
  <a href="https://github.com/XGenerationLab/XiYan-SQL"><img alt="MCP Playwright" src="https://raw.githubusercontent.com/XGenerationLab/XiYan-SQL/main/xiyanGBI.png" height="60"/></a>
</p>
<p align="center">
  <b>一个模型上下文协议 (MCP) 服务器，支持自然语言查询数据库</b></br>
  <sub>由 <a href="https://github.com/XGenerationLab/XiYan-SQL">XiYan-SQL</a> 提供支持，Test-to-SQL公开基准上的SOTA</sub>
</p>

<p align="center">
💻 <a href="https://github.com/XGenerationLab/xiyan_mcp_server">XiYan-mcp-server</a> | 
🌐 <a href="https://github.com/XGenerationLab/XiYan-SQL">XiYan-SQL</a> |
📖 <a href="https://arxiv.org/abs/2411.08599"> Arxiv</a> | 
📄 <a href="https://paperswithcode.com/paper/xiyan-sql-a-multi-generator-ensemble">PapersWithCode</a> |
💻 <a href="https://huggingface.co/collections/XGenerationLab/xiyansql-models-67c9844307b49f87436808fc">HuggingFace</a> |
🤖 <a href="https://modelscope.cn/collections/XiYanSQL-Models-4483337b614241">ModelScope</a> |
🌕 <a href="https://bailian.console.aliyun.com/xiyan">析言GBI</a> 
<br />
<a href="https://pepy.tech/projects/xiyan-mcp-server"><img src="https://static.pepy.tech/badge/xiyan-mcp-server" alt="PyPI 下载量"></a>
  <a href="https://smithery.ai/server/@XGenerationLab/xiyan_mcp_server"><img alt="Smithery 安装量" src="https://smithery.ai/badge/@XGenerationLab/xiyan_mcp_server" height="20"/></a>
<a href="https://github.com/XGenerationLab/xiyan_mcp_server" target="_blank">
    <img src="https://img.shields.io/github/stars/XGenerationLab/xiyan_mcp_server?style=social" alt="GitHub stars" />
</a>
<br />
<a href="https://github.com/XGenerationLab/xiyan_mcp_server">English</a> | <a href="https://github.com/XGenerationLab/xiyan_mcp_server/blob/main/README_zh.md"> 中文 </a><br />
<a href="https://github.com/XGenerationLab/xiyan_mcp_server/blob/main/imgs/dinggroup_out.png">钉钉群</a>｜ 
<a href="https://weibo.com/u/2540915670" target="_blank">在微博上关注我</a>
</p>

## 目录

- [功能](#features)
- [工具预览](#tool-preview)
- [安装](#installation)
  - [通过 pip 安装](#installing-from-pip)
  - [通过 Smithery.ai 安装](#installing-from-smitheryai)
- [配置](#configuration)
  - [LLM 配置](#llm-configuration)
    - [通用 LLM](#general-llms)
    - [文本到 SQL SOTA 模型](#text-to-sql-sota-model)
    - [本地 LLM](#local-llms)
  - [数据库配置](#database-configuration)
- [启动](#launch)
  - [Claude 桌面](#claude-desktop)
  - [Goose](#goose)
- [引用](#citation)

## 功能
- 🌐 通过 [XiYanSQL](https://github.com/XGenerationLab/XiYan-SQL) 以自然语言提取数据
- 🖱️ 列出可用的 MySQL 表作为资源
- 🔧 读取表内容

## 工具预览
 - 工具 ``get_data_via_natural_language`` 提供从数据库检索数据的自然语言接口。该服务器将输入的自然语言转换为 SQL，并调用数据库返回查询结果。

 - ``mysql://{table_name}`` 资源允许在指定特定的表名时，从数据库获取一部分样本数据以供模型参考。
- ``mysql://`` 资源将列出当前数据库的名称

## 安装
### 通过 pip 安装

需要 Python 3.11 及以上版本。
您可以通过 pip 安装服务器，它将安装最新版本。

```bash
pip install xiyan-mcp-server
```

之后您可以直接运行服务器：
```bash
python -m xiyan_mcp_server
```
但是在您完成后续配置之前，它不会提供任何功能。
您将获得一个 yml 文件。之后您可以通过以下命令运行服务器：
```yaml
env YML=path/to/yml python -m xiyan_mcp_server
```

### 通过 Smithery.ai 安装
请参见 [@XGenerationLab/xiyan_mcp_server](https://smithery.ai/server/@XGenerationLab/xiyan_mcp_server)

尚未全面测试。

## 配置

您需要一个 yml 配置文件来配置服务器。
在 config_demo.yml 中提供了一个默认配置文件，内容如下：

```yaml
model:
  name: "pre-xiyansql-qwencoder-32b"
  key: ""
  url: "https://pre-xiyan-stream.biz.aliyun.com/service/api/xiyan-sql"

database:
  host: "localhost"
  port: 3306
  user: "root"
  password: ""
  database: ""
```

### LLM 配置
``Name`` 是要使用的模型的名称，``key`` 是模型的 API 密钥，``url`` 是模型的 API 地址。我们支持以下模型。
#### 通用 LLM
如果您想使用通用 LLM，比如 gpt3.5，您可以直接配置如下：
```yaml
model:
  name: "gpt-3.5-turbo"
  key: "您的密钥"
  url: "https://api.openai.com/v1"
database:
```

如果您想使用阿里巴巴的 Qwen，例如 Qwen-max，您可以使用以下配置。
```yaml
model:
  name: "qwen-max"
  key: "您的密钥"
  url: "https://dashscope.aliyuncs.com/compatible-mode/v1"
database:
```
#### 文本到 SQL SOTA 模型
最后，我们推荐使用 XiYanSQL-qwencoder-32B (https://github.com/XGenerationLab/XiYanSQL-QwenCoder)，这是文本到 SQL 的 SOTA 模型，见 [Bird benchmark](https://bird-bench.github.io/)。
我们在阿里云 DashScope 上部署了该模型，因此您需要设置以下环境变量：
请发送您的电子邮件以获取 ``key``。 ( godot.lzl@alibaba-inc.com )
在电子邮件中，请附上以下信息：
```yaml
name: "您的姓名",
email: "您的电子邮件",
organization: "您所在的学校或公司或组织"
```
我们将根据您的电子邮件发送给您一个 ``key``。您可以将该 ``key`` 填写在 yml 文件中。
该 ``key`` 将在一个月或 200 查询或其他法律限制下过期。

```yaml
model:
  name: "pre-xiyansql-qwencoder-32b"
  key: "密钥"
  url: "https://pre-xiyan-stream.biz.aliyun.com/service/api/xiyan-sql"
database:
```

注意：该模型服务仅供试用，如果您需要在生产环境中使用，请与我们联系。

或者，您也可以在自己的服务器上部署模型 [XiYanSQL-qwencoder-32B](https://github.com/XGenerationLab/XiYanSQL-QwenCoder)。

#### 本地 LLM
未来将支持。

### 数据库配置
``host``, ``port``, ``user``, ``password``, ``database`` 是 MySQL 数据库的连接信息。

您可以使用本地或任何远程数据库。现在我们支持 MySQL（更多方言将在不久的将来支持）。

```yaml
database:
  host: "localhost"
  port: 3306
  user: "root"
  password: ""
  database: ""
```

## 启动
### Claude 桌面
在您的 Claude 桌面配置文件中添加以下内容：
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
### Goose
在配置中添加以下命令。

```yaml
env YML=path/to/yml python -m xiyan_mcp_server
```

## 引用
如果您觉得我们的工作对您有帮助，请随时引用我们。
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