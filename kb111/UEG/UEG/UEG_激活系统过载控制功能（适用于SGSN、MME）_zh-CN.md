---
id: GWFD-021401
name: 激活系统过载控制功能（适用于SGSN、MME）
ne_type: UEG
type: feature
description: 在系统过载时，UEG通过控制接入系统的业务量来防止拥塞进一步恶化而造成整系统的瘫痪，从而保证了自身处理业务的稳定性和高优先级业务（如语音业务）的成功率。  适用于SGSN、MME。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-021400 可靠性功能","GWFD-021401 系统过载控制功能","激活系统过载控制功能（适用于SGSN、MME）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
在系统过载时，UEG通过控制接入系统的业务量来防止拥塞进一步恶化而造成整系统的瘫痪，从而保证了自身处理业务的稳定性和高优先级业务（如语音业务）的成功率。适用于SGSN、MME。

## 必备事项
前提条件

请仔细阅读GWFD-021401系统过载控制功能特性概述（适用于SGSN、MME）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_intermmefc_list:
      type: items
      properties:
        FCSWITCH:
          name: 'InterMME接入流控功能开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '设置Inter-MME流控参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MINTHD:
          name: '流控速率最小值'
          type: integer
          minimum: 0
          maximum: 5000
          required: false
          description: '设置Inter-MME流控参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MAXTHD:
          name: '流控速率最大值'
          type: integer
          minimum: 0
          maximum: 5000
          required: false
          description: '设置Inter-MME流控参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_s1pagingfc_list:
      type: items
      properties:
        FCSWITCH:
          name: 'S1寻呼流控功能开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '设置S1寻呼流控参数。  开启PAE寻呼反压流控开关时，还需要通过SET PAECHECKPARA、SET PAECHECKTHD、SET REVERSEFCPARA设置PAE寻呼反压流控相关参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SGSSWITCH:
          name: 'SGs寻呼流控开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '设置S1寻呼流控参数。  开启PAE寻呼反压流控开关时，还需要通过SET PAECHECKPARA、SET PAECHECKTHD、SET REVERSEFCPARA设置PAE寻呼反压流控相关参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        S102SWITCH:
          name: 'S102寻呼流控开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '设置S1寻呼流控参数。  开启PAE寻呼反压流控开关时，还需要通过SET PAECHECKPARA、SET PAECHECKTHD、SET REVERSEFCPARA设置PAE寻呼反压流控相关参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PAGINGRESENDSWITCH:
          name: '寻呼重发控制开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '设置S1寻呼流控参数。  开启PAE寻呼反压流控开关时，还需要通过SET PAECHECKPARA、SET PAECHECKTHD、SET REVERSEFCPARA设置PAE寻呼反压流控相关参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ANTIBURSTSWITCH:
          name: '寻呼突发预防功能开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '设置S1寻呼流控参数。  开启PAE寻呼反压流控开关时，还需要通过SET PAECHECKPARA、SET PAECHECKTHD、SET REVERSEFCPARA设置PAE寻呼反压流控相关参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PAEFCSWITCH:
          name: 'PAE反压流控功能开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '设置S1寻呼流控参数。  开启PAE寻呼反压流控开关时，还需要通过SET PAECHECKPARA、SET PAECHECKTHD、SET REVERSEFCPARA设置PAE寻呼反压流控相关参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FCTHD:
          name: '寻呼流控速率门限'
          type: integer
          minimum: 10
          maximum: 255
          required: false
          description: '设置S1寻呼流控参数。  开启PAE寻呼反压流控开关时，还需要通过SET PAECHECKPARA、SET PAECHECKTHD、SET REVERSEFCPARA设置PAE寻呼反压流控相关参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FCTHDMIN:
          name: '寻呼流控速率最小值'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: '设置S1寻呼流控参数。  开启PAE寻呼反压流控开关时，还需要通过SET PAECHECKPARA、SET PAECHECKTHD、SET REVERSEFCPARA设置PAE寻呼反压流控相关参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RSVCAP:
          name: '寻呼预留处理量'
          type: integer
          minimum: 0
          maximum: 50
          required: false
          description: '设置S1寻呼流控参数。  开启PAE寻呼反压流控开关时，还需要通过SET PAECHECKPARA、SET PAECHECKTHD、SET REVERSEFCPARA设置PAE寻呼反压流控相关参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RSVVOCAP:
          name: '语音寻呼预留处理量'
          type: integer
          minimum: 0
          maximum: 50
          required: false
          description: '设置S1寻呼流控参数。  开启PAE寻呼反压流控开关时，还需要通过SET PAECHECKPARA、SET PAECHECKTHD、SET REVERSEFCPARA设置PAE寻呼反压流控相关参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_paecheckpara_list:
      type: items
      properties:
        CHECKINTERVAL:
          name: '检测间隔(s)'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: '通过**SET S1PAGINGFC**开启PAE寻呼反压流控开关时，需要设置PAE寻呼反压流控相关参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CHECKTIMES:
          name: '检测次数'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: '通过**SET S1PAGINGFC**开启PAE寻呼反压流控开关时，需要设置PAE寻呼反压流控相关参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_paecheckthd_list:
      type: items
      properties:
        RESTYPE:
          name: '资源类型'
          type: string
          enum:
          - PBUF
          - SHAREQUEUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TRIGTHD:
          name: '触发过载阈值（%）'
          type: integer
          minimum: 2
          maximum: 99
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RESUMTHD:
          name: '触发过载恢复阈值（%）'
          type: integer
          minimum: 2
          maximum: 99
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_reversefcpara_list:
      type: items
      properties:
        CTRLPLCY:
          name: '控制策略'
          type: string
          enum:
          - INSTANCENUM
          - PERCENT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PERCENTTRGTHD:
          name: '过载阈值（%）'
          type: integer
          minimum: 1
          maximum: 99
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PERCENTRESUMTHD:
          name: '恢复阈值（%）'
          type: integer
          minimum: 0
          maximum: 99
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_softparaofbit_list:
      type: items
      properties:
        DT:
          name: '参数类型'
          type: string
          enum:
          - BYTE
          - BYTE_EX
          - BYTE_EX_B
          - DWORD
          - DWORD_EX
          - DWORD_EX_B
          required: true
          description: '配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PARANUM:
          name: '参数索引'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VALUE:
          name: '参数值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: '配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: '配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_flowctrlpara_list:
      type: items
      properties:
        WEIGHTMODE:
          name: '业务权重获取方式'
          type: string
          enum:
          - CFG
          - LEARN
          required: false
          description: '设置流控系统参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PROCTYPE:
          name: '进程类型'
          type: string
          enum:
          - GBP
          - SGP
          - SPP
          - UPP
          required: false
          description: '设置流控系统参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MINWAL:
          name: '窗口最小值'
          type: integer
          minimum: 0
          maximum: 20000
          required: false
          description: '设置流控系统参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MAXWAL:
          name: '窗口最大值'
          type: integer
          minimum: 0
          maximum: 20000
          required: false
          description: '设置流控系统参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MINWAL_GBDATA:
          name: '2G用户面窗口最小值'
          type: integer
          minimum: 0
          maximum: 20000
          required: false
          description: '设置流控系统参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MAXWAL_GBDATA:
          name: '2G用户面窗口最大值'
          type: integer
          minimum: 0
          maximum: 20000
          required: false
          description: '设置流控系统参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MAXWAL_GBPAGING:
          name: '2G寻呼窗口最大值'
          type: integer
          minimum: 0
          maximum: 20000
          required: false
          description: '设置流控系统参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DROPRATETHD:
          name: '丢包率告警阈值'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: '设置流控系统参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_flowctrlque_list:
      type: items
      properties:
        APPTYPE:
          name: '业务类型'
          type: string
          enum:
          - APP_2G
          - APP_3G
          - APP_4G
          required: true
          description: '设置流控队列信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MSG2GTYPE:
          name: '2G消息类型'
          type: string
          enum:
          - ATTACH
          - PDP_ACT
          - RAU
          required: false
          description: '设置流控队列信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        WEIGHT:
          name: '业务权重'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: '设置流控队列信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        QUELENTH:
          name: '队列期望长度'
          type: integer
          minimum: 0
          maximum: 10000
          required: false
          description: '设置流控队列信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MSG3GTYPE:
          name: '3G消息类型'
          type: string
          enum:
          - ATTACH
          - PDP_ACT
          - RAU
          - SERVICE_REQ
          required: false
          description: '设置流控队列信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MSG4GTYPE:
          name: '4G消息类型'
          type: string
          enum:
          - ATTACH
          - EMM_EMGC
          - EMM_VIP
          - EMM_VOICE
          - ENCRYPT
          - SERVICE_REQ
          - TAU
          required: false
          description: '设置流控队列信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_intermmefixfc_list:
      type: items
      properties:
        ATTACHFCSWITCH:
          name: 'Attach接入流控功能开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '设置Inter-MME接入固定速率流控功能的相关参数，对Inter-MME的ServiceRequest和AttachRequest消息分别进行流控。  说明：  * 该命令与**SET INTERMMEFC**不建议同时开启。同时开启时该命令优先级高于**SET INTERMMEFC**。 * 当“FCTYPE”为“PROCESS（单进程）”时：    + “ATTACHSCOPE”值为：      - “PROCESS（单进程）”：表示“ATTACHTHD”参数指定的值是单SGP进程每秒钟可以通过的Attach Request消息数。     - “SYSTEM（整系统）”：表示“ATTACHTHD”参数指定的值是整系统每秒钟可以通过的Attach Request消息数。每个SGP进程独立进行流控，整系统的流控阈值除以SGP进程个数作为每个SGP进程的流控阈值。   + “SRSCOPE”值为：     - “PROCESS（单进程）”：表示“SRTHD”参数指定的值是单SGP进程每秒钟可以通过的Service Request消息数。     - “SYSTEM（整系统）”：表示“SRTHD”参数指定的值是整系统每秒钟可以通过的Service Request消息数。每个SGP进程独立进行流控，整系统的流控阈值除以SGP进程个数作为每个SGP进程的流控阈值。 * 当“FCTYPE”为“POD（POD）”时：   + “ATTACHSCOPE”值为：      - “PROCESS（单进程）”：表示“ATTACHTHD”参数指定的值乘以LINK-POD中SGP进程个数，作为每个LINK-POD的Attach Request消息流控阈值。     - “SYSTEM（整系统）”：表示“ATTACHTHD”参数指定的值是整系统每秒钟可以通过的Attach Request消息数。每个LINK-POD独立进行流控，整系统的流控阈值除以LINK-POD个数作为每个LINK-POD的流控阈值。当部分Pod故障时，正常的Pod的流控阈值不变。   + “SRSCOPE”值为：     - “PROCESS（单进程）”：表示“SRTHD”参数指定的值乘以LINK-POD中SGP进程个数，作为每个LINK-POD的Service Request消息流控阈值。     - “SYSTEM（整系统）”：表示“SRTHD”参数指定的值乘以LINK-POD中SGP进程个数，数作为每个LINK-POD的Service Request消息流控阈值。当部分Pod故障时，正常的Pod的流控阈值不变。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SRFCSWITCH:
          name: 'SR接入流控功能开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '设置Inter-MME接入固定速率流控功能的相关参数，对Inter-MME的ServiceRequest和AttachRequest消息分别进行流控。  说明：  * 该命令与**SET INTERMMEFC**不建议同时开启。同时开启时该命令优先级高于**SET INTERMMEFC**。 * 当“FCTYPE”为“PROCESS（单进程）”时：    + “ATTACHSCOPE”值为：      - “PROCESS（单进程）”：表示“ATTACHTHD”参数指定的值是单SGP进程每秒钟可以通过的Attach Request消息数。     - “SYSTEM（整系统）”：表示“ATTACHTHD”参数指定的值是整系统每秒钟可以通过的Attach Request消息数。每个SGP进程独立进行流控，整系统的流控阈值除以SGP进程个数作为每个SGP进程的流控阈值。   + “SRSCOPE”值为：     - “PROCESS（单进程）”：表示“SRTHD”参数指定的值是单SGP进程每秒钟可以通过的Service Request消息数。     - “SYSTEM（整系统）”：表示“SRTHD”参数指定的值是整系统每秒钟可以通过的Service Request消息数。每个SGP进程独立进行流控，整系统的流控阈值除以SGP进程个数作为每个SGP进程的流控阈值。 * 当“FCTYPE”为“POD（POD）”时：   + “ATTACHSCOPE”值为：      - “PROCESS（单进程）”：表示“ATTACHTHD”参数指定的值乘以LINK-POD中SGP进程个数，作为每个LINK-POD的Attach Request消息流控阈值。     - “SYSTEM（整系统）”：表示“ATTACHTHD”参数指定的值是整系统每秒钟可以通过的Attach Request消息数。每个LINK-POD独立进行流控，整系统的流控阈值除以LINK-POD个数作为每个LINK-POD的流控阈值。当部分Pod故障时，正常的Pod的流控阈值不变。   + “SRSCOPE”值为：     - “PROCESS（单进程）”：表示“SRTHD”参数指定的值乘以LINK-POD中SGP进程个数，作为每个LINK-POD的Service Request消息流控阈值。     - “SYSTEM（整系统）”：表示“SRTHD”参数指定的值乘以LINK-POD中SGP进程个数，数作为每个LINK-POD的Service Request消息流控阈值。当部分Pod故障时，正常的Pod的流控阈值不变。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FCTYPE:
          name: '流控粒度'
          type: string
          enum:
          - POD
          - PROCESS
          required: false
          description: '设置Inter-MME接入固定速率流控功能的相关参数，对Inter-MME的ServiceRequest和AttachRequest消息分别进行流控。  说明：  * 该命令与**SET INTERMMEFC**不建议同时开启。同时开启时该命令优先级高于**SET INTERMMEFC**。 * 当“FCTYPE”为“PROCESS（单进程）”时：    + “ATTACHSCOPE”值为：      - “PROCESS（单进程）”：表示“ATTACHTHD”参数指定的值是单SGP进程每秒钟可以通过的Attach Request消息数。     - “SYSTEM（整系统）”：表示“ATTACHTHD”参数指定的值是整系统每秒钟可以通过的Attach Request消息数。每个SGP进程独立进行流控，整系统的流控阈值除以SGP进程个数作为每个SGP进程的流控阈值。   + “SRSCOPE”值为：     - “PROCESS（单进程）”：表示“SRTHD”参数指定的值是单SGP进程每秒钟可以通过的Service Request消息数。     - “SYSTEM（整系统）”：表示“SRTHD”参数指定的值是整系统每秒钟可以通过的Service Request消息数。每个SGP进程独立进行流控，整系统的流控阈值除以SGP进程个数作为每个SGP进程的流控阈值。 * 当“FCTYPE”为“POD（POD）”时：   + “ATTACHSCOPE”值为：      - “PROCESS（单进程）”：表示“ATTACHTHD”参数指定的值乘以LINK-POD中SGP进程个数，作为每个LINK-POD的Attach Request消息流控阈值。     - “SYSTEM（整系统）”：表示“ATTACHTHD”参数指定的值是整系统每秒钟可以通过的Attach Request消息数。每个LINK-POD独立进行流控，整系统的流控阈值除以LINK-POD个数作为每个LINK-POD的流控阈值。当部分Pod故障时，正常的Pod的流控阈值不变。   + “SRSCOPE”值为：     - “PROCESS（单进程）”：表示“SRTHD”参数指定的值乘以LINK-POD中SGP进程个数，作为每个LINK-POD的Service Request消息流控阈值。     - “SYSTEM（整系统）”：表示“SRTHD”参数指定的值乘以LINK-POD中SGP进程个数，数作为每个LINK-POD的Service Request消息流控阈值。当部分Pod故障时，正常的Pod的流控阈值不变。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ATTACHSCOPE:
          name: 'Attach Request流控阈值作用范围'
          type: string
          enum:
          - PROCESS
          - SYSTEM
          required: false
          description: '设置Inter-MME接入固定速率流控功能的相关参数，对Inter-MME的ServiceRequest和AttachRequest消息分别进行流控。  说明：  * 该命令与**SET INTERMMEFC**不建议同时开启。同时开启时该命令优先级高于**SET INTERMMEFC**。 * 当“FCTYPE”为“PROCESS（单进程）”时：    + “ATTACHSCOPE”值为：      - “PROCESS（单进程）”：表示“ATTACHTHD”参数指定的值是单SGP进程每秒钟可以通过的Attach Request消息数。     - “SYSTEM（整系统）”：表示“ATTACHTHD”参数指定的值是整系统每秒钟可以通过的Attach Request消息数。每个SGP进程独立进行流控，整系统的流控阈值除以SGP进程个数作为每个SGP进程的流控阈值。   + “SRSCOPE”值为：     - “PROCESS（单进程）”：表示“SRTHD”参数指定的值是单SGP进程每秒钟可以通过的Service Request消息数。     - “SYSTEM（整系统）”：表示“SRTHD”参数指定的值是整系统每秒钟可以通过的Service Request消息数。每个SGP进程独立进行流控，整系统的流控阈值除以SGP进程个数作为每个SGP进程的流控阈值。 * 当“FCTYPE”为“POD（POD）”时：   + “ATTACHSCOPE”值为：      - “PROCESS（单进程）”：表示“ATTACHTHD”参数指定的值乘以LINK-POD中SGP进程个数，作为每个LINK-POD的Attach Request消息流控阈值。     - “SYSTEM（整系统）”：表示“ATTACHTHD”参数指定的值是整系统每秒钟可以通过的Attach Request消息数。每个LINK-POD独立进行流控，整系统的流控阈值除以LINK-POD个数作为每个LINK-POD的流控阈值。当部分Pod故障时，正常的Pod的流控阈值不变。   + “SRSCOPE”值为：     - “PROCESS（单进程）”：表示“SRTHD”参数指定的值乘以LINK-POD中SGP进程个数，作为每个LINK-POD的Service Request消息流控阈值。     - “SYSTEM（整系统）”：表示“SRTHD”参数指定的值乘以LINK-POD中SGP进程个数，数作为每个LINK-POD的Service Request消息流控阈值。当部分Pod故障时，正常的Pod的流控阈值不变。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ATTACHTHD:
          name: 'Attach Request速率门限(个/秒)'
          type: integer
          minimum: 1
          maximum: 3133440
          required: false
          description: '设置Inter-MME接入固定速率流控功能的相关参数，对Inter-MME的ServiceRequest和AttachRequest消息分别进行流控。  说明：  * 该命令与**SET INTERMMEFC**不建议同时开启。同时开启时该命令优先级高于**SET INTERMMEFC**。 * 当“FCTYPE”为“PROCESS（单进程）”时：    + “ATTACHSCOPE”值为：      - “PROCESS（单进程）”：表示“ATTACHTHD”参数指定的值是单SGP进程每秒钟可以通过的Attach Request消息数。     - “SYSTEM（整系统）”：表示“ATTACHTHD”参数指定的值是整系统每秒钟可以通过的Attach Request消息数。每个SGP进程独立进行流控，整系统的流控阈值除以SGP进程个数作为每个SGP进程的流控阈值。   + “SRSCOPE”值为：     - “PROCESS（单进程）”：表示“SRTHD”参数指定的值是单SGP进程每秒钟可以通过的Service Request消息数。     - “SYSTEM（整系统）”：表示“SRTHD”参数指定的值是整系统每秒钟可以通过的Service Request消息数。每个SGP进程独立进行流控，整系统的流控阈值除以SGP进程个数作为每个SGP进程的流控阈值。 * 当“FCTYPE”为“POD（POD）”时：   + “ATTACHSCOPE”值为：      - “PROCESS（单进程）”：表示“ATTACHTHD”参数指定的值乘以LINK-POD中SGP进程个数，作为每个LINK-POD的Attach Request消息流控阈值。     - “SYSTEM（整系统）”：表示“ATTACHTHD”参数指定的值是整系统每秒钟可以通过的Attach Request消息数。每个LINK-POD独立进行流控，整系统的流控阈值除以LINK-POD个数作为每个LINK-POD的流控阈值。当部分Pod故障时，正常的Pod的流控阈值不变。   + “SRSCOPE”值为：     - “PROCESS（单进程）”：表示“SRTHD”参数指定的值乘以LINK-POD中SGP进程个数，作为每个LINK-POD的Service Request消息流控阈值。     - “SYSTEM（整系统）”：表示“SRTHD”参数指定的值乘以LINK-POD中SGP进程个数，数作为每个LINK-POD的Service Request消息流控阈值。当部分Pod故障时，正常的Pod的流控阈值不变。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SRSCOPE:
          name: 'Service Request流控阈值作用范围'
          type: string
          enum:
          - PROCESS
          - SYSTEM
          required: false
          description: '设置Inter-MME接入固定速率流控功能的相关参数，对Inter-MME的ServiceRequest和AttachRequest消息分别进行流控。  说明：  * 该命令与**SET INTERMMEFC**不建议同时开启。同时开启时该命令优先级高于**SET INTERMMEFC**。 * 当“FCTYPE”为“PROCESS（单进程）”时：    + “ATTACHSCOPE”值为：      - “PROCESS（单进程）”：表示“ATTACHTHD”参数指定的值是单SGP进程每秒钟可以通过的Attach Request消息数。     - “SYSTEM（整系统）”：表示“ATTACHTHD”参数指定的值是整系统每秒钟可以通过的Attach Request消息数。每个SGP进程独立进行流控，整系统的流控阈值除以SGP进程个数作为每个SGP进程的流控阈值。   + “SRSCOPE”值为：     - “PROCESS（单进程）”：表示“SRTHD”参数指定的值是单SGP进程每秒钟可以通过的Service Request消息数。     - “SYSTEM（整系统）”：表示“SRTHD”参数指定的值是整系统每秒钟可以通过的Service Request消息数。每个SGP进程独立进行流控，整系统的流控阈值除以SGP进程个数作为每个SGP进程的流控阈值。 * 当“FCTYPE”为“POD（POD）”时：   + “ATTACHSCOPE”值为：      - “PROCESS（单进程）”：表示“ATTACHTHD”参数指定的值乘以LINK-POD中SGP进程个数，作为每个LINK-POD的Attach Request消息流控阈值。     - “SYSTEM（整系统）”：表示“ATTACHTHD”参数指定的值是整系统每秒钟可以通过的Attach Request消息数。每个LINK-POD独立进行流控，整系统的流控阈值除以LINK-POD个数作为每个LINK-POD的流控阈值。当部分Pod故障时，正常的Pod的流控阈值不变。   + “SRSCOPE”值为：     - “PROCESS（单进程）”：表示“SRTHD”参数指定的值乘以LINK-POD中SGP进程个数，作为每个LINK-POD的Service Request消息流控阈值。     - “SYSTEM（整系统）”：表示“SRTHD”参数指定的值乘以LINK-POD中SGP进程个数，数作为每个LINK-POD的Service Request消息流控阈值。当部分Pod故障时，正常的Pod的流控阈值不变。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SRTHD:
          name: 'Service Request速率门限(个/秒)'
          type: integer
          minimum: 1
          maximum: 3133440
          required: false
          description: '设置Inter-MME接入固定速率流控功能的相关参数，对Inter-MME的ServiceRequest和AttachRequest消息分别进行流控。  说明：  * 该命令与**SET INTERMMEFC**不建议同时开启。同时开启时该命令优先级高于**SET INTERMMEFC**。 * 当“FCTYPE”为“PROCESS（单进程）”时：    + “ATTACHSCOPE”值为：      - “PROCESS（单进程）”：表示“ATTACHTHD”参数指定的值是单SGP进程每秒钟可以通过的Attach Request消息数。     - “SYSTEM（整系统）”：表示“ATTACHTHD”参数指定的值是整系统每秒钟可以通过的Attach Request消息数。每个SGP进程独立进行流控，整系统的流控阈值除以SGP进程个数作为每个SGP进程的流控阈值。   + “SRSCOPE”值为：     - “PROCESS（单进程）”：表示“SRTHD”参数指定的值是单SGP进程每秒钟可以通过的Service Request消息数。     - “SYSTEM（整系统）”：表示“SRTHD”参数指定的值是整系统每秒钟可以通过的Service Request消息数。每个SGP进程独立进行流控，整系统的流控阈值除以SGP进程个数作为每个SGP进程的流控阈值。 * 当“FCTYPE”为“POD（POD）”时：   + “ATTACHSCOPE”值为：      - “PROCESS（单进程）”：表示“ATTACHTHD”参数指定的值乘以LINK-POD中SGP进程个数，作为每个LINK-POD的Attach Request消息流控阈值。     - “SYSTEM（整系统）”：表示“ATTACHTHD”参数指定的值是整系统每秒钟可以通过的Attach Request消息数。每个LINK-POD独立进行流控，整系统的流控阈值除以LINK-POD个数作为每个LINK-POD的流控阈值。当部分Pod故障时，正常的Pod的流控阈值不变。   + “SRSCOPE”值为：     - “PROCESS（单进程）”：表示“SRTHD”参数指定的值乘以LINK-POD中SGP进程个数，作为每个LINK-POD的Service Request消息流控阈值。     - “SYSTEM（整系统）”：表示“SRTHD”参数指定的值乘以LINK-POD中SGP进程个数，数作为每个LINK-POD的Service Request消息流控阈值。当部分Pod故障时，正常的Pod的流控阈值不变。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_softparaofbit_list_10:
      type: items
      properties:
        DT:
          name: '参数类型'
          type: string
          enum:
          - BYTE
          - BYTE_EX
          - BYTE_EX_B
          - DWORD
          - DWORD_EX
          - DWORD_EX_B
          required: true
          description: '控制系统中S1接口Inter-MME Service Request固定速率流控失效阈值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PARANUM:
          name: '参数索引'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '控制系统中S1接口Inter-MME Service Request固定速率流控失效阈值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VALUE:
          name: '参数值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: '控制系统中S1接口Inter-MME Service Request固定速率流控失效阈值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: '控制系统中S1接口Inter-MME Service Request固定速率流控失效阈值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_talistpagingcfg_list:
      type: items
      properties:
        TAC:
          name: '跟踪区域码'
          type: string
          maxLength: 6
          required: true
          description: '设置S1模式基于TALIST寻呼消息不重发的TAC区间，以及不重发的TAC区间对于IMS寻呼消息不生效。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TACRANGE:
          name: '跟踪区域码范围'
          type: string
          maxLength: 6
          required: false
          description: '设置S1模式基于TALIST寻呼消息不重发的TAC区间，以及不重发的TAC区间对于IMS寻呼消息不生效。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMSPAGINGSW:
          name: '语音寻呼开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '设置S1模式基于TALIST寻呼消息不重发的TAC区间，以及不重发的TAC区间对于IMS寻呼消息不生效。'
          data_source: '全网规划'
          pattern: ''
          default: ON
  examples:
    set_intermmefc_list:
    - FCSWITCH: ON
      MINTHD: 10
      MAXTHD: 200
    set_s1pagingfc_list:
    - FCSWITCH: ON
      SGSSWITCH: ON
      S102SWITCH: ON
      PAGINGRESENDSWITCH: ON
      ANTIBURSTSWITCH: ON
      PAEFCSWITCH: ON
      FCTHD: 150
      FCTHDMIN: 10
      RSVCAP: 15
      RSVVOCAP: 5
    set_paecheckpara_list:
    - CHECKINTERVAL: 1
      CHECKTIMES: 5
    set_paecheckthd_list:
    - RESTYPE: PBUF
      TRIGTHD: 60
      RESUMTHD: 30
    set_reversefcpara_list:
    - CTRLPLCY: PERCENT
      PERCENTTRGTHD: 50
      PERCENTRESUMTHD: 5
    set_softparaofbit_list:
    - DT: BYTE_EX_B
      PARANUM: 323
      VALUE: VALUE_1
      POSITION: 1
    set_flowctrlpara_list:
    - WEIGHTMODE: LEARN
      PROCTYPE: GBP
      MINWAL: 30
      MAXWAL: 2000
      MINWAL_GBDATA: 2500
      MAXWAL_GBDATA: 16000
      MAXWAL_GBPAGING: 900
      DROPRATETHD: 5
    set_flowctrlque_list:
    - APPTYPE: APP_2G
      MSG2GTYPE: ATTACH
      WEIGHT: 9
      QUELENTH: 400
      MSG3GTYPE: ATTACH
      MSG4GTYPE: ATTACH
    set_intermmefixfc_list:
    - ATTACHFCSWITCH: OFF
      SRFCSWITCH: OFF
      FCTYPE: PROCESS
      ATTACHSCOPE: PROCESS
      ATTACHTHD: 4080
      SRSCOPE: PROCESS
      SRTHD: 4080
    set_softparaofbit_list_10:
    - DT: BYTE_EX_B
      PARANUM: 339
      VALUE: VALUE_0
      POSITION: 1
    add_talistpagingcfg_list:
    - TAC: '0xBF85'
      TACRANGE: '0xBFFF'
      IMSPAGINGSW: OFF
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 设置Inter-MME流控参数。

```jinja2
{%- for item in set_intermmefc_list -%}
    SET INTERMMEFC:
    {#- --- 可选参数 --- -#}
    {%- if item.FCSWITCH is not none -%}
        FCSWITCH={{item.FCSWITCH}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：FCSWITCH=ON 时可选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        {%- if item.MINTHD is not none -%}
            MINTHD={{item.MINTHD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FCSWITCH=ON 时可选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        {%- if item.MAXTHD is not none -%}
            MAXTHD={{item.MAXTHD}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 设置S1寻呼流控参数，包括寻呼流控功能开关、寻呼流控速率门限、寻呼流控速率最小值和寻呼预留处理量等。

#### 3.1 ****SET S1PAGINGFC****

```jinja2
{%- for item in set_s1pagingfc_list -%}
    SET S1PAGINGFC:
    {#- --- 可选参数 --- -#}
    {%- if item.FCSWITCH is not none -%}
        FCSWITCH={{item.FCSWITCH}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：FCSWITCH=ON 时可选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        {%- if item.SGSSWITCH is not none -%}
            SGSSWITCH={{item.SGSSWITCH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FCSWITCH=ON 时可选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        {%- if item.S102SWITCH is not none -%}
            S102SWITCH={{item.S102SWITCH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FCSWITCH=ON 时可选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        {%- if item.PAGINGRESENDSWITCH is not none -%}
            PAGINGRESENDSWITCH={{item.PAGINGRESENDSWITCH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FCSWITCH=ON 时可选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        {%- if item.ANTIBURSTSWITCH is not none -%}
            ANTIBURSTSWITCH={{item.ANTIBURSTSWITCH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FCSWITCH=ON 时可选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        {%- if item.PAEFCSWITCH is not none -%}
            PAEFCSWITCH={{item.PAEFCSWITCH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FCSWITCH=ON 时可选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        {%- if item.FCTHD is not none -%}
            FCTHD={{item.FCTHD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FCSWITCH=ON 时可选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        {%- if item.FCTHDMIN is not none -%}
            FCTHDMIN={{item.FCTHDMIN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FCSWITCH=ON 时可选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        {%- if item.RSVCAP is not none -%}
            RSVCAP={{item.RSVCAP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FCSWITCH=ON 时可选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        {%- if item.RSVVOCAP is not none -%}
            RSVVOCAP={{item.RSVVOCAP}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.2 （可选）当开启PAE寻呼反压流控开关时，还需要设置PAE寻呼反压流控相关参数。

```jinja2
{%- if is_optional_pae_reverse_fc_params -%}
    {%- for item in set_paecheckpara_list -%}
        SET PAECHECKPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.CHECKINTERVAL is not none -%}
            CHECKINTERVAL={{item.CHECKINTERVAL}},
        {%- endif -%}
        {%- if item.CHECKTIMES is not none -%}
            CHECKTIMES={{item.CHECKTIMES}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_pae_reverse_fc_params -%}
    {%- for item in set_paecheckthd_list -%}
        SET PAECHECKTHD:
        {#- --- 必选参数 --- -#}
        RESTYPE={{item.RESTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.TRIGTHD is not none -%}
            TRIGTHD={{item.TRIGTHD}},
        {%- endif -%}
        {%- if item.RESUMTHD is not none -%}
            RESUMTHD={{item.RESUMTHD}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_pae_reverse_fc_params -%}
    {%- for item in set_reversefcpara_list -%}
        SET REVERSEFCPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.CTRLPLCY is not none -%}
            CTRLPLCY={{item.CTRLPLCY}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CTRLPLCY=PERCENT 时可选 --- -#}
        {%- if item.CTRLPLCY == 'PERCENT' -%}
            {%- if item.PERCENTTRGTHD is not none -%}
                PERCENTTRGTHD={{item.PERCENTTRGTHD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CTRLPLCY=PERCENT 时可选 --- -#}
        {%- if item.CTRLPLCY == 'PERCENT' -%}
            {%- if item.PERCENTRESUMTHD is not none -%}
                PERCENTRESUMTHD={{item.PERCENTRESUMTHD}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 配置是否开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。

```jinja2
{%- for item in set_softparaofbit_list -%}
    SET SOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    PARANUM={{item.PARANUM}},
    VALUE={{item.VALUE}},
    POSITION={{item.POSITION}},
    ;
{%- endfor -%}
```

### 5 设置流控系统参数。

### ****SET FLOWCTRLPARA****

```jinja2
{%- for item in set_flowctrlpara_list -%}
    SET FLOWCTRLPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.WEIGHTMODE is not none -%}
        WEIGHTMODE={{item.WEIGHTMODE}},
    {%- endif -%}
    {%- if item.PROCTYPE is not none -%}
        PROCTYPE={{item.PROCTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PROCTYPE=SPP/SGP/GBP/UPP 时必选 --- -#}
    {%- if item.PROCTYPE in ['SPP', 'SGP', 'GBP', 'UPP'] -%}
        MINWAL={{item.MINWAL}},
    {%- endif -%}
    {#- --- 条件必选：PROCTYPE=SPP/SGP/GBP/UPP 时必选 --- -#}
    {%- if item.PROCTYPE in ['SPP', 'SGP', 'GBP', 'UPP'] -%}
        MAXWAL={{item.MAXWAL}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PROCTYPE=GBP 时可选 --- -#}
    {%- if item.PROCTYPE == 'GBP' -%}
        {%- if item.MINWAL_GBDATA is not none -%}
            MINWAL_GBDATA={{item.MINWAL_GBDATA}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PROCTYPE=GBP 时可选 --- -#}
    {%- if item.PROCTYPE == 'GBP' -%}
        {%- if item.MAXWAL_GBDATA is not none -%}
            MAXWAL_GBDATA={{item.MAXWAL_GBDATA}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PROCTYPE=GBP 时可选 --- -#}
    {%- if item.PROCTYPE == 'GBP' -%}
        {%- if item.MAXWAL_GBPAGING is not none -%}
            MAXWAL_GBPAGING={{item.MAXWAL_GBPAGING}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PROCTYPE=SPP/SGP/GBP/UPP 时可选 --- -#}
    {%- if item.PROCTYPE in ['SPP', 'SGP', 'GBP', 'UPP'] -%}
        {%- if item.DROPRATETHD is not none -%}
            DROPRATETHD={{item.DROPRATETHD}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 设置流控队列参数。

### ****SET FLOWCTRLQUE****

```jinja2
{%- for item in set_flowctrlque_list -%}
    SET FLOWCTRLQUE:
    {#- --- 必选参数 --- -#}
    APPTYPE={{item.APPTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：APPTYPE=APP_2G 时必选 --- -#}
    {%- if item.APPTYPE == 'APP_2G' -%}
        MSG2GTYPE={{item.MSG2GTYPE}},
    {%- endif -%}
    {#- --- 条件必选：APPTYPE=APP_2G/APP_3G/APP_4G 时必选 --- -#}
    {%- if item.APPTYPE in ['APP_2G', 'APP_3G', 'APP_4G'] -%}
        WEIGHT={{item.WEIGHT}},
    {%- endif -%}
    {#- --- 条件必选：APPTYPE=APP_2G/APP_3G/APP_4G 时必选 --- -#}
    {%- if item.APPTYPE in ['APP_2G', 'APP_3G', 'APP_4G'] -%}
        QUELENTH={{item.QUELENTH}},
    {%- endif -%}
    {#- --- 条件必选：APPTYPE=APP_4G 时必选 --- -#}
    {%- if item.APPTYPE == 'APP_4G' -%}
        MSG4GTYPE={{item.MSG4GTYPE}},
    {%- endif -%}
    {#- --- 条件必选：APPTYPE=APP_3G 时必选 --- -#}
    {%- if item.APPTYPE == 'APP_3G' -%}
        MSG3GTYPE={{item.MSG3GTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 分别控制Inter-MME ServiceRequest流程和 Attach流程S1接口流控参数。与2中命令不建议同时开启。

```jinja2
{%- for item in set_intermmefixfc_list -%}
    SET INTERMMEFIXFC:
    {#- --- 可选参数 --- -#}
    {%- if item.ATTACHFCSWITCH is not none -%}
        ATTACHFCSWITCH={{item.ATTACHFCSWITCH}},
    {%- endif -%}
    {%- if item.SRFCSWITCH is not none -%}
        SRFCSWITCH={{item.SRFCSWITCH}},
    {%- endif -%}
    {%- if item.FCTYPE is not none -%}
        FCTYPE={{item.FCTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ATTACHFCSWITCH=ON 时可选 --- -#}
    {%- if item.ATTACHFCSWITCH == 'ON' -%}
        {%- if item.ATTACHSCOPE is not none -%}
            ATTACHSCOPE={{item.ATTACHSCOPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ATTACHFCSWITCH=ON 时可选 --- -#}
    {%- if item.ATTACHFCSWITCH == 'ON' -%}
        {%- if item.ATTACHTHD is not none -%}
            ATTACHTHD={{item.ATTACHTHD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SRFCSWITCH=ON 时可选 --- -#}
    {%- if item.SRFCSWITCH == 'ON' -%}
        {%- if item.SRSCOPE is not none -%}
            SRSCOPE={{item.SRSCOPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SRFCSWITCH=ON 时可选 --- -#}
    {%- if item.SRFCSWITCH == 'ON' -%}
        {%- if item.SRTHD is not none -%}
            SRTHD={{item.SRTHD}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 设置Inter-MME Service Request固定速率流控失效相关参数。

```jinja2
{%- for item in set_softparaofbit_list_10 -%}
    SET SOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    PARANUM={{item.PARANUM}},
    VALUE={{item.VALUE}},
    POSITION={{item.POSITION}},
    ;
{%- endfor -%}
```

### 9 设置S1模式基于TALIST寻呼消息不重发的TAC区间。

```jinja2
{%- for item in add_talistpagingcfg_list -%}
    ADD TALISTPAGINGCFG:
    {#- --- 必选参数 --- -#}
    TAC="{{item.TAC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.TACRANGE is not none -%}
        TACRANGE="{{item.TACRANGE}}",
    {%- endif -%}
    {%- if item.IMSPAGINGSW is not none -%}
        IMSPAGINGSW={{item.IMSPAGINGSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

