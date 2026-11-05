---
id: ''
name: 安装IPSec服务
ne_type: UEG
type: feature
description: IPSec(Internet Protocol Security)是IETF制定的一系列协议，通过对数据流中的每个IP包进行鉴权和加密，为IP数据报提供了高质量的、可互操作的、基于密码技术的安全性。  仅当UEG网元需要部署IPSec功能时，才需要安装IPSec服务。  **在CSPedge裸机场景下，需要先**实例化UEG，**然后**再参考本章节，**动态上线**IPSec服务。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","UEG软件安装（风筝M）","基于生产预安装UEG（裸机容器）","修改UEG安装参数","UEG软件安装（已预安装）","可选服务安装与卸载","安装IPSec服务"]
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
  examples:
    opr_featureenable_list:
    - PODINSTANCENUM: 'ipsecctl-pod:1/ipsecexec-c4-pod:1'
      FUNCTIONSETNAME: 'IPSec'
      EXTENDEDATTR: '保持空白，无需填写。'
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

### 4 **（可选）**更新pbui-domain。

### 仅当**UEG-S**从21.3.2及之前版本升级到当前版本后，再进行IPSec动态上线时，需要执行该操作步骤。其他场景下，请跳过该操作步骤。

#### 4.1 在OM Portal菜单界面选择“应用管理 > 应用部署”，在应用部署下找到UEG的堆栈名称，点击“更新”。

#### 4.2 在“show”页面中进行“domainList01”参数值检查。

##### 4.2.1 如果参数值“numa0”中含有“pbui-domain”，则无需修改，直接跳转到5。

##### 4.2.2 如果参数值“numa0”中没有“pbui-domain”则需要执行如下步骤：

###### 4.2.2.1 手动添加“pbui-domain”到“numa0”下。

###### domainList01参数正确取值如下：

###### default："numa0:pbub-domain,pbua-domain,mep1-domain,pbuen-domain,**pbui-domain**,pbul-domain;numa1:isu-domain,omu-domain,sdu-domain,pbuml-domain"

###### 4.2.2.2 单击“下一步”，随后再单击“下一步”。

###### 4.2.2.3 单击“开始检查”，待检查完成后再单击“更新堆栈”，等待更新完成。

### 5 执行**OPR FEATUREENABLE**命令（UEG-M和UEG-L在UEG视图），填写pod实例个数。

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

### 6 执行命令（UEG-M和UEG-L在CSP视图），确认已经成功实例化IPSec Pod。

### **UEG-M和UEG-L形态：**

### 回显pod个数和规划一致，且“Pod状态”为“Running”。

### 7 执行命令（UEG-M和UEG-L在UEG视图），查询进程的状态。

### **UEG-M和UEG-L形态：**

### 预期结果：“未就绪进程数”和“故障进程数”均为0。

