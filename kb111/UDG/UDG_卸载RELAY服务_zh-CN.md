---
id: ''
name: 卸载RELAY服务
ne_type: UDG
type: feature
description: 当运营商不需要RELAY服务或RELAY服务动态上线失败时，可以单独卸载RELAY的pod，从而下线RELAY服务。
risk_level: ''
doc_source: ["网络部署","软件安装","基于VNF LCM安装UDG（非SDN）","卸载UDG","卸载RELAY服务"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商不需要RELAY服务或RELAY服务动态上线失败时，可以单独卸载RELAY的pod，从而下线RELAY服务。

## 必备事项
前提条件

已经完成网络设计，已规划下线RELAY pod的类型和数量。
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

### 1 下线RELAY堆栈。

#### 1.1 登录MANO（MAE/VNF LCM）业务面客户端。

##### 1.1.1 在浏览器地址栏中输入以下地址后按回车键，弹出MANO（MAE/VNF LCM）客户端界面。

##### **https://MANO（MAE/VNF LCM）业务的IP地址:端口号/**（例如https://10.50.12.104:31943/）

##### 1.1.2 输入用户名和密码。

##### 系统默认的用户名和密码是“admin/Changeme\_123”，如果已修改MANO（MAE/VNF LCM）客户端用户名和密码，请使用新设置的用户名和密码登录。

##### 1.1.3 单击“登录”，在MAE主界面的“应用”区域，单击“VNF LCM”，进入MANO（MAE/VNF LCM）系统界面。

#### 1.2 卸载RELAY堆栈。

##### 1.2.1 选择菜单栏“VNF生命周期管理 >扩缩容管理 > 手动扩缩容”，进入“手动扩缩容”窗口。

##### 1.2.2 选择待操作的VNF，单击右侧“操作”列的“堆栈上下线”图标。

##### 1.2.3 在弹出的界面中“操作”选择“下线”，选择需要下线的“堆栈名称”，**注意不需要勾选**“进行虚拟机扩缩容”。

##### 1.2.4 单击“下一步”后，在弹出的确认界面点击“确认”，自动跳转到“扩缩容任务”界面，可以查看下线堆栈进度。如果下线堆栈失败，请联系华为技术支持解决。

##### 1.2.5 执行命令，确认已经成功下线RELAY服务pod。

##### 回显“查询Pod不存在”。

### 2 若动态下线RELAY服务后，不再上线RELAY服务，则需要缩容RELAY自身VM（PBU\_E-R\_ARM），释放VM资源。若后续还需要上线RELAY服务，则不必缩容RELAY自身VM。**缩容VM**：请参见《UDG边缘侧扩缩容指导书（扩容单板）》。

