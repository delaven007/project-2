"""用户可以登录和注册
1.确定并发方案，确定套接字，具体细节和需求分析
*Process多进程  tcp套接字
*注册后直接进入二级界面，历史记录最近10个

2.使用dict -->words
用户表：id   name   passwd
create table user (id int primary key auto_increment,name varchar(32) not null ,passwd varchar(128) not null);

历史记录表：id name   word   time
 create table hist (id int primary key auto_increment,name varchar(32) not null,word varchar(32) not null,time datetime default now());

3.结构设计，如何封装，客户端服务端工作流程
 *客户端（发请求，展示结果）
 *服务端（逻辑操作，解决请求）
 *数据库服务端（操作数据库）

界面处理：
        while True：
            界面1

            while True:
                界面2

4.功能模块划分

   *网络搭建
   *注册
   *登录
   *查单词
   *历史记录


* 登录凭借用户名和密码登录
* 注册要求用户必须填写用户名,密码,其他内容自定
* 用户名要求不能重复
* 要求用户信息能够长期保存
可以通过基本的图形界面print以提示客户端输入。
* 程序分为服务端和客户端两部分
* 客户端通过print打印简单界面输入命令发起请求
* 服务端主要负责逻辑数据处理
* 启动服务端后应该能满足多个客户端同时操作
客户端启动后即进入一级界面,包含如下功能:登录 注册 退出
* 退出后即退出该软件
* 登录成功即进入二级界面,失败回到一级界面
* 注册成功可以回到一级界面继续登录,也可以直接用注册用户进入二级界面
用户登录后进入二级界面,功能如下:查单词 历史记录 注销
file:///C:/Users/lvze/Desktop/6%E9%A1%B9%E7%9B%AE%E7%BB%BC%E5%90%88/project.html
12/142019/5/26
project
* 选择注销则回到一级界面
* 查单词:循环输入单词,得到单词解释,输入特殊符号退出单词查询状态
* 历史记录:查询当前用户的查词记录,要求记录包含name
word
time。可以查看所有记录或者前10条均可。
单词本说明
每个单词一定占一行
单词按照从小到大顺序排列
单词和解释之间一定有空格
查词说明
直接使用单词本查询(文本操作)
先将单词存入数据库,然后通过数据库查询。(数据库操作)

"""