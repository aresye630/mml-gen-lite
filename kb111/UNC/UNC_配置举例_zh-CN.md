---
id: ''
name: 配置举例
ne_type: UNC
type: feature
description: 本操作指导用实例描述2G现网演进成SGSN Pool的配置过程。  图1是2G网络演进目标示意图。  **图1** 目标网络示意图
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","容灾功能","SGSN容灾方案","改造部署","激活业务","典型场景：SGSN Pool改造","2G现网演进成SGSN Pool","配置举例"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导用实例描述2G现网演进成SGSN Pool的配置过程。图1是2G网络演进目标示意图。**图1** 目标网络示意图

```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_pool_list:
      type: items
      properties:
        POOLID:
          name: 'POOL标识'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRILENGTH:
          name: 'NRI长度'
          type: integer
          minimum: 1
          maximum: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_localnri_list:
      type: items
      properties:
        POOLID:
          name: 'POOL区标识'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRIVBGN:
          name: 'NRI起始值'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRINUM:
          name: 'NRI个数'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    blk_localnri_list:
      type: items
      properties:
        POOLID:
          name: 'POOL区标识'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRIVBGN:
          name: 'NRI起始值'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_localnri_list:
      type: items
      properties:
        POOLID:
          name: 'POOL区标识'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRIVBGN:
          name: 'NRI起始值'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_localnri_list_1:
      type: items
      properties:
        POOLID:
          name: 'POOL区标识'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRIVBGN:
          name: 'NRI起始值'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRINUM:
          name: 'NRI个数'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_sys_list:
      type: items
      properties:
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
    add_poolnri_list:
      type: items
      properties:
        POOLID:
          name: 'POOL区标识'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRIV:
          name: 'NRI值'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV4V6
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'SGSN信令面地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGSNN:
          name: 'SGSN名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        ALTERNATIVE:
          name: 'SGSN信令面地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: 'SGSN信令面地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_nse_list:
      type: items
      properties:
        NSEI:
          name: 'NSEI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GB\_FLEX:
          name: 'GB\_FLEX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_gbnsecfgpara_list:
      type: items
      properties:
        PARAINDEX:
          name: 'PARAINDEX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GB\_FLEX:
          name: 'GB\_FLEX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_offloadinf_list:
      type: items
      properties:
        OFFLOADTMR:
          name: '迁移模式周期路由更新定时器（s）'
          type: integer
          minimum: 2
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FIRSTTM:
          name: '第一阶段迁移时间（min）'
          type: integer
          minimum: 0
          maximum: 432
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NONRAI:
          name: '非广播 RAI'
          type: string
          maxLength: 12
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POOLID:
          name: 'POOL区标识'
          type: integer
          minimum: 0
          maximum: 4095
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NULLNRIV:
          name: 'NULL NRI值'
          type: integer
          minimum: 0
          maximum: 1023
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nonrai_list:
      type: items
      properties:
        NONRAI:
          name: '路由区标识'
          type: string
          maxLength: 12
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV4V6
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'SGSN IPv4信令面地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGSNN:
          name: 'SGSN名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        ALTERNATIVE:
          name: 'SGSN IPv6信令面地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: 'SGSN IPv6信令面地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
    add_poolla_list:
      type: items
      properties:
        LAC:
          name: '位置区域码'
          type: string
          maxLength: 4
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_poolla_list_3:
      type: items
      properties:
        BGNTAI:
          name: '起始TAI'
          type: string
          maxLength: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDTAI:
          name: '终止TAI'
          type: string
          maxLength: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LAC:
          name: '位置区域码'
          type: string
          maxLength: 4
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_gbauthciph_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - SPECIAL_USER
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SECPLC:
          name: '安全策略'
          type: string
          enum:
          - AUTHANDPROTECTED
          - AUTHONLY
          - NEVER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHEVENT:
          name: '鉴权事件'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTSAUTH:
          name: '是否支持附着流程的二次鉴权功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHEVENTTHRESHOLD:
          name: '鉴权事件上限'
          type: integer
          minimum: 0
          maximum: 1023
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHPERIOD:
          name: '鉴权周期'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHSETSNUMBER:
          name: '鉴权集数量'
          type: integer
          minimum: 1
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHSETV2:
          name: '是否支持V2取鉴权集功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAFTIMES:
          name: '用户鉴权失败次数临界值'
          type: integer
          minimum: 3
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CIPHALG:
          name: '加密算法'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GETAUTHADVTH:
          name: '预先取鉴权集门限值'
          type: integer
          minimum: 0
          maximum: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NCIPH:
          name: '版本协商失败允许不加密'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREGETAUTHSETS:
          name: '是否预取鉴权集'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RAUSAUTH:
          name: '是否支持路由更新流程的二次鉴权功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNUM:
          name: '鉴权集重用次数'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        XIDRESET:
          name: 'Rau Accept无响应后是否启用XID Reset流程'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_gmmptmsirealloc_list:
      type: items
      properties:
        WITHRAUPROC:
          name: '伴随RAU流程分配'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REALLOCTMR:
          name: 'P-TMSI重分配流程间隔时长（小时）'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REALLOCCOND:
          name: 'P-TMSI重分配流程发起条件'
          type: string
          enum:
          - AFTER_PTMSI_ALLOC
          - IN_READY_STATE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_gbauthciph_list_1:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - SPECIAL_USER
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SECPLC:
          name: '安全策略'
          type: string
          enum:
          - AUTHANDPROTECTED
          - AUTHONLY
          - NEVER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHEVENT:
          name: '鉴权事件'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTSAUTH:
          name: '是否支持附着流程的二次鉴权功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHEVENTTHRESHOLD:
          name: '鉴权事件上限'
          type: integer
          minimum: 0
          maximum: 1023
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHPERIOD:
          name: '鉴权周期'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHSETSNUMBER:
          name: '鉴权集数量'
          type: integer
          minimum: 1
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHSETV2:
          name: '是否支持V2取鉴权集功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAFTIMES:
          name: '用户鉴权失败次数临界值'
          type: integer
          minimum: 3
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CIPHALG:
          name: '加密算法'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GETAUTHADVTH:
          name: '预先取鉴权集门限值'
          type: integer
          minimum: 0
          maximum: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NCIPH:
          name: '版本协商失败允许不加密'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREGETAUTHSETS:
          name: '是否预取鉴权集'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RAUSAUTH:
          name: '是否支持路由更新流程的二次鉴权功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNUM:
          name: '鉴权集重用次数'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        XIDRESET:
          name: 'Rau Accept无响应后是否启用XID Reset流程'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_gbauthciph_list_2:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - SPECIAL_USER
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SECPLC:
          name: '安全策略'
          type: string
          enum:
          - AUTHANDPROTECTED
          - AUTHONLY
          - NEVER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHEVENT:
          name: '鉴权事件'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTSAUTH:
          name: '是否支持附着流程的二次鉴权功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHEVENTTHRESHOLD:
          name: '鉴权事件上限'
          type: integer
          minimum: 0
          maximum: 1023
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHPERIOD:
          name: '鉴权周期'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHSETSNUMBER:
          name: '鉴权集数量'
          type: integer
          minimum: 1
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHSETV2:
          name: '是否支持V2取鉴权集功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAFTIMES:
          name: '用户鉴权失败次数临界值'
          type: integer
          minimum: 3
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CIPHALG:
          name: '加密算法'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GETAUTHADVTH:
          name: '预先取鉴权集门限值'
          type: integer
          minimum: 0
          maximum: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NCIPH:
          name: '版本协商失败允许不加密'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREGETAUTHSETS:
          name: '是否预取鉴权集'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RAUSAUTH:
          name: '是否支持路由更新流程的二次鉴权功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNUM:
          name: '鉴权集重用次数'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        XIDRESET:
          name: 'Rau Accept无响应后是否启用XID Reset流程'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_nse_list_1:
      type: items
      properties:
        NSEI:
          name: 'NSEI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GB\_FLEX:
          name: 'GB\_FLEX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_gbnsecfgpara_list_1:
      type: items
      properties:
        PARAINDEX:
          name: 'PARAINDEX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GB\_FLEX:
          name: 'GB\_FLEX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_nse_list_2:
      type: items
      properties:
        NSEI:
          name: 'NSEI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GB\_FLEX:
          name: 'GB\_FLEX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_gbnsecfgpara_list_2:
      type: items
      properties:
        PARAINDEX:
          name: 'PARAINDEX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GB\_FLEX:
          name: 'GB\_FLEX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_resrec_list:
      type: items
      properties:
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NAME:
          name: 'NAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DOMAIN:
          name: 'DOMAIN'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IP:
          name: 'IP'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_resrec_list_1:
      type: items
      properties:
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NAME:
          name: 'NAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DOMAIN:
          name: 'DOMAIN'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IP:
          name: 'IP'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_pool_list:
    - POOLID: 0
      NRILENGTH: 5
    add_localnri_list:
    - POOLID: 0
      NRIVBGN: 1
      NRINUM: 1
    blk_localnri_list:
    - POOLID: 1
      NRIVBGN: 10
    rmv_localnri_list:
    - POOLID: 1
      NRIVBGN: 10
    add_localnri_list_1:
    - POOLID: 1
      NRIVBGN: 10
      NRINUM: 1
    set_sys_list:
    - CNID: 1
    add_poolnri_list:
    - POOLID: 0
      NRIV: 2
      IPTYPE: IPV4
      IPV4: '10.168.155.2'
      SGSNN: 'SGSN2'
      ALTERNATIVE: ''
      IPV6: ''
    mod_nse_list:
    - NSEI: '1001'
      GB\_FLEX: YES
    mod_gbnsecfgpara_list:
    - PARAINDEX: '1'
      GB\_FLEX: YES
    set_offloadinf_list:
    - OFFLOADTMR: 4
      FIRSTTM: 54
      NONRAI: '12300611111'
      POOLID: 0
      NULLNRIV: 0
    add_nonrai_list:
    - NONRAI: '12300612222'
      IPTYPE: IPV4
      IPV4: '10.168.155.2'
      SGSNN: 'SGSN2'
      ALTERNATIVE: ''
      IPV6: ''
    set_licenseswitch_list:
    - LICITEM: 'LKV2GBFLEX02'
      SWITCH: ENABLE
    add_poolla_list:
    - LAC: '0011'
    add_poolla_list_3:
    - BGNTAI: '1230033101'
      ENDTAI: '1230033105'
      LAC: '0011'
    mod_gbauthciph_list:
    - SUBRANGE: ALL\_USER
      SECPLC: AUTHONLY
      AUTHEVENT: PROD\_RAU-1&SMS\_MT-1&SMS\_MO-1&DETACH-1&INTER\_RAU-1&INTRA\_RAU-1&PTMSI\_ATTACH-1&IMSI\_ATTACH-1&PTMSI\_SIG\_NOMATCH-1&PTMSI\_SIG\_NOSIG-1&SM\_PDP-1&LCS-1&SYSTEM\_CHANGE\_INTRA\_RAU-1
      ATTSAUTH: ''
      AUTHEVENTTHRESHOLD: ''
      AUTHPERIOD: ''
      AUTHSETSNUMBER: ''
      AUTHSETV2: ''
      CAFTIMES: ''
      CIPHALG: ''
      GETAUTHADVTH: ''
      NCIPH: ''
      PREGETAUTHSETS: ''
      RAUSAUTH: ''
      RNUM: ''
      XIDRESET: ''
      IMSIPRE: ''
    set_gmmptmsirealloc_list:
    - WITHRAUPROC: YES
      REALLOCTMR: 1
      REALLOCCOND: IN\_READY\_STATE
    mod_gbauthciph_list_1:
    - SUBRANGE: ALL\_USER
      SECPLC: AUTHONLY
      AUTHEVENT: PROD\_RAU-0&SMS\_MT-0&SMS\_MO-0&DETACH-0&INTER\_RAU-1&INTRA\_RAU-0&PTMSI\_ATTACH-1&IMSI\_ATTACH-1&PTMSI\_SIG\_NOMATCH-0&PTMSI\_SIG\_NOSIG-0&SM\_PDP-0&LCS-0&SYSTEM\_CHANGE\_INTRA\_RAU-0
      ATTSAUTH: ''
      AUTHEVENTTHRESHOLD: ''
      AUTHPERIOD: ''
      AUTHSETSNUMBER: ''
      AUTHSETV2: ''
      CAFTIMES: ''
      CIPHALG: ''
      GETAUTHADVTH: ''
      NCIPH: ''
      PREGETAUTHSETS: ''
      RAUSAUTH: ''
      RNUM: ''
      XIDRESET: ''
      IMSIPRE: ''
    mod_gbauthciph_list_2:
    - SUBRANGE: ALL\_USER
      SECPLC: AUTHONLY
      AUTHEVENT: PROD\_RAU-1&SMS\_MT-1&SMS\_MO-1&DETACH-1&INTER\_RAU-1&INTRA\_RAU-1&PTMSI\_ATTACH-1&IMSI\_ATTACH-1&PTMSI\_SIG\_NOMATCH-1&PTMSI\_SIG\_NOSIG-1&SM\_PDP-1&LCS-1&SYSTEM\_CHANGE\_INTRA\_RAU-1
      ATTSAUTH: ''
      AUTHEVENTTHRESHOLD: ''
      AUTHPERIOD: ''
      AUTHSETSNUMBER: ''
      AUTHSETV2: ''
      CAFTIMES: ''
      CIPHALG: ''
      GETAUTHADVTH: ''
      NCIPH: ''
      PREGETAUTHSETS: ''
      RAUSAUTH: ''
      RNUM: ''
      XIDRESET: ''
      IMSIPRE: ''
    mod_nse_list_1:
    - NSEI: '1002'
      GB\_FLEX: YES
    mod_gbnsecfgpara_list_1:
    - PARAINDEX: '1'
      GB\_FLEX: YES
    mod_nse_list_2:
    - NSEI: '1001'
      GB\_FLEX: YES
    mod_gbnsecfgpara_list_2:
    - PARAINDEX: '1'
      GB\_FLEX: YES
    add_resrec_list:
    - TYPE: A
      NAME: MNC000.MCC123.gprs
      DOMAIN: RAC0001.LAC0011
      IP: 10.166.155.2
    add_resrec_list_1:
    - TYPE: A
      NAME: MNC000.MCC123.gprs
      DOMAIN: RAC0001.LAC0011
      IP: 10.166.153.1
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 准备阶段。

#### 1.1 割接前一周，检查待组建POOL的各SGSN的MML脚本，进行割接前的相关事项检查，并确保相关接口功能已配置完成。确认无误后，务必备份各SGSN的MML脚本。

#### 1.2 割接前3天，提前准备以下脚本，并完成和华为技术支持的审核确认。

##### 1.2.1 各SGSN与待割接的BSC的新建Gb接口配置脚本。

##### 1.2.2 各SGSN上的POOL配置相关脚本。

##### 1.2.3 DNS Server（可能是客户设备）上的配置脚本。

#### 待割接的BSC1当前所连接的SGSN上已经有此BSC1相关的配置数据，不用新增，只需在其他SGSN上配置BSC1相关数据。

### 2 配置同步阶段。

#### 2.1 割接前一天或当晚，在各SGSN上，加载License文件，License中开启Gb-flex功能（LKV2GBFLEX02）、“SGSN负荷分担”功能(可选)、SGSN Pool用户迁移（可选，LKV2SGSNMG02）功能。

#### 2.2 割接前一天或当晚，在U2020/MAE上，加载支持SGSN POOL管理的License文件。（包括SGSN Pool管理、SGSN Pool负载均衡管理、SGSN Pool用户定位。）

#### 2.3 各SGSN配置参数同步。

#### 比如移动性管理，会话管理相关配置。

### 3 设置SGSN1的Pool ID和NRI长度。

```jinja2
{%- for item in add_pool_list -%}
    ADD POOL:
    {#- --- 必选参数 --- -#}
    POOLID={{item.POOLID}},
    NRILENGTH={{item.NRILENGTH}},
    ;
{%- endfor -%}
```

### 目前NRI长度等于7bit仅在中国部署。在海外部署时，NRI长度采用5bit。

### 配置举例以配置SGSN1为例，SGSN2、SGSN3配置类似。

### 4 在SGSN1上配置本局NRI信息，在P-TMSI分配时将填写设定的NRI值。

```jinja2
{%- for item in add_localnri_list -%}
    ADD LOCALNRI:
    {#- --- 必选参数 --- -#}
    POOLID={{item.POOLID}},
    NRIVBGN={{item.NRIVBGN}},
    NRINUM={{item.NRINUM}},
    ;
{%- endfor -%}
```

### 在用户迁移过程中，不可以通过ADD LOCALNRI增加本局NRI。

### 不建议在高峰期执行ADD LOCALNRI命令。如果在高峰期执行ADD LOCALNRI命令失败，请执行如下命令，直到执行ADD LOCALNRI命令成功为止（以增加一条POOLID为1，NRI的值为10，NRI个数为1的本局NRI失败为例）。

```jinja2
{%- for item in blk_localnri_list -%}
    BLK LOCALNRI:
    {#- --- 必选参数 --- -#}
    POOLID={{item.POOLID}},
    NRIVBGN={{item.NRIVBGN}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in rmv_localnri_list -%}
    RMV LOCALNRI:
    {#- --- 必选参数 --- -#}
    POOLID={{item.POOLID}},
    NRIVBGN={{item.NRIVBGN}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_localnri_list_1 -%}
    ADD LOCALNRI:
    {#- --- 必选参数 --- -#}
    POOLID={{item.POOLID}},
    NRIVBGN={{item.NRIVBGN}},
    NRINUM={{item.NRINUM}},
    ;
{%- endfor -%}
```

### 5 配置SGSN1侧的CN ID。

```jinja2
{%- for item in set_sys_list -%}
    SET SYS:
    {#- --- 可选参数 --- -#}
    {%- if item.CNID is not none -%}
        CNID={{item.CNID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置SGSN1的Pool参数。

#### 6.1 在SGSN1上配置Pool区内其他SGSN的NRI信息。

```jinja2
{%- for item in add_poolnri_list -%}
    ADD POOLNRI:
    {#- --- 必选参数 --- -#}
    POOLID={{item.POOLID}},
    NRIV={{item.NRIV}},
    IPTYPE={{item.IPTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.SGSNN is not none -%}
        SGSNN="{{item.SGSNN}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPV4/IPV4V6 时必选 --- -#}
    {%- if item.IPTYPE in ['IPV4', 'IPV4V6'] -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV4V6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4V6' -%}
        ALTERNATIVE="{{item.ALTERNATIVE}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 6.2 SGSN1（待割接BSC直连的SGSN）上的待割接BSC的Flex开关。

##### 6.2.1 方案一

##### 在SGSN1（待割接BSC直连的SGSN）上打开待割接BSC的Flex开关。

###### 6.2.1.1 Gb接口静态配置：**MOD NSE**: NSEI=1001, GB\_FLEX=YES;

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_nse_list的变量区（command: MOD NSE） -#}
<!-- MISSING_MACRO: command=MOD NSE list_name=mod_nse_list step_id=6.2.1.1 -->
```

###### 6.2.1.2 Gb接口动态自动配置：**MOD GBNSECFGPARA**: PARAINDEX=1, GB\_FLEX=YES;

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_gbnsecfgpara_list的变量区（command: MOD GBNSECFGPARA） -#}
<!-- MISSING_MACRO: command=MOD GBNSECFGPARA list_name=mod_gbnsecfgpara_list step_id=6.2.1.2 -->
```

##### 这里需要添加该配置的SGSN为直连SGSN，比如BSC1原来连接的是SGSN1，则在组SGSN POOL的时候只有SGSN1需要执行此操作，SGSN2和SGSN3在配置的时候不需要执行。

##### 6.2.2 方案二

##### 在这里不打开SGSN1（原SGSN）上待割接BSC的Flex开关。

#### 6.3 可选:系统已销售和支持迁移功能时需执行，在各个SGSN上，配置规划好的OFFLOADINFO（配置本SGSN迁移数据）和NONRAI（在本SGSN上增加Pool区内其它SGSN的非广播路由区信息）。

```jinja2
{%- if is_optional_offloadinfo_nonrai_config -%}
    {%- for item in set_offloadinf_list -%}
        SET OFFLOADINF:
        {#- --- 可选参数 --- -#}
        {%- if item.OFFLOADTMR is not none -%}
            OFFLOADTMR={{item.OFFLOADTMR}},
        {%- endif -%}
        {%- if item.FIRSTTM is not none -%}
            FIRSTTM={{item.FIRSTTM}},
        {%- endif -%}
        {%- if item.NONRAI is not none -%}
            NONRAI="{{item.NONRAI}}",
        {%- endif -%}
        {%- if item.POOLID is not none -%}
            POOLID={{item.POOLID}},
        {%- endif -%}
        {%- if item.NULLNRIV is not none -%}
            NULLNRIV={{item.NULLNRIV}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_offloadinfo_nonrai_config -%}
    {%- for item in add_nonrai_list -%}
        ADD NONRAI:
        {#- --- 必选参数 --- -#}
        NONRAI="{{item.NONRAI}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IPTYPE is not none -%}
            IPTYPE={{item.IPTYPE}},
        {%- endif -%}
        {%- if item.SGSNN is not none -%}
            SGSNN="{{item.SGSNN}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPTYPE=IPV4/IPV4V6 时必选 --- -#}
        {%- if item.IPTYPE in ['IPV4', 'IPV4V6'] -%}
            IPV4="{{item.IPV4}}",
        {%- endif -%}
        {#- --- 条件必选：IPTYPE=IPV4V6 时必选 --- -#}
        {%- if item.IPTYPE == 'IPV4V6' -%}
            ALTERNATIVE="{{item.ALTERNATIVE}}",
        {%- endif -%}
        {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
        {%- if item.IPTYPE == 'IPV6' -%}
            IPV6="{{item.IPV6}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.4 打开SGSN1 license控制配置中的Gb-flex开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 6.5 如果SGSN是使用UNC作为融合节点支持MME POOL，在SGSN1上配置Mapping的GUMMEI。

##### 6.5.1 如果值配置LAC，会向MME连接的所有eNodeb下发对应的Mapping的GUMMEI。

```jinja2
{%- if is_scenario_lac_only -%}
    {%- for item in add_poolla_list -%}
        ADD POOLLA:
        {#- --- 必选参数 --- -#}
        LAC="{{item.LAC}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 6.5.2 配置TA和LA的对应关系，只向LA对应的TA所覆盖的eNodeb下发响应的Mapping的GUMMEI。

```jinja2
{%- if is_scenario_ta_la_mapping -%}
    {%- for item in add_poolla_list_3 -%}
        ADD POOLLA:
        {#- --- 必选参数 --- -#}
        LAC="{{item.LAC}}",
        {#- --- 可选参数 --- -#}
        {%- if item.BGNTAI is not none -%}
            BGNTAI="{{item.BGNTAI}}",
        {%- endif -%}
        {%- if item.ENDTAI is not none -%}
            ENDTAI="{{item.ENDTAI}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### POOLLA只有在融合节点同时支持SGSN POOL和MME POOL的时候才需要配置，支持一个POOL时，不需要。

#### 6.6 在SGSN1上打开鉴权开关。

##### 6.6.1 方案一

##### 打开2G鉴权开关（包括PDP激活鉴权开关、签名不匹配开关和无签名开关）。

```jinja2
{%- if is_scenario_scheme1 -%}
    {%- for item in mod_gbauthciph_list -%}
        MOD GBAUTHCIPH:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.SECPLC is not none -%}
            SECPLC={{item.SECPLC}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=SPECIAL_USER 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_USER' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHEVENT is not none -%}
                AUTHEVENT={{item.AUTHEVENT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.ATTSAUTH is not none -%}
                ATTSAUTH={{item.ATTSAUTH}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHEVENTTHRESHOLD is not none -%}
                AUTHEVENTTHRESHOLD={{item.AUTHEVENTTHRESHOLD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHPERIOD is not none -%}
                AUTHPERIOD={{item.AUTHPERIOD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHSETSNUMBER is not none -%}
                AUTHSETSNUMBER={{item.AUTHSETSNUMBER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHSETV2 is not none -%}
                AUTHSETV2={{item.AUTHSETV2}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.CAFTIMES is not none -%}
                CAFTIMES={{item.CAFTIMES}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
            {%- if item.CIPHALG is not none -%}
                CIPHALG={{item.CIPHALG}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.GETAUTHADVTH is not none -%}
                GETAUTHADVTH={{item.GETAUTHADVTH}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
            {%- if item.NCIPH is not none -%}
                NCIPH={{item.NCIPH}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.PREGETAUTHSETS is not none -%}
                PREGETAUTHSETS={{item.PREGETAUTHSETS}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.RAUSAUTH is not none -%}
                RAUSAUTH={{item.RAUSAUTH}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.RNUM is not none -%}
                RNUM={{item.RNUM}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
            {%- if item.XIDRESET is not none -%}
                XIDRESET={{item.XIDRESET}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 6.6.2 方案二

##### 本步骤不执行任何操作，直接进行后续操作。

#### 6.7 打开P-TMSI重分配开关。

```jinja2
{%- for item in set_gmmptmsirealloc_list -%}
    SET GMMPTMSIREALLOC:
    {#- --- 可选参数 --- -#}
    {%- if item.WITHRAUPROC is not none -%}
        WITHRAUPROC={{item.WITHRAUPROC}},
    {%- endif -%}
    {%- if item.REALLOCTMR is not none -%}
        REALLOCTMR={{item.REALLOCTMR}},
    {%- endif -%}
    {%- if item.REALLOCCOND is not none -%}
        REALLOCCOND={{item.REALLOCCOND}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 6.8 P-TMSI重分配完成。

##### 6.8.1 方案一

##### 经过1.5个周期路由更新时长，P-TMSI重分配完成之后，在各SGSN上恢复2G鉴权开关，再进行后续操作。

```jinja2
{%- if is_scenario_scheme1 -%}
    {%- for item in mod_gbauthciph_list_1 -%}
        MOD GBAUTHCIPH:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.SECPLC is not none -%}
            SECPLC={{item.SECPLC}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=SPECIAL_USER 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_USER' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHEVENT is not none -%}
                AUTHEVENT={{item.AUTHEVENT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.ATTSAUTH is not none -%}
                ATTSAUTH={{item.ATTSAUTH}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHEVENTTHRESHOLD is not none -%}
                AUTHEVENTTHRESHOLD={{item.AUTHEVENTTHRESHOLD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHPERIOD is not none -%}
                AUTHPERIOD={{item.AUTHPERIOD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHSETSNUMBER is not none -%}
                AUTHSETSNUMBER={{item.AUTHSETSNUMBER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHSETV2 is not none -%}
                AUTHSETV2={{item.AUTHSETV2}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.CAFTIMES is not none -%}
                CAFTIMES={{item.CAFTIMES}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
            {%- if item.CIPHALG is not none -%}
                CIPHALG={{item.CIPHALG}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.GETAUTHADVTH is not none -%}
                GETAUTHADVTH={{item.GETAUTHADVTH}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
            {%- if item.NCIPH is not none -%}
                NCIPH={{item.NCIPH}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.PREGETAUTHSETS is not none -%}
                PREGETAUTHSETS={{item.PREGETAUTHSETS}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.RAUSAUTH is not none -%}
                RAUSAUTH={{item.RAUSAUTH}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.RNUM is not none -%}
                RNUM={{item.RNUM}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
            {%- if item.XIDRESET is not none -%}
                XIDRESET={{item.XIDRESET}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 鉴权开关的恢复取值需要根据原有配置规划或网络状态进行。

##### 6.8.2 方案二

##### 本步骤不执行任何操作，直接进行后续操作。

### 7 重复上述步骤3~7，配置其他SGSN的Pool参数，本例中需要配置SGSN2、SGSN3的数据。

### 8 各SGSN配置完成后，执行Flex功能检查，详细检查项如表1所示。

### **表1** Flex功能Checklist

### | Flex功能检查 | 要求结果 |

### | --- | --- |

### | 鉴权开关 | 与规划数据一致 |

### | 系统容量 | 和规划一致 |

### | Pool ID | 一致 |

### | NRI长度 | 一致 |

### | CN ID | 不重复，与规划数据一致 |

### | Pool NRI | 所有SGSN均配置了Pool内其他SGSN的NRI和IP地址的对应关系，且IP地址配置一致。 |

### | 建立待割接的第一个BSC的所有RAI的性能测量任务 | 已经建立 |

### | OFFLOADINFO（可选） | 与规划数据一致 |

### | NONRAI | 不重复，与规划数据一致 |

### | Local NRI | 不重复，与规划数据一致 |

### | POOLLA | 与规划数据一致 |

### | license控制(LICENSESWITCH) | Gb-flex开启 |

### 9 割接阶段。

### 第一次割接（预割接）2个或1个BSC，按照如下几个方面进行操作。

### 在大容量局点，推荐首次测试或预割接时必须同时有2个BSC，目的是预割接时充分验证2个BSCPTMSI\_ATTACH-1的POOL负荷分担效果以及POOL内Intra-RAU流程发生时的NRI分配效果。

### 此配置举例以割接BSC1为例，BSC2、BSC3割接过程类似。

#### 9.1 **可选：**仅方案二需要执行此步骤：在SGSN1上打开鉴权开关。

#### 打开2G鉴权开关（包括2G PDP激活鉴权开关、签名不匹配开关和无签名开关）。

```jinja2
{%- if is_optional_open_auth_switch and is_scenario_scheme2 -%}
    {%- for item in mod_gbauthciph_list_2 -%}
        MOD GBAUTHCIPH:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.SECPLC is not none -%}
            SECPLC={{item.SECPLC}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=SPECIAL_USER 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_USER' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHEVENT is not none -%}
                AUTHEVENT={{item.AUTHEVENT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.ATTSAUTH is not none -%}
                ATTSAUTH={{item.ATTSAUTH}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHEVENTTHRESHOLD is not none -%}
                AUTHEVENTTHRESHOLD={{item.AUTHEVENTTHRESHOLD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHPERIOD is not none -%}
                AUTHPERIOD={{item.AUTHPERIOD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHSETSNUMBER is not none -%}
                AUTHSETSNUMBER={{item.AUTHSETSNUMBER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.AUTHSETV2 is not none -%}
                AUTHSETV2={{item.AUTHSETV2}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.CAFTIMES is not none -%}
                CAFTIMES={{item.CAFTIMES}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
            {%- if item.CIPHALG is not none -%}
                CIPHALG={{item.CIPHALG}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.GETAUTHADVTH is not none -%}
                GETAUTHADVTH={{item.GETAUTHADVTH}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
            {%- if item.NCIPH is not none -%}
                NCIPH={{item.NCIPH}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.PREGETAUTHSETS is not none -%}
                PREGETAUTHSETS={{item.PREGETAUTHSETS}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.RAUSAUTH is not none -%}
                RAUSAUTH={{item.RAUSAUTH}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHONLY/AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC in ['AUTHONLY', 'AUTHANDPROTECTED'] -%}
            {%- if item.RNUM is not none -%}
                RNUM={{item.RNUM}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
        {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
            {%- if item.XIDRESET is not none -%}
                XIDRESET={{item.XIDRESET}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 9.2 按照之前准备的脚本，配置新增连接的BSC与SGSN之间的链路数据，调通Gb链路。

##### 9.2.1 核心网侧：在各SGSN上，分别配置与各个待割接的BSC的Gb接口IP链路数据，然后调通Gb接口链路。

##### 9.2.2 无线侧：在各个待割接的BSC上，分别配置与各个SGSN之间的Gb接口链路数据，然后调通Gb接口链路。

#### 9.3 核心网SGSN侧

##### 9.3.1 BSC的Flex开关

###### 9.3.1.1 方案一

###### 在SGSN2、SGSN3（割接前非直连SGSN）上，打开待割接BSC的Flex开关：

####### 9.3.1.1.1 Gb接口静态配置：**MOD NSE**: NSEI=1002, GB\_FLEX=YES;

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_nse_list_1的变量区（command: MOD NSE） -#}
<!-- MISSING_MACRO: command=MOD NSE list_name=mod_nse_list_1 step_id=9.3.1.1.1 -->
```

####### 9.3.1.1.2 Gb接口动态自动配置：**MOD GBNSECFGPARA**: PARAINDEX=1, GB\_FLEX=YES;

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_gbnsecfgpara_list_1的变量区（command: MOD GBNSECFGPARA） -#}
<!-- MISSING_MACRO: command=MOD GBNSECFGPARA list_name=mod_gbnsecfgpara_list_1 step_id=9.3.1.1.2 -->
```

###### 对于方案一，割接前直连的SGSN1的该配置在组SGSN Pool的时候已经修改了，本步骤不需要再修改。

###### 9.3.1.2 方案二

###### 在POOL内所有SGSN上打开待割接BSC的Flex开关：

####### 9.3.1.2.1 Gb接口静态配置：**MOD NSE**: NSEI=1001, GB\_FLEX=YES;

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_nse_list_2的变量区（command: MOD NSE） -#}
<!-- MISSING_MACRO: command=MOD NSE list_name=mod_nse_list_2 step_id=9.3.1.2.1 -->
```

####### 9.3.1.2.2 Gb接口动态自动配置：**MOD GBNSECFGPARA**: PARAINDEX=1, GB\_FLEX=YES;

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_gbnsecfgpara_list_2的变量区（command: MOD GBNSECFGPARA） -#}
<!-- MISSING_MACRO: command=MOD GBNSECFGPARA list_name=mod_gbnsecfgpara_list_2 step_id=9.3.1.2.2 -->
```

##### 9.3.2 检查2G的PAGING表是否上报

##### 2G的PAGING表是自动上报的，链路配置完成之后，使用命令检查LST GBPAGING，查询小区上报是否符合规划。

#### 9.4 DNS Server上的Default SGSN配置。

#### Default SGSN需要基于路由区进行规划，且保证分摊均匀。其中的路由区包括待割接BSC下所有POOL内的RAI。

#### 考虑容灾备份，最好对同一个路由区至少有两个SGSN互为备份。本例中，对于域名“LAC0011.RAC0001.MNC000.MCC123.GPRS.”，将SGSN1和SGSN2配置为Default SGSN，即在DNS上将BSC1的路由区域名解析成为SGSN1和SGSN2的GTPC地址。并通知与该BSC1覆盖范围相邻的非本SGSN Pool的其他SGSN做相应的数据修改。

#### 通常地，本网内有一个本地DNS Server，上一级DNS Server不在本地。这种情况下，当核心网内多个SGSN改造成POOL后，该DNS Server可以视作POOL外的DNS Server，也可以视作POOL内的DNS Server，它除了保留原有的域名解析数据、解析功能外，还需要为SGSN POOL增加Default SGSN的数据配置。以华为DNS Server为例：

##### 9.4.1 方式一：在华为DNS Server的LMT上配置，主备均需要：

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_resrec_list的变量区（command: ADD RESREC） -#}
<!-- MISSING_MACRO: command=ADD RESREC list_name=add_resrec_list step_id=9.4.1 -->
```

##### 9.4.2 方式二：在不带LMT的DNS Server上，在named.ra文件中增加A记录（详细参见《DNS产品文档》）：

##### RAC0001.LAC0011

##### IN       A        10.166.155.2

#### 以下为DNS Server上原有配置，不需新增：

##### 9.4.3 方式一：在华为DNS Server上：

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_resrec_list_1的变量区（command: ADD RESREC） -#}
<!-- MISSING_MACRO: command=ADD RESREC list_name=add_resrec_list_1 step_id=9.4.3 -->
```

##### 9.4.4 方式二：在不带LMT的DNS Server上：

##### RAC0001.LAC0011                       IN       A        10.166.153.1

##### 9.4.5 如果本网的运营商除了本地DNS Server外，还有上一级的DNS Server也在本地，在改造成SGSN POOL后，POOL内有一个DNS Server A，POOL外还有一个上级的DNS Server B，则，Default SGSN的数据配置就需要在DNS Server B上完成。这种情况比较少见。

##### 9.4.6 如果POOL内某个SGSN下扩容BSC/RNC网元，在POOL内的DNS Server上，需要在扩容操作阶段，新增加该BSC/RNC的全部RAI的相关A记录（对应哪几个SGSN作为DefaultSGSN，需在扩容前完成规划），并且增加RNCID的相关A记录。

##### 9.4.7 修改了DNS服务器上的配置的，需要在清除各SGSN的cash记录。

#### 9.5 BSC上的配置。

##### 9.5.1 在待割接的BSC上，配置各SGSN的NRI长度、CN ID、NRI数值、负荷分担比例。

##### 该步骤可在割接前提前完成。

##### 9.5.2 在待割接的BSC上，打开Gb-flex开关（不同厂家可能实现不同，如无具体命令，则有相应Flex启动或生效的类似操作）。

##### 该步骤在割接当晚，上述全部操作（SGSN侧、DNS Server、RAN侧）完成后，执行。

#### 9.6 核心网配置检查。

#### **表2** 核心网配置检查Checklist

#### | 核心网配置检查 | 要求结果 |

#### | --- | --- |

#### | 鉴权开关（Inter RAU 、2G PDP激活鉴权、Attach、签名不匹配、无签名等） | 打开 |

#### | P-TMSI重分配开关 | 打开 |

#### | BSC | Flex开关已打开 |

#### | DNS | 配置与规划一致 |

#### 9.7 接入网络测试（对割接入的BSC进行业务拨测）。

##### 9.7.1 基本上网业务拨测。

##### 9.7.2 POOL功能业务拨测。

##### 如果拨测失败且无法定位，Pool基本功能验证失败，需收集各设备上的配置信息和相关，进行POOL回退，参见Pool改造回退。

##### 9.7.3 拨测成功后，观察网络运行状况。

###### 9.7.3.1 观察割接后SGSN的话统指标，在各个SGSN侧观察激活成功率，附着成功率，路由更新成功率的指标，其指标应该与割接前基本保持一致，以及BSC侧的话统结果，如果指标明显异常，需要倒回，参见Pool改造回退。

###### 9.7.3.2 观察各SGSN和U2020/MAE上的告警。

###### 9.7.3.3 在U2020/MAE上组建SGSN POOL，将已进入POOL运行状态的各个SGSN纳入SGSN POOL，进行后续SGSN POOL管理。在U2020/MAE上登记SGSN POOL的相关KPI指标（具体参见U2020/MAE上的界面操作指导）。

##### 9.7.4 在割接后的第二天及一周内观察和分析相应数据是否正常。

##### 割接后话统明显异常，需要启动倒回流程，参见Pool改造回退。

#### 9.8 **可选：**仅方案二需要执行此步骤：等待P-TMSI重分配完成。

#### 需要经过1.5个周期路由更新时长，P-TMSI重分配完成之后，在各SGSN上恢复割接之前鉴权开关，再进行后续操作。

#### 9.9 重复步骤a~h，以相同的方式割接剩余的BSC，本例中为BSC2、BSC3。

### 10 在各SGSN上执行用户迁移保证负荷均衡。

### 具体请参见《U2020 MBB网络管理系统 虚拟化产品文档》 / 《iMaster MAE产品文档》的手工迁移用户部分。

