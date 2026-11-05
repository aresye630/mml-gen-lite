---
id: ''
name: 激活流串接功能
ne_type: UDG
type: feature
description: 当需要通过部署增值业务提升用户体验或运营收益时，请参考本节激活流串接功能。
risk_level: ''
doc_source: ["特性部署","业务专题","UDG SFIP功能专题","功能描述","流串接功能","激活流串接功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当需要通过部署增值业务提升用户体验或运营收益时，请参考本节激活流串接功能。

## 必备事项
前提条件

* 请仔细阅读流串接功能。
* 已通过OM Portal登录“第三方应用操作维护入口”界面。
* 本特性受License控制，请先完成加载License。
* 已根据网络规划获取表1中数据及表中各参数间的关联关系。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV4ISCFUN02'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 在“MML命令行 - UDG”窗口上执行**SET LICENSESWITCH**打开License开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 创建FG，同时完成FG绑定业务链VLAN、FG包含的app范围的创建。

#### 2.1 在“第三方应用操作维护入口”界面，选择“业务链”，进入业务链的配置界面。

#### 2.2 在左边导航树选择“FG”。

#### 2.3 单击“创建FG”，弹出“创建FG”的界面。

#### 2.4 输入"FG名称"、"VLAN ID"。

#### 此处VLAN ID为app External（Chain）平面的VLAN ID，输入VLAD ID后，显示chain平面VLAN ID为输入值的未绑定到FG下的app全集。

#### 2.5 勾选FG包含的应用的范围。

#### 2.6 单击“确定”，完成创建。

#### **图1** 创建FG

### 3 创建SFC。

#### 3.1 在左边导航树选择“FG > FG Name > SFC”。

#### 3.2 单击“创建SFC”，弹出“创建SFC”的界面。

#### 3.3 输入“上行首跳ID”、“下行首跳ID”和“SFC名称”。

#### 3.4 鼠标拖动“应用”区域框下的app实例到下方线上。

#### 3.5 单击“确定”，完成创建。

#### **图2** 创建SFC

