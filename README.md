<h1 align="center">XiYan MCP Server</h1>
<p align="center">
  <a href="https://github.com/XGenerationLab/XiYan-SQL"><img alt="MCP Playwright" src="https://raw.githubusercontent.com/XGenerationLab/XiYan-SQL/main/xiyanGBI.png" height="60"/></a>
</p>
<p align="center">
  <b>A Model Context Protocol (MCP) server that enables natural language queries to databases</b></br>
  <sub>powered by <a href="https://github.com/XGenerationLab/XiYan-SQL" >XiYan-SQL</a>, SOTA of text-to-sql on open benchmarks</sub>
</p>

<p align="center">
💻 <a href="https://github.com/XGenerationLab/xiyan_mcp_server" >XiYan-mcp-server</a> | 
🌐 <a href="https://github.com/XGenerationLab/https://github.com/XGenerationLab/XiYan-SQL" >XiYan-SQL</a> |
📖 <a href="https://arxiv.org/abs/2411.08599"> Arxiv</a> | 
📄 <a href="https://paperswithcode.com/paper/xiyan-sql-a-multi-generator-ensemble" >PapersWithCode</a>
💻 <a href="https://huggingface.co/collections/XGenerationLab/xiyansql-models-67c9844307b49f87436808fc">HuggingFace</a> |
🤖 <a href="https://modelscope.cn/collections/XiYanSQL-Models-4483337b614241" >ModelScope</a> |
🌕 <a href="https://bailian.console.aliyun.com/xiyan">析言GBI</a> 
<br />
<a href="https://pepy.tech/projects/xiyan-mcp-server"><img src="https://static.pepy.tech/badge/xiyan-mcp-server" alt="PyPI Downloads"></a>
  <a href="https://smithery.ai/server/@XGenerationLab/xiyan_mcp_server"><img alt="Smithery Installs" src="https://smithery.ai/badge/@XGenerationLab/xiyan_mcp_server" height="20"/></a>
<a href="https://github.com/XGenerationLab/xiyan_mcp_server" target="_blank">
    <img src="https://img.shields.io/github/stars/XGenerationLab/xiyan_mcp_server?style=social" alt="GitHub stars" />
</a>
<br />
<a href="https://github.com/XGenerationLab/xiyan_mcp_server" >English</a> | <a href="https://github.com/XGenerationLab/xiyan_mcp_server/blob/main/README_zh.md"> 中文 </a><br />
<a href="https://github.com/XGenerationLab/xiyan_mcp_server/blob/main/imgs/dinggroup_out.png">Ding Group钉钉群</a>｜ 
<a href="https://weibo.com/u/2540915670" target="_blank">Follow me on Weibo</a>
</p>


## Table of Contents

- [Features](#features)
- [Tool Preview](#tool-preview)
- [Installation](#installation)
  - [Installing from pip](#installing-from-pip)
  - [Installing from Smithery.ai](#installing-from-smitheryai)
- [Configuration](#configuration)
  - [LLM Configuration](#llm-configuration)
    - [General LLMs](#general-llms)
    - [Text-to-SQL SOTA model](#text-to-sql-sota-model)
    - [Local LLMs](#local-llms)
  - [Database Configuration](#database-configuration)
- [Launch](#launch)
  - [Claude Desktop](#claude-desktop)
  - [Goose](#goose)
- [Citation](#citation)


## Features
- 🌐 Fetch data by natural language through [XiYanSQL](https://github.com/XGenerationLab/XiYan-SQL)
- 🖱️ List available MySQL tables as resources
- 🔧 Read table contents

## Tool Preview
 - The tool ``get_data_via_natural_language`` provides a natural language interface for retrieving data from a database. This server will convert the input natural language into SQL using a built-in model and call the database to return the query results.

 - The ``mysql://{table_name}`` resource allows obtaining a portion of sample data from the database for model reference when a specific table_name is specified.
- The ``mysql://`` resource will list the names of the current databases

## Installation
### Installing from pip

Python 3.11+ is required. 
you can install the server through pip, and it will install the latest verion

```bash
pip install xiyan-mcp-server
```

After that you can directly run the server by:
```bash
python -m xiyan_mcp_server
```
But it does not provide any functions until you complete following config.
You will get a yml file. After that you can run the server by:
```yaml
env YML=path/to/yml python -m xiyan_mcp_server
```

### Installing from Smithery.ai
See [@XGenerationLab/xiyan_mcp_server](https://smithery.ai/server/@XGenerationLab/xiyan_mcp_server)

Not fully tested.

## Configuration

You need a yml config file to configure the server.
a default config file is provided in config_demo.yml which looks like this:

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

### LLM Configuration
``Name`` is the name of the model to use, ``key`` is the API key of the model, ``url`` is the API url of the model. We support following models.
#### general LLMs
if you want to use the general LLMs, e.g. gpt3.5, you can directly config like this:
```yaml
model:
  name: "gpt-3.5-turbo"
  key: "YOUR KEY "
  url: "https://api.openai.com/v1"
database:
```

if you want to use Qwen from alibaba, e.g. Qwen-max, you can use following config.
```yaml
model:
  name: "qwen-max"
  key: "YOUR KEY "
  url: "https://dashscope.aliyuncs.com/compatible-mode/v1"
database:
```
#### Text-to-SQL SOTA model
Last, we recommend the XiYanSQL-qwencoder-32B (https://github.com/XGenerationLab/XiYanSQL-QwenCoder), which is the SOTA model in text-to-sql, see [Bird benchmark](https://bird-bench.github.io/).
We deployed the model on Alibaba Cloud DashScope, so you need to set the following environment variables:
Send me your email to get the ``key``. ( godot.lzl@alibaba-inc.com )
In the email, please attach the following information:
```yaml
name: "YOUR NAME",
email: "YOUR EMAIL",
organization: "your college or Company or Organization"
```
We will send you a ``key`` according to your email. And you can fill the ``key`` in the yml file.
The ``key`` will be expired by  1 month or 200 queries or other legal restrictions.


```yaml
model:
  name: "pre-xiyansql-qwencoder-32b"
  key: "KEY"
  url: "https://pre-xiyan-stream.biz.aliyun.com/service/api/xiyan-sql"
database:
```

Note: this model service is just for trial, if you need to use it in production, please contact us.

Alternatively, you can also deploy the model [XiYanSQL-qwencoder-32B](https://github.com/XGenerationLab/XiYanSQL-QwenCoder) on your own server.

#### Local LLMs
To support in the future.

### Database Configuration
``host``, ``port``, ``user``, ``password``, ``database`` are the connection information of the MySQL database.

You can use local or any remote databases. Now we support MySQL (more dialects soon).


```yaml
database:
  host: "localhost"
  port: 3306
  user: "root"
  password: ""
  database: ""
```

## Launch
### Claude desktop
Add this in your claude desktop config file
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
Add following command in the config.

```yaml
env YML=path/to/yml python -m xiyan_mcp_server
```


## Citation
If you find our work helpful, feel free to give us a cite.
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


