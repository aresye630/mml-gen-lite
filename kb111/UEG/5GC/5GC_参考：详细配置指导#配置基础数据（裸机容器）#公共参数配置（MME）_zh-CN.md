---
id: ''
name: 公共参数配置（MME）
ne_type: UEG
type: feature
description: 本章节用于指导MME的公共数据配置，包括PLMN、MMEID等。  以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","配置基础数据（裸机容器）","公共参数配置（MME）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本章节用于指导MME的公共数据配置，包括PLMN、MMEID等。以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* 已经获取网设LLD文档。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_cpsys_list:
      type: items
      properties:
        DESC:
          name: '系统描述'
          type: string
          maxLength: 64
          required: false
          description: '配置系统基本信息。  园区MME的PLMN需要和中心网络隔离，按照ToB园区的PLMN配置。'
          data_source: '整网规划'
          pattern: ''
          default: ''
        ID:
          name: '系统标识'
          type: integer
          minimum: 0
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NM:
          name: '系统名称'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRV:
          name: '服务描述'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROVER:
          name: '协议版本'
          type: string
          enum:
          - R4
          - R99
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CNID:
          name: '核心网标识'
          type: integer
          minimum:
          - 0
          - 65535
          maximum:
          - 4095
          - 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAP:
          name: '设备能力'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: '主备场景下：主用的CAP值为255，备用的CAP值为0。  负荷分担场景下：两套UEG的CAP值均为255。'
          data_source: ''
          pattern: ''
          default: ''
    add_hplmn_list:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: '配置用户的归属PLMN。  园区MME的PLMN需要和中心网络隔离，按照ToB园区的PLMN配置。'
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CC:
          name: '国家码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SM:
          name: '是否允许SM业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        MAXSMNUM:
          name: '最大承载数'
          type: integer
          minimum: 1
          maximum: 11
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 11
        SMS:
          name: '是否允许SMS业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        S5S8TYPE:
          name: '协议类型'
          type: string
          enum:
          - GTP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        PLMNN:
          name: '运营商名称'
          type: string
          maxLength: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_mmeid_list:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: '配置MMEID。'
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MMEGI:
          name: 'MME组识别码'
          type: string
          maxLength: 4
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MMEC:
          name: 'MME编码（起始值）'
          type: string
          maxLength: 2
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_emm_list:
      type: items
      properties:
        T3412:
          name: 'T3412（min）'
          type: integer
          minimum: 1
          maximum: 186
          required: false
          description: '该命令中T3412固定设置为15min，其余参数保持初始值设置。  UEG1联动复位后，连接态用户可以快速接入UEG2，但空闲态用户需依靠TAU/SR流程向UEG2发送上行信令来恢复业务，系统默认周期TAU时长较长（5G业务50min，4G业务54min）。由于2B用户量少，可以通过调低周期TAU的时长来触发空闲态用户的业务快速恢复（MME/AMF上TAU周期修改为15min）。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        RCHTMR:
          name: '移动可达定时器（min）'
          type: integer
          minimum: 2
          maximum: 198
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
  examples:
    set_cpsys_list:
    - DESC: 'HCGPBER1'
      ID: 0
      NM: 'HCGPBER1'
      SRV: 'prsBER1'
      MNC: '03'
      MCC: '123'
      PROVER: R4
      CNID: 0
      CAP: 255
    - DESC: 'HCGPBER1'
      ID: 0
      NM: 'HCGPBER1'
      SRV: 'prsBER1'
      MNC: '03'
      MCC: '123'
      PROVER: R4
      CNID: 0
      CAP: 0
    add_hplmn_list:
    - MCC: '123'
      MNC: '03'
      CC: '86'
      SM: YES
      MAXSMNUM: 7
      SMS: NO
      S5S8TYPE: GTP
      PLMNN: 'noname_1'
    - MCC: '123'
      MNC: '03'
      CC: '86'
      SM: YES
      MAXSMNUM: 7
      SMS: NO
      S5S8TYPE: GTP
      PLMNN: 'noname_1'
    add_mmeid_list:
    - MCC: '123'
      MNC: '03'
      MMEGI: '8001'
      MMEC: '01'
    - MCC: '123'
      MNC: '03'
      MMEGI: '8001'
      MMEC: '02'
    set_emm_list:
    - T3412: 15
      RCHTMR: 20
    - T3412: 15
      RCHTMR: 20
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置系统基本信息。

#### 2.1 //DC1

```jinja2
{%- for item in set_cpsys_list -%}
    SET CPSYS:
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {%- if item.ID is not none -%}
        ID={{item.ID}},
    {%- endif -%}
    {%- if item.NM is not none -%}
        NM="{{item.NM}}",
    {%- endif -%}
    {%- if item.SRV is not none -%}
        SRV="{{item.SRV}}",
    {%- endif -%}
    {%- if item.MCC is not none -%}
        MCC="{{item.MCC}}",
    {%- endif -%}
    {%- if item.MNC is not none -%}
        MNC="{{item.MNC}}",
    {%- endif -%}
    {%- if item.PROVER is not none -%}
        PROVER={{item.PROVER}},
    {%- endif -%}
    {%- if item.CNID is not none -%}
        CNID={{item.CNID}},
    {%- endif -%}
    {%- if item.CAP is not none -%}
        CAP={{item.CAP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置Home PLMN。

#### 3.1 //DC1

```jinja2
{%- for item in add_hplmn_list -%}
    ADD HPLMN:
    {#- --- 必选参数 --- -#}
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CC is not none -%}
        CC="{{item.CC}}",
    {%- endif -%}
    {%- if item.SM is not none -%}
        SM={{item.SM}},
    {%- endif -%}
    {%- if item.SMS is not none -%}
        SMS={{item.SMS}},
    {%- endif -%}
    {%- if item.S5S8TYPE is not none -%}
        S5S8TYPE={{item.S5S8TYPE}},
    {%- endif -%}
    {%- if item.PLMNN is not none -%}
        PLMNN="{{item.PLMNN}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SM=YES 时可选 --- -#}
    {%- if item.SM == 'YES' -%}
        {%- if item.MAXSMNUM is not none -%}
            MAXSMNUM={{item.MAXSMNUM}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置MMEID。

#### 4.1 //DC1

```jinja2
{%- for item in add_mmeid_list -%}
    ADD MMEID:
    {#- --- 必选参数 --- -#}
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    MMEGI="{{item.MMEGI}}",
    MMEC="{{item.MMEC}}",
    ;
{%- endfor -%}
```

### 5 设置移动性管理EMM（EPS Mobility Management）参数，将周期TAU的时长设置为15min。

#### 5.1 //DC1

```jinja2
{%- for item in set_emm_list -%}
    SET EMM:
    {#- --- 可选参数 --- -#}
    {%- if item.T3412 is not none -%}
        T3412={{item.T3412}},
    {%- endif -%}
    {%- if item.RCHTMR is not none -%}
        RCHTMR={{item.RCHTMR}},
    {%- endif -%}
    ;
{%- endfor -%}
```

