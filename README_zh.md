<h1 align="center">XiYan MCP 服务器</h1>
<p align="center">
  <a href="https://github.com/XGenerationLab/XiYan-SQL"><img alt="MCP Playwright" src="https://raw.githubusercontent.com/XGenerationLab/XiYan-SQL/main/xiyanGBI.png" height="60"/></a>
</p>
<p align="center">
  <b>一个允许自然语言查询数据库的模型上下文协议 (MCP) 服务器</b></br>
  <sub>基于 <a href="https://github.com/XGenerationLab/XiYan-SQL">XiYan-SQL</a>，在开放基准上达到文本到 SQL 的最新技术水平</sub>
</p>

<p align="center">
💻 <a href="https://github.com/XGenerationLab/xiyan_mcp_server">XiYan-mcp-server</a> | 
🌐 <a href="https://github.com/XGenerationLab/https://github.com/XGenerationLab/XiYan-SQL">XiYan-SQL</a> |
📖 <a href="https://arxiv.org/abs/2411.08599"> Arxiv</a> | 
📄 <a href="https://paperswithcode.com/paper/xiyan-sql-a-multi-generator-ensemble">PapersWithCode</a> |
💻 <a href="https://huggingface.co/collections/XGenerationLab/xiyansql-models-67c9844307b49f87436808fc">HuggingFace</a> |
🤖 <a href="https://modelscope.cn/collections/XiYanSQL-Models-4483337b614241">ModelScope</a> |
🌕 <a href="https://bailian.console.aliyun.com/xiyan">析言GBI</a> 
<br />
<a href="https://opensource.org/licenses/Apache-2.0">
  <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License: Apache 2.0" />
</a>
<a href="https://pepy.tech/projects/xiyan-mcp-server"><img src="https://static.pepy.tech/badge/xiyan-mcp-server" alt="PyPI 下载量"></a>
<a href="https://smithery.ai/server/@XGenerationLab/xiyan_mcp_server"><img alt="Smithery 安装次数" src="https://smithery.ai/badge/@XGenerationLab/xiyan_mcp_server" height="20"/></a>
<a href="https://github.com/XGenerationLab/xiyan_mcp_server" target="_blank">
    <img src="https://img.shields.io/github/stars/XGenerationLab/xiyan_mcp_server?style=social" alt="GitHub stars" />
</a>
<br />
<a href="https://github.com/XGenerationLab/xiyan_mcp_server">English</a> | <a href="https://github.com/XGenerationLab/xiyan_mcp_server/blob/main/README_zh.md">中文</a><br />
<a href="https://github.com/XGenerationLab/xiyan_mcp_server/blob/main/imgs/dinggroup_out.png">钉钉群</a>｜ 
<a href="https://weibo.com/u/2540915670" target="_blank">在微博关注我</a>
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
  - [Cline](#cline)
  - [Goose](#goose)
  - [Cursor](#cursor)
- [引用](#citation)

## 功能
- 🌐 通过 [XiYanSQL](https://github.com/XGenerationLab/XiYan-SQL) 以自然语言获取数据
- 🖱️ 列出可用的 MySQL 表作为资源
- 🔧 读取表内容

## 工具预览
- 工具 ``get_data_via_natural_language`` 提供了一个自然语言接口，用于从数据库中检索数据。该服务器将输入的自然语言转换为 SQL，使用内置模型并调用数据库返回查询结果。

- ``mysql://{table_name}`` 资源允许在指定特定表名时，从数据库获取部分示例数据以供模型参考。
- ``mysql://`` 资源将列出当前数据库的名称。

## 安装
### 通过 pip 安装

需要 Python 3.11 或更高版本。
您可以通过 pip 安装服务器，它将安装最新版本。

```bash
pip install xiyan-mcp-server
```

然后您可以直接运行服务器：
```bash
python -m xiyan_mcp_server
```
但在完成以下配置之前，它不提供任何功能。
您将获得一个 yml 文件。之后，您可以通过以下方式运行服务器：
```yaml
env YML=path/to/yml python -m xiyan_mcp_server
```

### 通过 Smithery.ai 安装
请参见 [@XGenerationLab/xiyan_mcp_server](https://smithery.ai/server/@XGenerationLab/xiyan_mcp_server)

未完全测试。

## 配置

您需要一个 yml 配置文件来配置服务器。
提供了一个默认配置文件 config_demo.yml，格式如下：

```yaml
model:
  name: "XGenerationLab/XiYanSQL-QwenCoder-32B-2412"
  key: ""
  url: "https://api-inference.modelscope.cn/v1/"

database:
  host: "localhost"
  port: 3306
  user: "root"
  password: ""
  database: ""
```

### LLM 配置
``Name`` 是要使用的模型名称， ``key`` 是该模型的 API 密钥， ``url`` 是该模型的 API 地址。我们支持以下模型。

| 版本 | 通用 LLM（GPT，qwenmax）                                             | Modelscope 的 SOTA 模型                   | Dashscope 的 SOTA 模型                                   | 
|----------|-------------------------------|--------------------------------------------|-----------------------------------------------------------|
| 描述 | 基本，易于使用 | 性能最佳，稳定，推荐 | 性能最佳，供试用                               |
| 名称     | 官方模型名称（例如 gpt-3.5-turbo，qwen-max）                 | XGenerationLab/XiYanSQL-QwenCoder-32B-2412 | xiyansql-qwencoder-32b                                    | 
| 密钥      | 服务提供商的 API 密钥（例如 OpenAI，阿里云）      | Modelscope 的 API 密钥                  | 通过邮件获得的 API 密钥                                     |
| url      | 服务提供商的端点（例如 "https://api.openai.com/v1"） | https://api-inference.modelscope.cn/v1/    | https://xiyan-stream.biz.aliyun.com/service/api/xiyan-sql |

#### 通用 LLM
如果您想使用通用 LLM，例如 gpt3.5，您可以直接配置如下：
```yaml
model:
  name: "gpt-3.5-turbo"
  key: "YOUR KEY"
  url: "https://api.openai.com/v1"
database:
```

如果您想使用来自阿里巴巴的 Qwen，例如 Qwen-max，您可以使用以下配置。
```yaml
model:
  name: "qwen-max"
  key: "YOUR KEY"
  url: "https://dashscope.aliyuncs.com/compatible-mode/v1"
database:
```

#### 文本到 SQL SOTA 模型
我们推荐 XiYanSQL-qwencoder-32B (https://github.com/XGenerationLab/XiYanSQL-QwenCoder)，这是文本到 SQL 的 SOTA 模型，参见 [Bird benchmark](https://bird-bench.github.io/)。
使用该模型有两种方式。您可以使用任一个。
(1) [Modelscope](https://www.modelscope.cn/models/XGenerationLab/XiYanSQL-QwenCoder-32B-2412)，(2) 阿里云 DashScope。

##### (1) Modelscope 版本
您需要从 Modelscope 申请 ``key`` 用于 API推断，网址：https://www.modelscope.cn/docs/model-service/API-Inference/intro。
然后可以使用以下配置：
```yaml
model:
  name: "XGenerationLab/XiYanSQL-QwenCoder-32B-2412"
  key: ""
  url: "https://api-inference.modelscope.cn/v1/"
```

阅读我们的 [模型描述](https://www.modelscope.cn/models/XGenerationLab/XiYanSQL-QwenCoder-32B-2412) 获取更多细节。

##### (2) Dashscope 版本

我们在阿里云 DashScope 上部署了该模型，因此您需要设置以下环境变量：
请发送您的电子邮件以获取 ``key``。 (godot.lzl@alibaba-inc.com)
在邮件中，请附上以下信息：
```yaml
name: "YOUR NAME",
email: "YOUR EMAIL",
organization: "您的学院或公司或组织"
```
我们将根据您的电子邮件发送给您一个 ``key``。您可以将 ``key`` 填入 yml 文件中。
该 ``key`` 将在 1 个月或 200 次查询或其他法律限制后过期。

```yaml
model:
  name: "xiyansql-qwencoder-32b"
  key: "KEY"
  url: "https://xiyan-stream.biz.aliyun.com/service/api/xiyan-sql"
database:
```

注意：该模型服务仅供试用，如果您需要在生产环境中使用，请与我们联系。

另外，您也可以在自己的服务器上部署 [XiYanSQL-qwencoder-32B](https://github.com/XGenerationLab/XiYanSQL-QwenCoder)。

#### 本地 LLM
将来支持。

### 数据库配置
``host``、``port``、``user``、``password``、``database`` 是 MySQL 数据库的连接信息。

您可以使用本地或任何远程数据库。现在我们支持 MySQL（更多方言即将推出）。

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
### Cline
准备与 [Claude 桌面](#claude-desktop) 类似的配置。

### Goose
在配置中添加以下命令：

```yaml
env YML=path/to/yml python -m xiyan_mcp_server
```

### Cursor
使用与 [Goose](#goose) 相同的命令。

## 引用
如果您发现我们的工作对您有帮助，请随时引用我们。
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