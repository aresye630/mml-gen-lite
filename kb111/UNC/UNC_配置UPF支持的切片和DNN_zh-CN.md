---
id: ''
name: 配置UPF支持的切片和DNN
ne_type: UNC
type: feature
description: '* SMF根据网络规划配置对端UPF支持的服务切片信息。用户激活时，SMF从激活请求中获取用户切片信息，根据UPF支持的服务切片列表选择出符合条件的UPF。 * SMF根据网络规划配置对端UPF支持的DNN。用户激活时，SMF从激活请求中获取用户DNN信息，根据UPF支持的DNN列表选择出符合条件的UPF。    5G SA架构下，切片和DNN是一对多关系，即：一个切片可以包含多个DNN，一个DNN只能归属于一个切片。切片底下包含很多DNN，如果UPF支持该切片，那么UPF就应该支持切片底下的所有DNN。'
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置SMF&PGW-C&SGW-C&GGSN","公共配置","配置和UPF的对接（N4/Sxa/Sxb）","配置N4接口","配置UPF支持的切片和DNN"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
* SMF根据网络规划配置对端UPF支持的服务切片信息。用户激活时，SMF从激活请求中获取用户切片信息，根据UPF支持的服务切片列表选择出符合条件的UPF。* SMF根据网络规划配置对端UPF支持的DNN。用户激活时，SMF从激活请求中获取用户DNN信息，根据UPF支持的DNN列表选择出符合条件的UPF。  5G SA架构下，切片和DNN是一对多关系，即：一个切片可以包含多个DNN，一个DNN只能归属于一个切片。切片底下包含很多DNN，如果UPF支持该切片，那么UPF就应该支持切片底下的所有DNN。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* 已经获取网设LLD文档。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_pnfns_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置用户面支持的服务切片信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SST:
          name: '切片/服务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SD:
          name: '切片分类器'
          type: string
          minLength: 0
          maxLength: 8
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 'FFFFFF'
    add_pnfdnn_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置用户面节点支持的DNN及其归属切片的信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 0
          maxLength: 66
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PNFNSINDEX:
          name: '对端NF的切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 0
  examples:
    add_pnfns_list:
    - INDEX: 1
      NFINSTANCEID: 'UPF_Instance_1'
      SST: 1
      SD: 'FFFFFF'
    add_pnfdnn_list:
    - INDEX: 1
      NFINSTANCEID: 'UPF_Instance_1'
      DNN: 'huawei.com'
      PNFNSINDEX: 1
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置UPF\_Instance\_1~UPF\_Instance\_4支持的网络切片。

```jinja2
{%- for item in add_pnfns_list -%}
    ADD PNFNS:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SST={{item.SST}},
    {#- --- 可选参数 --- -#}
    {%- if item.SD is not none -%}
        SD="{{item.SD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置UPF\_Instance\_1~UPF\_Instance\_4支持的DNN。

```jinja2
{%- for item in add_pnfdnn_list -%}
    ADD PNFDNN:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    DNN="{{item.DNN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PNFNSINDEX is not none -%}
        PNFNSINDEX={{item.PNFNSINDEX}},
    {%- endif -%}
    ;
{%- endfor -%}
```

