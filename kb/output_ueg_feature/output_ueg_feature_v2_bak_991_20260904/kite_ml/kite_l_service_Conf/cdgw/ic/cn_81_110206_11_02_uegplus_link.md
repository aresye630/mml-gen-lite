# 配置本地PCC功能（UPF）

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

当网络中无PCRF/PCF，若通过特定APN激活的用户需要激活为PCC用户，则需要配置本地PCC功能。

对于本地PCC功能（本地规则），UPF/SMF上需定义相同的规则组标识（即**ADD USERPROFILE**命令中的“用户模板名称（USERPROFILENAME）”参数值），UPF上定义该规则对应的业务流特征及业务的精细化管理动作。用户注册过程中，由SMF下发规则组标识，SMF通过规则组标识的方式激活UPF本地静态配置的规则来实现计费和策略的控制。SMF不支持实时更新规则。

**说明** 

适用于PGW-U、UPF。

配置本地PCC时，UEG上需要配置rule和UserProfile，本页面不关注具体规则内容配置，具体规则内容需要根据具体业务策略确定。

## 必备事项

前提条件

- 请仔细阅读GWFD-022201 PCC基本功能。
- 完成加载license（如果有需求，请联系华为技术支持工程师处理）。

数据

| 类别               | 参数名称                        | 取值样例            | 获取方法     | 说明                                      |
|:-----------------|:----------------------------|:----------------|:---------|:----------------------------------------|
| ADD PCCPOLICYGRP | PCC策略组名称（PCCPOLICYGRPNM）    | pg_test         | 本端规划     | 存在多条数据时，该参数不能相同。                        |
| ADD PCCPOLICYGRP | URR组名称（URRGROUPNAME）        | urrgp_test      | 已配置数据中获取 | 已通过ADD URRGROUP命令配置计费属性。                |
| ADD FLOWFILTER   | 流过滤器名称（FLOWFILTERNAME）      | flowfilter_test | 本端规划     | 不同流过滤器之间，该参数不能重复。                       |
| ADD FILTER       | 过滤器名称（FILTERNAME）           | filter_test     | 本端规划     | 不同过滤器之间，该参数不能重复。                        |
| ADD FILTER       | 三四层IPv4协议输入类型（L34PROTTYPE）  | STRING          | 本端规划     | Any to any的三四层filter。                   |
| ADD FILTER       | 三四层协议类型（L34PROTOCOL）        | ANY             | 本端规划     | Any to any的三四层filter。                   |
| ADD FLTBINDFLOWF | 流过滤器名称（FLOWFILTERNAME）      | flowfilter_test | 已配置数据中获取 | 使用ADD FLOWFILTER命令定义的流过滤器名称。            |
| ADD FLTBINDFLOWF | 过滤器名称（FILTERNAME）           | filter_test     | 已配置数据中获取 | 使用ADD FILTER命令定义的过滤器名称。                 |
| ADD RULE         | 规则名称（RULENAME）              | rule_test       | 与对端协商    | 存在多条数据时，该参数+策略类型不能完全相同。 与SMF上配置的规则名称相同。 |
| ADD RULE         | 策略类型（POLICYTYPE）            | PCC             | 本端规划     | 使用样例值。                                  |
| ADD RULE         | 流过滤器或流过滤器组选择(FILTERINGMODE) | FLOWFILTER      | 本端规划     | -                                       |
| ADD RULE         | 流过滤器名称（FLOWFILTERNAME）      | flowfilter_test | 已配置数据中获取 | 使用ADD FLOWFILTER命令定义的流过滤器名称。            |
| ADD RULE         | 策略名称（POLICYNAME）            | pg_test         | 已配置数据中获取 | 使用ADD PCCPOLICYGRP命令定义的PCC策略组名称。        |
| ADD RULE         | 全局优先级（PRIORITY）             | 65535           | 本端规划     | 仅对PCC用户生效。优先级值越小，优先级越高。                 |
| ADD USERPROFILE  | 用户模板名称（USERPROFILENAME）     | up_test         | 与对端协商    | 与SMF上配置的用户模板名称保持一致。                     |
| ADD RULEBINDING  | 用户模板名称（USERPROFILENAME）     | up_test         | 已配置数据中获取 | 使用ADD USERPROFILE命令定义的用户模板名称。           |
| ADD RULEBINDING  | 规则名称（RULENAME）              | rule_test       | 已配置数据中获取 | 使用ADD RULE命令定义的规则名称。                    |

## 操作步骤

1. 打开本特性的License配置开关。

   **SET LICENSESWITCH**
2. 配置PCC策略组。

   **ADD PCCPOLICYGRP**
3. 配置流过滤器。

   **ADD FLOWFILTER**

   流过滤器必须至少绑定一个filter或一个l7filter，否则所有报文都匹配不上该流过滤器。
4. 配置三四层过滤条件。
   1. 配置三四层过滤条件。

      **ADD FILTER**
   2. 配置三四层过滤条件与流过滤器的绑定关系。

      **ADD FLTBINDFLOWF**
5. 配置规则。

   **ADD RULE**

   若需配置多个规则，则需要多次执行5。
6. 配置规则与用户模板的绑定关系 。
   1. 创建UserProfile。

      **ADD USERPROFILE**
   2. 将已配置的rule绑定到UserProfile。

      **ADD RULEBINDING**
7. 将新配置的Filter跟UserProfile置为生效。

   **SET REFRESHSRV**

## 任务示例

任务描述

本举例中配置的是3/4层any to any的filter，未配置7层规则，表示所有报文都匹配。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3G5PCCB01",SWITCH=ENABLE;
```

//配置流过滤器和三四层过滤条件。

```
ADD FILTER: FILTERNAME="filter_test", L34PROTTYPE=STRING, L34PROTOCOL=ANY;
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_test";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",FILTERNAME="filter_test";
```

//配置PCC策略组。**当需要计费时，请配置参数URRGROUPNAME**。

```
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pg_test",URRGROUPNAME="urrgp_test";
```

//配置规则。

```
ADD RULE:RULENAME="rule_test",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilter_test",PRIORITY=65535, POLICYNAME="pg_test";
```

//配置规则与用户模板的绑定关系。

```
ADD USERPROFILE:USERPROFILENAME="up_test";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";
```

//将新配置的Filter和UserProfile置为生效。

```
SET REFRESHSRV:REFRESHTYPE=ALL;
```