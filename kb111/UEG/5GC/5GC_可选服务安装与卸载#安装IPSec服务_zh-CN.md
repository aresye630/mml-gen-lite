---
id: ''
name: 安装IPSec服务
ne_type: UEG
type: feature
description: IPSec(Internet Protocol Security)是IETF制定的一系列协议，通过对数据流中的每个IP包进行鉴权和加密，为IP数据报提供了高质量的、可互操作的、基于密码技术的安全性。  仅当UEG网元需要部署IPSec功能时，才需要安装IPSec服务。  **在CSPedge裸机场景下，需要先**实例化UEG，**然后**再参考本章节，**动态上线**IPSec服务。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-M","软件安装","基于生产预安装UEG（裸机容器）","修改UEG安装参数","UEG软件安装（已预安装）","可选服务安装与卸载","安装IPSec服务"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('DSP POD')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
IPSec(Internet Protocol Security)是IETF制定的一系列协议，通过对数据流中的每个IP包进行鉴权和加密，为IP数据报提供了高质量的、可互操作的、基于密码技术的安全性。仅当UEG网元需要部署IPSec功能时，才需要安装IPSec服务。**在CSPedge裸机场景下，需要先**实例化UEG，**然后**再参考本章节，**动态上线**IPSec服务。

## 必备事项
前提条件

前提条件

* 已经实例化UEG。已经检查系统运行状态，UEG正常工作。
* 准备好部署所需要的镜像文件：UEG-IPsec\_xx.x.x\_Docker\_EDGE\_X86.zip或UEG-IPsec\_xx.x.x\_Docker\_EDGE\_ARM.zip。（请区分X86和ARM场景，对不同的环境使用不同的软件包。）

  IPSec的镜像文件请从UEG下获取。

* 上下线本服务时，不能同时上下线其他部件。
* 当动态上线一个服务的任务失败；必须先动态下线此服务，再重新触发动态上线任务。如果是动态下线失败，只能继续重新触发动态下线任务。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    opr_featureenable_list:
      type: items
      properties:
        PODINSTANCENUM:
          name: 'Pod实例个数列表'
          type: string
          minLength: 0
          maxLength: 1024
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        EXTENDEDATTR:
          name: '扩展属性'
          type: string
          minLength: 0
          maxLength: 1024
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        FUNCTIONSETNAME:
          name: '网络功能集名称'
          type: string
          minLength: 0
          maxLength: 1024
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
  examples:
    opr_featureenable_list:
    - PODINSTANCENUM: 'ipsecexec-c4-pod:pod个数/ipsecctl-pod:pod个数'
      EXTENDEDATTR: '保持空白，无需填写。'
      FUNCTIONSETNAME: 'IPSec'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 上传依赖的软件包。

#### 1.1 登录OM Portal，单击“软件中心> 软件仓库 > 应用仓库”点击“添加”进行软件包上传。

#### 1.2 选择“UEG-IPsec\_xx.x.x\_Docker\_EDGE\_X86.zip” 或“UEG-IPsec\_xx.x.x\_Docker\_EDGE\_ARM.zip”包进行上传。当软件包状态变为“准备上传”，点击“上传”，完成IPSec软件包上传过程。

### 2 登录OM Portal的MML界面。

### 3 执行**DSP POD**命令（UEG-M和UEG-L在CSP视图），查询出：UEG网元IPSec是否已实例化。

### 如果所查到的IPsec Pod数**为无数据**；则继续执行后续步骤，需要将该Pod填写为规划值，执行命令后，将会实例化此Pod。

### 如果所查到的原IPsec Pod数为**非0**；则说明该Pod已实例化完毕，无需继续实例化操作。如果需要继续执行实例化，请先下线IPsec pod，再上线新的pod。

### 4 执行**OPR FEATUREENABLE**命令（UEG-M和UEG-L在UEG视图），填写pod实例个数。

### **UEG-M和UEG-L形态：**

```jinja2
{%- set DSP_POD=getParameterValue('DSP POD') -%}
{%- if DSP_POD=='' -%}
    {%- for item in opr_featureenable_list -%}
        OPR FEATUREENABLE:
        {#- --- 必选参数 --- -#}
        PODINSTANCENUM="{{item.PODINSTANCENUM}}",
        {#- --- 可选参数 --- -#}
        {%- if item.FUNCTIONSETNAME is not none -%}
            FUNCTIONSETNAME="{{item.FUNCTIONSETNAME}}",
        {%- endif -%}
        {%- if item.EXTENDEDATTR is not none -%}
            EXTENDEDATTR="{{item.EXTENDEDATTR}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### （1）无需配置“EXTENDEDATTR(扩展属性)”参数。

### （2）裸机环境下部署的pod数标准为1。

### 5 执行命令（UEG-M和UEG-L在CSP视图），确认已经成功实例化IPSec Pod。

### **UEG-M和UEG-L形态：**

### 回显pod个数和规划一致，且“Pod状态”为“Running”。

### 6 执行命令（UEG-M和UEG-L在UEG视图），查询进程的状态。

### **UEG-M和UEG-L形态：**

### 预期结果：“未就绪进程数”和“故障进程数”均为0。

