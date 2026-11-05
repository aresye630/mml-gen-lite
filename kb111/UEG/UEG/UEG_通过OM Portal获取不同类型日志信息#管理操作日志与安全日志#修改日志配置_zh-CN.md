---
id: ''
name: 修改日志配置
ne_type: UEG
type: feature
description: '* 系统默认安全审计日志存留期为90天，日志占用空间为200MB，系统每半小时周期性检查审计日志的存留期和占用空间，并删除超过设置的日志存留期和日志占用空间的最早的安全审计日志。 * 操作类操作日志和安全日志，超过日志占用空间后，优先老化一周前的次要级别日志；查询类操作日志，超过日志占用空间后，优先老化自动查询类的操作日志。 * 如果用户需要节省日志存储空间，或者为安全方面考虑，需要减少或增加日志的存留期限时可通过修改参数“日志存留期（天）”和“日志占用空间（MB）”更改日志配置。 * 当存储日志的时间超过“日志存留期（天）”或存储的日志大小超过“日志占用空间（MB）”，都会触发日志清理。 * 查询类操作日志老化阈值为固定值20000条。 * 此外，用户也可以通过下发MML命令**SET LOGCLEANPOLICY**设置日志老化策略。'
tags: []
risk_level: ''
doc_source: ["日常维护","UEG 基础运维操作（风筝S，虚机容器）","获取日志","通过OM Portal获取不同类型日志信息","管理操作日志与安全日志","修改日志配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
* 系统默认安全审计日志存留期为90天，日志占用空间为200MB，系统每半小时周期性检查审计日志的存留期和占用空间，并删除超过设置的日志存留期和日志占用空间的最早的安全审计日志。* 操作类操作日志和安全日志，超过日志占用空间后，优先老化一周前的次要级别日志；查询类操作日志，超过日志占用空间后，优先老化自动查询类的操作日志。* 如果用户需要节省日志存储空间，或者为安全方面考虑，需要减少或增加日志的存留期限时可通过修改参数“日志存留期（天）”和“日志占用空间（MB）”更改日志配置。* 当存储日志的时间超过“日志存留期（天）”或存储的日志大小超过“日志占用空间（MB）”，都会触发日志清理。* 查询类操作日志老化阈值为固定值20000条。* 此外，用户也可以通过下发MML命令**SET LOGCLEANPOLICY**设置日志老化策略。

## 必备事项
前提条件

* 已登录OM Portal。
* 操作员拥有安全管理员权限。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties: {}
  examples: {}
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 选择“安全 > 日志审计”，进入日志审计页面。

### 2 在左侧导航选择“日志配置”，在界面上修改“日志存留期（天）”。

#### 2.1 “日志存留期（天）”输入值必须在7~365之间，默认值为90（天）。

#### 2.2 “日志存留期（天）”修改后，系统会在下个每小时周期性检查时生效。

#### 2.3 系统判断日志是否达到存留期时，以“操作日志”、“安全日志”和“系统日志”中的“开始时间”为起始时间。

### 3 在“日志配置”界面修改“日志占用空间（MB）”并单击“应用”。

#### 3.1 “日志占用空间（MB）”输入值必须在120～1000之间，默认值为200（MB）。

#### 3.2 “日志占用空间（MB）”修改后，系统会在下个每小时周期性检查时生效。

#### 3.3 当日志占用空间超过设置值时，系统会在设置值下个周期生效时，删除超过设置值的时间最早的日志记录。

### 4 查看存储数据库。

#### 4.1 审计日志服务平稳运行后，用户可执行如下命令查看审计日志数据的存储。

##### 4.1.1 Windows操作系统通过“putty.exe”工具使用**mtuser**用户登录OMU；Linux操作系统通过终端模拟器使用**mtuser**用户登录OMU。

##### 仅在Fullstack虚机场景下涉及登录OMU操作，非Fullstack虚机场景请联系华为技术支持。

##### 维护接口IP地址获取方法为：

###### 4.1.1.1 执行MML命令**DSP NODE**，配置“网元ID”为“0”，查询并记录节点名称和节点IP（虚拟机类型为OMU的任一OMU节点）。

###### 4.1.1.2 执行MML命令**DSP NODERES**，配置“资源类型”为“PORT(网口)”，“节点名称”为“步骤1记录的节点名称”，查询“网口平面”为“Ext-OM”的IP地址，即为维护接口IP地址。

###### 如果“网口平面”没有“Ext-OM”，登录PaaSOM-1节点，执行ssh **mtuser**@*nodeIP*（步骤1查询到的节点IP），登录节点。PaaSOM-1节点IP地址可以从现网网设文档获取。

##### 4.1.2 执行**ssh mtuser@<*GaussDB所在节点IP*>**登录所在GaussDB节点。然后执行**su root**切换至root用户。

##### 4.1.3 通过**which docker**检查容器引擎类型，并进入GaussDB容器。

###### 4.1.3.1 如果存在docker可执行文件，如下命令所示。

###### PaaSOM-1:/home/mtuser # which docker

###### /usr/bin/docker

###### 执行**docker ps |grep gauss**获取GaussDB dockerId。

###### 执行**docker exec -it -u root *dockerId* sh**进入GaussDB容器。

###### 4.1.3.2 如果没有找到docker可执行文件，如下命令所示。

###### PaaSOM-1:/home/mtuser # which docker

###### which: no docker in (/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin)

###### 执行**crictl ps |grep gauss**获取GaussDB containerdID。

###### inipv6-csp-a-0:/home/mtuser # crictl ps |grep gauss

###### d7706d396a48a       registry.fusionstage.local:20202/csp/cspgaussdb_docker:23.0.0.B159                About an hour ago    Running             gauss-softwarecomp              0                   6c60ce978ec69

###### 执行**crictl inspect containerdID | grep "pid"**获取GaussDB容器实例的pid。

###### inipv6-csp-a-0:/home/mtuser # crictl inspect d7706d396a48a |grep "pid"

###### "pid": 45803,

###### "pid": 1

###### "type": "pid"

###### 执行**nsenter -t pid -a**进入GaussDB容器实例。

###### 仅非三方CaaS场景下产生-bash: EulerOS\_history: command not found报错。

###### inipv6-csp-a-0:/home/mtuser # nsenter -t 45803 -a

###### -bash: EulerOS_history: command not found

###### [root@gaussdb-6a19b165-0 /]#

###### 执行**unset PROMPT\_COMMAND**忽略-bash: EulerOS\_history: command not found错误。

###### 仅非三方CaaS场景下需要执行此步骤。

###### [root@gaussdb-6a19b165-0 /]# unset PROMPT_COMMAND

###### [root@gaussdb-6a19b165-0 /]#

##### 4.1.4 执行**su - dbuser -c "gsql -d auditdb -p 23521 -U auditdbuser -h localhost****"**，输入GaussDB数据库AUDITDB的用户密码， 进入AUDITDB数据库，其中Gauss数据库AUDITDB的用户默认密码可以从《GaussDB数据库用户默认账号》获取。

##### 4.1.5 执行**select \* from T\_OPERATIONLOG;**查看系统操作类操作日志。

##### 4.1.6 执行**select \* from T\_QUERYLOG;**查看系统查询类操作日志。

##### 4.1.7 执行**select \* from T\_SECURITYLOG;**查看系统安全日志。

##### 4.1.8 执行**select \* from T\_CSPSYSTEMLOG;**查看系统日志。

##### 4.1.9 执行**select \* from BACKUPCONFIG\_INFO;**查看审计日志日志留存期配置内容。

