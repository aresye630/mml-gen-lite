# 查询服务发现条件信息（LST DISCCONDCFG）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询一条服务发现条件信息。

- 若需要查询所有网元类型的信息，不输入任何参数。
- 若需要查询某个网元类型的详细信息，请输入“网元类型”。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                         |
|:-------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------|
| NFTYPE | 网元类型   | 可选必选说明：可选参数 参数含义：用于指示系统需要按照哪个网元类型来查询服务发现条件信息；若不输入，则表示查询所有服务发现条件信息。 取值范围： CHF(CHF)BSF(BSF)SCP(SCP)AMF(AMF)NWDAF(NWDAF)PCF(PCF) 默认值：无。 配置原则：无。 |

## 使用实例

1. 查询所有服务发现条件信息：

   ```
   LST DISCCONDCFG:;
   ```

   ```
   %%LST DISCCONDCFG:;%% 
   RETCODE = 0  操作成功 

   操作结果如下
   ------------------------ 
   网元类型     CHF参数      BSF参数                                           SCP参数    优选位置值    AMF参数      NWDAF参数    PCF参数

   CHF          GPSI         NULL                                              NULL       NULL          NULL         NULL         NULL
   BSF          NULL         IPV4 Address&IPV4 DNN&IPV4 IPDOMAIN&IPV6 Prefix   NULL       NULL          NULL         NULL         NULL
   NWDAF        NULL         NULL                                              NULL       NULL          NULL         TAI          NULL
   NWDAF        NULL         NULL                                              NULL       NULL          NULL         EVENT        NULL
   (结果个数 = 4) 

   ---    END
   ```
2. 查询一个服务发现条件信息，“网元类型”为“BSF(BSF)”：

   ```
   LST DISCCONDCFG: NFTYPE=BSF;
   ```

   ```
   %%LST DISCCONDCFG: NFTYPE=BSF;%% 
   RETCODE = 0  操作成功
    
   操作结果如下 
   ------------------------       
     网元类型  =  BSF 
      CHF参数  =  NULL 
      BSF参数  =  IPV4 Address&IPV4 DNN&IPV4 IPDOMAIN&IPV6 Prefix
      SCP参数  =  NULL 
   优选位置值  =  NULL 
      AMF参数  =  NULL
    NWDAF参数  =  NULL
      PCF参数  =  NULL
   (结果个数 = 1) 

    ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD DISCCONDCFG**。