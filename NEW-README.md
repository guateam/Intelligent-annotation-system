# INTELLIGENT-ANNOTATION-SYSTEM

课外阅读智能批注系统

## Table of Contents 目录

   * [INTELLIGENT-ANNOTATION-SYSTEM](#intelligent-annotation-system)
      * [Table of Contents 目录](#table-of-contents-目录)
      * [Process 开发进度表](#process-开发进度表)
      * [Server 服务端](#server-服务端)
         * [Environment 开发环境](#environment-开发环境)
         * [API 接口](#api-接口)
            * [Design 设计思路](#design-设计思路)
            * [Format 格式约定](#format-格式约定)
            * [Document 文档](#document-文档)
               * [Account 账户](#account-账户)
               * [Reading 读书](#reading-读书)
               * [User 用户](#user-用户)
               * [Information 信息](#information-信息)
               * [Other 杂项](#other-杂项)
         * [Database 数据库](#database-数据库)
            * [Design 设计思路](#design-设计思路-1)
            * [Structure 结构](#structure-结构)
      * [WEB-APP 网页应用](#web-app-网页应用)
         * [Environment 开发环境](#environment-开发环境-1)
         * [Page&amp;Function 页面和功能](#pagefunction-页面和功能)
            * [Design 设计思路](#design-设计思路-2)
            * [Draft 设计稿](#draft-设计稿)
            * [交互逻辑](#交互逻辑)
      * [移动应用](#移动应用)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)

## Process 开发进度表

2018-10-08

----

<table>
    <tr>
        <td rowspan="2"><strong>服务端</strong></td>
        <td><strong>接口</strong></td>
        <td>书籍推荐</td>
        <td>热门文章</td>
        <td>优秀批注</td>
        <td>热门分类</td>
        <td>优秀学生</td>
        <td>优秀老师</td>
    </tr>
    <tr>
        <td><strong>核心算法</strong></td>
        <td>解决代理的问题</td>
        <td>重构CNN网络</td>
        <td colspan="2">对运行接口做高层抽象，方便其他项目调用</td>
        <td colspan="2">尝试对样本分词，看看能不能提高训练效率</td>
    </tr>
    <tr>
        <td rowspan="2"><strong>网页应用</strong></td>
        <td><strong>设计</strong></td>
        <td colspan="3">登陆页面</td>
        <td colspan="3">注册页面</td>
    </tr>
    <tr>
        <td><strong>制作</strong></td>
        <td>登陆页面</td>
        <td>注册页面</td>
        <td>Search</td>
        <td colspan="2">和服务端对接</td>
        <td>修改样式</td>
    </tr>
    <tr>
        <td colspan="2"><strong>数据库</strong></td>
        <td colspan="2">填入若干用于测试的内容</td>
        <td colspan="2">批注需要添加字段来表示权重，用于排序</td>
        <td colspan="2">用户表添加字段存储用户画像向量</td>
    </tr>
</table>


2018-09-24 √

----

<table>
    <tr>
        <td rowspan="2"><strong>服务端</strong></td>
        <td><strong>接口</strong></td>
        <td colspan="2">登陆 √</td>
        <td colspan="2">注册 √</td>
    </tr>
    <tr>
        <td><strong>核心算法</strong></td>
        <td colspan="4">基于CNN的长句分类DEMO √</td>
    </tr>
    <tr>
        <td rowspan="2"><strong>网页应用</strong></td>
        <td><strong>设计</strong></td>
        <td colspan="2">首页 √</td>
        <td colspan="2">书籍详情页 √</td>
    </tr>
    <tr>
        <td><strong>制作</strong></td>
        <td>首页 √</td>
        <td>书籍详情页 √</td>
        <td>完成基本的路由配置 √</td>
        <td>抽象出部分组件等待复用 √</td>
    </tr>
</table>


## Server 服务端

### Environment 开发环境

```shell
Language:
	Python3.6
Virtual Environment:
	$ python -m venv venv       # 创建python虚拟环境
	$ source venv/bin/activate  # 进入虚拟环境
	$ deactivate                # 退出虚拟环境
Packages:
    Flask==1.0.2
    jieba==0.39
    numpy==1.14.5
    PyMySQL==0.9.2
    pyquery==1.4.0
    redis==2.10.6
    requests==2.19.1
    scipy==1.1.0
    sklearn==0.0
    tensorboard==1.10.0
    tensorflow==1.10.1
```

### API 接口

#### Design 设计思路

暂无

#### Format 格式约定

```python
Type:
	json
Format:
	{
        code: ,  # 操作状态码
        msg: ,   # 错误提示
        data: ,  # 返回数据
	}
```

#### Document 文档

##### Account 账户

1. 用户登录

    - 接口 `/api/account/login()`

    - 参数 `username`-用户名 `password`-密码

    - 返回值

      ```python
      {
          code: ,       # 0=未知用户 -1=未成功初始化token 1=成功
          msg: ,        # 信息
          data: {
              token: ,  # 用户标识
              group: ,  # 用户群组
          }
      }
      ```

2. 用户登出

    - 接口 `/api/account/logout()`

    - 参数 `token`-用户标识

    - 返回值

      ```python
      {
          code: ,  # 0=未知用户 1=成功
          msg: ,   # 信息
      }
      ```

3. 用户注册

    - 接口 `/api/account/signup()`

    - 参数 `username`-用户名 `password`-密码 `phone`-手机号 `email`-电子邮箱 `nickname`-昵称 `group`-用户组

    - 返回值

      ```python
      {
          code: ,  # 0=用户名已存在 -1=EMail已存在 -2=手机号已存在 -3=未知错误 1=成功
          msg: ,   # 信息
      }
      ```

4. 用户名检测

    - 接口 `/api/account/check_username_available()`

    - 参数 `username`-用户名

    - 返回值

      ```python
      {
          code: ,  # 0=不可用 1=可用
          msg: ,   # 信息
      }
      ```

5. 手机号检测

    - 接口 `/api/account/check_phone_available()`

    - 参数 `phone`-手机号

    - 返回值

      ```python
      {
          code: ,  # 0=不可用 1=可用
          msg: ,   # 信息
      }
      ```

6. 邮箱检测

    - 接口 `/api/account/check_email_available()`

    - 参数 `email`-邮箱

    - 返回值

      ```python
      {
          code: ,  # 0=不可用 1=可用
          msg: ,   # 信息
      }
      ```

##### Reading 读书

1. 通过书籍ID获取书籍详情

   - 接口 `/api/reading/get_book_info()`

   - 参数 `id`-文章id

   - 返回值

     ```python
     {
         code: ,           # 0=未知书籍 1=成功
         msg: ,            # 信息
         data: {
             id: ,         # 文章id
             title: ,      # 文章标题
             file_path: ,  # 文章内容地址
             uploader: ,   # 上传人
             state: ,      # 文章状态 0=未审核 1=已审核 -1=未通过审核或下架
             date: ,       # 文章上传日期
         }
     }
     ```

2. 首页文章推荐

   - 接口 `/api/reading/article_recommend()`

   - 参数 `token`-用户token

   - 返回值

     ```python
     {
         code: ,                     # 0=未知用户 1=成为
         msg: ,                      # 信息
         data: {
             [
                 {
                     id: ,           # 文章id
                     title: ,        # 文章标题
                     file_path: ,    # 文章内容地址
                     uploader: ,     # 上传人
                     date: ,         # 文章上传日期
                     cover: ,        # 封面
                     author: ,       # 作者
                     num_comment: ,  # 评论数
                     like: ,         # 点赞数
                 },
                 ...
             ]                       # 文章数组
         }
     }
     ```

3. 首页优秀批注推荐

   - 接口 `/api/reading/comment_recommend()`

   - 参数 `token`-用户token

   - 返回值

     ```python
     {
         code: ,                          # 0=未知用户 1=成为
         msg: ,                           # 信息
         data: {
             [
                 {
                     id: ,                # 批注id
                     book_id: ,           # 文章id
                     book_name: ,         # 文章标题
                     comment: ,           # 批注内容
                     comment_uploader: ,  # 批注上传人
                     comment_sentence: ,  # 批注目标段落
                     num_comment: ,       # 评论数
                     like: ,              # 点赞数
                 },
                 ...
             ]                            # 批注数组
         }
     }
     ```

4. 首页热门分类

   - 接口 `/api/reading/tag_recommend()`

   - 参数 `token`-用户token

   - 返回值

     ```python
     {
         code: ,              # 0=未知用户 1=成功
         msg: ,               # 信息
         data: {
             [
                 {
                     id: ,    # Tag ID
                     name: ,  # 分类名称
                 },
                 ...
             ]                # 分类数组
         }
     }
     ```

##### User 用户

1. 首页推荐老师

   - 接口 `/api/user/teacher_recommend()`

   - 参数 `token`-用户token

   - 返回值

     ```python
     {
         code: ,                   # 0=未知用户 1=成功
         msg: ,                    # 信息
         data: {
             [
                 {
                     id: ,         # 用户id
                     name: ,       # 用户昵称
                     school: ,     # 来自学校
                     introduce: ,  # 简介
                 },
                 ...
             ]                     # 老师列表
         }
     }
     ```

2. 首页推荐学生

   - 接口 `/api/user/student_recommend()`

   - 参数 `token`-用户token

   - 返回值

     ```python
     {
         code: ,                   # 0=未知用户 1=成功
         msg: ,                    # 信息
         data: {
             [
                 {
                     id: ,         # 用户id
                     name: ,       # 用户昵称
                     school: ,     # 来自学校
                     introduce: ,  # 简介
                 },
                 ...
             ]                     # 学生列表
         }
     }
     ```

##### Information 信息

1. 通知信息

   - 接口

   - 参数 `token`-用户token

   - 返回值

     ```python
     {
         code: ,  # 0=未知用户 1=成功
         msg: ,   # 信息
         data: {
             [
                 {
                     # 待定
                 },
                 ...
             ]
         }
     }
     ```


##### Other 杂项

1. Ping

   - 接口 `/api/check_server()`

   - 参数 `None`

   - 返回值

     ```python
     {
         code: ,  # 1=成功
         msg: ,   # 信息
     }
     ```

### Database 数据库

#### Design 设计思路

#### Structure 结构

IntelligentAnnotationSystem.article

| Field      | Type         | Null | Key  | Default           | Extra          | Comments       |
| ---------- | ------------ | ---- | ---- | ----------------- | -------------- | -------------- |
| id         | int(11)      | NO   | PRI  | NULL              | auto_increment | 文章id         |
| title      | varchar(45)  | NO   |      | NULL              |                | 文章标题       |
| author     | varchar(20)  | NO   |      | 未知作者          |                | 文章作者       |
| image_path | varchar(200) | YES  |      | NULL              |                | 标题图片的路径 |
| file_path  | varchar(200) | NO   |      | NULL              |                | 文章内容的路径 |
| uploader   | int(11)      | NO   |      | NULL              |                | 上传人         |
| state      | int(11)      | NO   |      | NULL              |                | 审核状态       |
| date       | timestamp    | NO   |      | CURRENT_TIMESTAMP |                | 上传时间       |

IntelligentAnnotationSystem.article_tag

| Field      | Type        | Null | Key  | Default | Extra          | Comments |
| ---------- | ----------- | ---- | ---- | ------- | -------------- | -------- |
| id         | int(11)     | NO   | PRI  | NULL    | auto_increment | id       |
| article_id | int(11)     | NO   | MUL  | NULL    |                | 文章id   |
| tag        | varchar(20) | NO   |      | NULL    |                | Tag      |

IntelligentAnnotationSystem.comments

| Field          | Type      | Null | Key  | Default           | Extra          | Comments     |
| -------------- | --------- | ---- | ---- | ----------------- | -------------- | ------------ |
| id             | int(11)   | NO   | PRI  | NULL              | auto_increment | 批注id       |
| article_id     | int(11)   | NO   | MUL  | NULL              |                | 文章id       |
| user_id        | int(11)   | NO   | MUL  | NULL              |                | 批注人id     |
| paragraph      | int(11)   | NO   |      | NULL              |                | 自然段       |
| start_index    | int(11)   | NO   |      | NULL              |                | 开始索引     |
| end_index      | int(11)   | NO   |      | NULL              |                | 结束索引     |
| type           | int(11)   | NO   |      | NULL              |                | 批注类型     |
| text           | text      | YES  |      | NULL              |                | 文字批注内容 |
| disagree_count | int(11)   | NO   |      | 0                 |                | 反对数       |
| date           | timestamp | NO   |      | CURRENT_TIMESTAMP |                | 批注时间     |
| agree_count    | int(11)   | NO   |      | 0                 |                | 赞同数       |

IntelligentAnnotationSystem.user

| Field    | Type         | Null | Key  | Default           | Extra          | Comments                      |
| -------- | ------------ | ---- | ---- | ----------------- | -------------- | ----------------------------- |
| id       | int(11)      | NO   | PRI  | NULL              | auto_increment | 用户id                        |
| username | varchar(20)  | NO   |      | NULL              |                | 用户名                        |
| email    | varchar(45)  | YES  |      | NULL              |                | 邮箱                          |
| phone    | varchar(20)  | YES  |      | NULL              |                | 手机                          |
| password | varchar(200) | NO   |      | NULL              |                | 密码                          |
| nickname | varchar(45)  | YES  |      | NULL              |                | 昵称                          |
| token    | varchar(25)  | YES  |      | NULL              |                | TOKEN                         |
| group    | int(11)      | NO   |      | NULL              |                | 用户组 1=管理员 2=教师 3=学生 |
| date     | timestamp    | NO   |      | CURRENT_TIMESTAMP |                | 注册时间                      |


## WEB-APP 网页应用

### Environment 开发环境

### Page&Function 页面和功能

#### Design 设计思路

#### Draft 设计稿

#### 交互逻辑


## 移动应用

暂无