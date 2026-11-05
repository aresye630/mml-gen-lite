---
id: ''
name: 修改Redis数据库管理员用户密码
ne_type: UDG
type: feature
description: 该操作为高危操作，修改后请妥善保管密码，操作影响见对系统的影响。  升级或者安装补丁后，如果存在回退升级或回退补丁场景，请勿修改Redis数据库管理员用户密码。  修改密码后，如果存在单节点故障恢复场景，需要重新修改故障恢复节点的密码，保持两个节点Redis数据库管理员用户的密码一致。  * 在开局结束后，系统管理员必须及时修改Redis数据库管理员用户的密码，为确保Redis数据库安全。 * 在日常维护中，系统管理员需要定期修改Redis数据库管理员用户的密码，为确保Redis数据库安全。  容器部署模式需要登录容器后执行。
risk_level: ''
doc_source: ["网络部署","安全配置","UDG安全配置","安全配置建议","必选配置","系统安全配置","修改数据库用户密码","修改Redis数据库管理员用户密码"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该操作为高危操作，修改后请妥善保管密码，操作影响见对系统的影响。升级或者安装补丁后，如果存在回退升级或回退补丁场景，请勿修改Redis数据库管理员用户密码。修改密码后，如果存在单节点故障恢复场景，需要重新修改故障恢复节点的密码，保持两个节点Redis数据库管理员用户的密码一致。* 在开局结束后，系统管理员必须及时修改Redis数据库管理员用户的密码，为确保Redis数据库安全。* 在日常维护中，系统管理员需要定期修改Redis数据库管理员用户的密码，为确保Redis数据库安全。容器部署模式需要登录容器后执行。

## 必备事项
前提条件

* 已登录OM Portal。
* 已获取Redis数据库管理员用户“dbuser”用户的旧密码。

  待修改用户的初始密码请参见《UDG数据库用户默认帐号》，如果初始密码已经修改，待修改用户的旧密码请联系系统管理员获取。
* 已准备Redis数据库管理员用户“dbuser”用户的新密码。

  新密码符合如下复杂程度要求：
  + 密码不能少于8个字符且不超过32个字符。
  + 密码必须由如下组合而成：
    - 至少包括一个大写字母（A~Z）；
    - 至少包括一个小写字母（a~z）；
    - 至少包括一个数字字符（0~9）；
    - 至少包括1个特殊字符，如：“~、#、$、%、&、(、)、\*、+、,、-、.、:、;、<、=、>、/、?、@、[、]、^、\_、`、{、|、}、!”
  + 密码不能包含用户名或者用户名的倒序。
  + 新密码与旧密码至少有两个字符不同。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties: {}
  examples: {}
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 选择“应用配置 > 服务治理”，查看Redis数据库的主备状态是否正常。

### Redis数据库主备状态通过“应用配置”“服务治理”中OMCache服务列表的“属性”列中“status”字段值获取。如查看OMCache服务实例“属性”信息所示，如果“status”字段值有“master”和“slave”，则说明主备状态正常。

### **图1** 查看OMCache服务实例“属性”信息

### 主备状态正常 => 步骤 2

### 主备状态异常 => 联系华为技术支持，先处理Redis数据库主备状态，处理完成后，执行步骤 2

### 2 获取Redis数据库节点IP。

### Redis数据库节点IP通过“应用配置 > 服务治理”中OMCache服务列表的“属性”列中“nodeID”字段值获取。如查看OMCache服务实例“属性”信息所示，如果“status”字段值为“master”则对应“nodeID”字段值为主用节点IP，如果“status”字段值为“slave”则对应“nodeID”字段值为备用节点IP。

### 3 登录服务器。

#### 3.1 Windows操作系统使用Putty工具以mtuser用户登录OMU，Linux操作系统通过终端模拟器以mtuser用户登录OMU，执行**su root**切换至root用户。

#### 3.2 通过2获取到的主用Redis数据库节点IP，执行**ssh mtuser@<*主用Redis数据库节点IP*>**登录主用Redis数据库所在节点，然后执行**su root**切换至root用户。

### 4 执行以下操作登录Redis容器。

#### 4.1 通过执行**which docker**命令，检查docker可执行文件是否存在。

##### 4.1.1 若**存在**，如下命令所示。

##### host-192-168-0-2:/home/mtuser # which docker

##### /usr/bin/docker

##### 执行**docker ps | grep redis**命令查询Redis容器ID。

##### host-192-168-0-2:/home/mtuser # docker ps | grep redis

##### fb5446ab13dd        192.168.0.1:20202/op_svc_pom/redis_docker:20.4.1.B122                      "/bin/c-init -v /opt…"   29 hours ago        Up 29 hours                             k8s_redis-softwarecomp_omcache-2da1c75d-0_fst-manage_9f444290-a584-4a45-98e9-911f6e833b91_1

##### host-192-168-0-2:/home/mtuser #

##### 上述示例中，“fb5446ab13dd”为主用Redis容器ID。

##### 执行**docker exec**命令以root用户登录Redis容器，如下命令所示。

##### host-192-168-0-2:/home/mtuser # docker exec -u root -it --privileged fb5446ab13dd bash

##### [root@fb5446ab13dd /]#

##### 4.1.2 若**不****存在**，如下命令所示。

##### host-192-168-0-2:/home/mtuser # which docker

##### which: no docker in (/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin)

##### 执行**crictl ps | grep redis**命令查询Redis容器ID。

##### host-192-168-0-2:/home/mtuser # crictl ps |grep redis

##### fb5446ab13dd       registry.fusionstage.local:20202/csp/redis_docker:23.0.0.B214                     45 hours ago        Running             redis-softwarecomp              0                   b1d7289270a31

##### 上述示例中，“fb5446ab13dd ”为主用Redis容器ID。

##### 执行**crictl inspect**命令查询Redis容器实例的pid，如下命令所示。

##### host-192-168-0-2:/home/mtuser # crictl inspect fb5446ab13dd |grep "pid" | head -1

##### "pid": 37141,

##### 执行**nsenter**命令进入Redis容器，如下命令所示。

##### host-192-168-0-2:/home/mtuser # nsenter -t 37141 -a

##### -bash: EulerOS_history: command not found

##### [root@omcache-b2329b88-0 /]#

##### 执行**unset PROMPT\_COMMAND**命令忽略-bash: EulerOS\_history: command not found错误

##### [root@omcache-b2329b88-0 /]# unset PROMPT_COMMAND

##### [root@omcache-b2329b88-0 /]#

### 5 运行脚本mod\_local\_redisadapter\_pwd.sh更新Redis数据库密码。

### su - paas -s /opt/csp/redis/OMCache/bin/mod_local_redisadapter_pwd.sh

### *********************************************************************

### *************************** WARNING *********************************

### *********************************************************************

### * This shell script is used to fresh the password of redis adapter in memory. *

### * You need enter 3 parameters.                                      *

### * If you want to quit, please press "Ctrl + c".                     *

### *********************************************************************

### 1. The first parameter is old password.

### Please input the old password ended with Enter: //此处输入前提条件中获取的Redis数据库旧密码

### The old password input end.

### 2. The second parameter is new password.

### Note that the new password must contain 8 to 32 characters.

### Note that the new password must contain numbers, lowercase letters, uppercase letters and special characters.

### Note that the collection of special characters is ~#$%&()*+,-.:;<=>/?@[]^_`{|}!

### Note that the new password cannot be the user name or its reverse.

### Note that the new password must contain at least two characters different from the old password.

### Please input the new password ended with Enter: //此处输入前提条件中准备的Redis数据库新密码

### The new password input end.

### 3. The third parameter is confirmation of new password.

### Please re-enter new password ended with Enter: //此处输入前提条件中准备的Redis数据库新密码

### Re-enter new password input end.

### Congratulations, modify password success!

### *********************************************************************

### 脚本执行的回显信息中包含“success”，表示密码修改成功。

### 6 通过步骤 2获取到的备用Redis数据库IP地址，参照步骤 3和步骤 4操作进入到备用Redis容器中，执行步骤 5操作更新备用Redis数据库密码。

### 7 重启Redis客户端和服务端所在节点。

### 网元普通域前台执行mml命令**DSP NODE**查询OMU或CSP\_A、CSP\_B、CSP\_C类型虚拟机，执行mml命令**RST NODE**复位。

### 8 等待7执行结束15分钟后，登录网元前台（根据修改场景登录普通域或扩展域前台），打开“应用配置->服务治理”，搜索opsagent，执行批量复位。

