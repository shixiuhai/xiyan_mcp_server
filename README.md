
[💻 XiYan-mcp-server](https://github.com/XGenerationLab/xiyan_mcp_server) | 
[💻 XiYan-SQL](https://github.com/XGenerationLab/XiYan-SQL) |
[📖 Arxiv](https://arxiv.org/abs/2411.08599)| 
[📄 PapersWithCode](https://paperswithcode.com/paper/xiyan-sql-a-multi-generator-ensemble)

[![smithery badge](https://smithery.ai/badge/@XGenerationLab/xiyan_mcp_server)](https://smithery.ai/server/@XGenerationLab/xiyan_mcp_server)

[English](https://github.com/XGenerationLab/xiyan_mcp_server)  | [中文](https://github.com/XGenerationLab/xiyan_mcp_server/blob/main/README_zh.md)


# XiYan MCP Server


A Model Context Protocol (MCP) server that enables natural language queries to databases, powered by [XiYanSQL](https://github.com/XGenerationLab/XiYan-SQL) as text-to-sql technique (SOTA of text-to-sql open benchmarks).

We support MySQL database now and more dialects are coming soon.

## 1. Features
- Fetch data by natural language through [XiYanSQL](https://github.com/XGenerationLab/XiYan-SQL)
- List available MySQL tables as resources
- Read table contents

## 2. Tool Preview
 - The tool ``get_data_via_natural_language`` provides a natural language interface for retrieving data from a database. This server will convert the input natural language into SQL using a built-in model and call the database to return the query results.

 - The ``mysql://{table_name}`` resource allows obtaining a portion of sample data from the database for model reference when a specific table_name is specified.
- The ``mysql://`` resource will list the names of the current databases

## 3. Installation
### 3.1 Install from pip

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


### 3.2 Install from Smithery.ai
See [@XGenerationLab/xiyan_mcp_server](https://smithery.ai/server/@XGenerationLab/xiyan_mcp_server)

Not fully tested.

## 4. Configuration

You need a yml config file to configure the server.
a default config file is provided in config_demo.yml which looks like this:

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

### 4.1 About LLM
``Name`` is the name of the model to use, ``key`` is the API key of the model, ``url`` is the API url of the model. We support following models.
#### Using general LLMs
if you want to use the general LLMs, e.g. gpt3.5, you can directly config like this:
```yaml
model:
  name: "gpt-3.5-turbo"
  key: "YOUR KEY "
  url: "https://api.openai.com/v1/chat/completions"
database:
```

if you want to use Qwen from alibaba, e.g. Qwen-max,
```yaml
model:
  name: "qwen-max"
  key: "YOUR KEY "
  url: "https://dashscope.aliyuncs.com/compatible-mode/v1"
database:
```
#### Using Text-to-SQL SOTA model
Last, we recommend the XiYanSQL-qwencoder-32B (https://github.com/XGenerationLab/XiYanSQL-QwenCoder), which is the SOTA model in text-to-sql.
We deployed the model on Alibaba Cloud DashScope, so you need to set the following environment variables:
Contact us to get the ``key``. ( godot.lzl@alibaba-inc.com )
```yaml
model:
  name: "pre-xiyan_multi_dialect_v3"
  key: "KEY"
  url: "https://poc-dashscope.aliyuncs.com/compatible-mode/v1"
database:
```

Alternatively, you can also deploy the model (XiYanSQL-qwencoder-32B) on your own server.

#### Local LLMs
To support in the future.

### 4.2 About the database
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


## 5. Citation
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


