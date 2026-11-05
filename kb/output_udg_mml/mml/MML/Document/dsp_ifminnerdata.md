# 查询IFM模块内部数据（DSP IFMINNERDATA）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询IFM内部数据信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识      | 参数名称       | 参数说明                                                                                                                                                                                                                  |
|:----------|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TYPE      | 接口管理内部数据类型 | 可选必选说明：必选参数 参数含义：该参数用来查询内部数据类型。 数据来源：本端规划 取值范围：枚举类型。 INNERCFG_IF：内部配置接口索引。INNERCFG_NAME：内部配置接口名称。INNERCFG_STAT：内部配置统计信息。MNGIF：管理接口信息。 默认值：无                                                                           |
| CID       | 组件CID      | 可选必选说明：必选参数 参数含义：该参数指定组件CID。 数据来源：本端规划 取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。 默认值：无                                                                                                                                       |
| IFNAME    | 接口名称       | 可选必选说明：条件必选参数 前提条件：该参数在“TYPE”配置为“INNERCFG_NAME”时为必选参数。 参数含义：该参数用于指定接口名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。 默认值：无 配置原则：请使用LST INTERFACE命令查看可用接口。                                                      |
| IFINDEX   | 接口索引       | 可选必选说明：条件必选参数 前提条件：该参数在“TYPE”配置为“INNERCFG_IF”时为必选参数。 参数含义：该参数指定接口索引。 数据来源：本端规划 取值范围：整数类型，取值范围为1～4294967294。 默认值：无                                                                                                     |
| MNGIFTYPE | 管理口查询类型    | 可选必选说明：条件必选参数 前提条件：该参数在“TYPE”配置为“MNGIF”时为必选参数。 参数含义：该参数用来查询管理口数据类型。 数据来源：本端规划 取值范围：枚举类型。 MNGIF_LOG_FROM_DEVM：来自DEVM日志信息。MNGIF_LOG_TO_DEVM：发往DEVM日志信息。MNGIF_LOG_TO_FES：发往FES日志信息。MNGIF_LOG_FES_SMOOTH：同步FES日志信息。 默认值：无 |

#### 使用实例

- 按接口索引查询IFM内部接口信息：

  ```
  DSP IFMINNERDATA:TYPE=INNERCFG_IF, CID="0x807a0016", IFINDEX=4;
  ```

  ```
          RETCODE = 0  操作成功。

           结果如下
          ------------------------
          查询结果数据

          Com-Cid:  0x807a0016
          ================================================================================
          IfIndex:4          VrId: 0
          ==============================
          isExistIf:  1
          isVisiable: 1
          stackType:  255
          ifNameLen:  20
          ifName:     GigabitEthernet0/0/1
          =======no main if===========
          (结果个数 = 2)
          ---    END
  ```
- 按接口名称查询IFM内部接口信息：

  ```
  DSP IFMINNERDATA:TYPE=INNERCFG_NAME, CID="0x807a0016", IFNAME="GigabitEthernet0/0/1";
  ```

  ```
          RETCODE = 0  操作成功。

           结果如下
          ------------------------
          查询结果数据

           Com-Cid:  0x807a0016
          ================================================================================

          =======if information===========
           IfIndex:    4
           VrId:       0
           isExistIf:  1
           isVisiable: 1
           ifNameLen:  20
           ifName:     GigabitEthernet0/0/1

          (结果个数 = 2)
          ---    END
  ```
- 查询IFM配置统计信息：

  ```
  DSP IFMINNERDATA:TYPE=INNERCFG_STAT, CID="0x807a0017";
  ```

  ```
          RETCODE = 0  操作成功。

           结果如下
          ------------------------
          查询结果数据

           Com-Cid:  0x807a0017
          ===============================================================================
           IfInnerCfg: 7fdc8ce6073c, pThis: 7fdc8ce5ef60
          ==============================
           Name2Index Node Number: 11
           Run Statistics:
             AddIf:        11         DelIf:        0          SetIf:        0
             GetIf:        1          Get-VrNul:    0          Get-IfNul:    0
             GetNextIf:    0          GetNext-VrNul:0          GetNext-IfNul:0
             GetByName:    13         GetByNameNul: 12         DelIfTblNul:  0
             DelVrTblNul:  0          NewVrTbl:     1          DelVrTbl:     0
             DelN2INul:    0
           Error Statistics:
             MallocFail:   0          AddVrIfTbl:   0          AddN2I:       0
             NullIfSet:    0          NameLen0:     0          NameLen>64:   0
             AddExistIf:   0          InsertIf:     0          InsertVr:     0
             AlreadyInIdx: 0          NotInIdx:     0          DbParseFail:  0
             InnInfo:      11         InnInfoOfIfIdx:13
             TypeName:     5          Order:        11         PanelOrder:   0
          (结果个数 = 2)
          ---    END
  ```
- 查询管理口发往FES消息日志信息：

  ```
  DSP IFMINNERDATA:TYPE=MNGIF,CID="0x807A0017",MNGIFTYPE=MNGIF_LOG_TO_FES;
  ```

  ```
           RETCODE = 0  操作成功。

           结果如下
           --------
           查询结果数据

           Com-Cid:  0x807a0017
           ================================================================================

           Mng-If info to FES:
           -------------------------------------------------------------------------------
           IfIndex      Time                           IfInfo         Data
           -------------------------------------------------------------------------------
           3            2017-04-26 08:46:38            MIFACTIVE      Act-Idx:4  Bak-Idx:4294967295
           3            2017-04-26 08:47:29            MIFACTIVE      Act-Idx:4  Bak-Idx:5

          (结果个数 = 2)
          ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释             |
|:--------|:------------------|
| 查询结果数据  | 用来显示IFM内部的查询结果数据。 |