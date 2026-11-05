# 查询Diameter路由组状态(DSP DMRTS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于请求系统显示指定的Diameter路由组的状态。

- 若需要请求系统显示全部Diameter路由组数据记录的信息，请不要输入任何参数。
- 若需要请求系统显示某个Diameter路由组数据记录的信息，请输入“路由组名称”参数。

## 注意事项

无。

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                               |
|:--------|:-------|:---------------------------------------------------|
| RTSNAME | 路由组名称  | 用于请求系统显示哪个Diameter路由组的状态信息；若不输入，则表示所有的Diameter路由组。 |

## 使用实例

1. 显示所有Diameter路由组表中的路由组配置状态信息：

   ```
   DSP DMRTS:;
   ```

   ```
   %%DSP DMRTS:;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    路由组名称  目标域名  应用类型  消息路由方式  路由选择模式  Diameter路由组状态  路由组标识  本端实体名称

    S6A/S6D     default   S6a/S6d   本地处理      轮询方式      断开                0           NULL
    SWX         default   SWx       本地处理      轮询方式      断开                1           NULL
    SLH         default   SLh       本地处理      轮询方式      断开                2           NULL
    CX/DX       default   Cx/Dx     本地处理      轮询方式      断开                3           NULL
    SH          default   Sh        本地处理      轮询方式      断开                4           NULL
    ZH          default   Zh        本地处理      轮询方式      断开                5           NULL
    S13         default   S13/S13'  本地处理      轮询方式      断开                6           NULL
    Ml          default   Ml        本地处理      轮询方式      断开                7           NULL
    S6b         default   S6b       本地处理      轮询方式      断开                8           NULL
    SWm         default   SWm       本地处理      轮询方式      断开                9           NULL
    STa/SWa     default   STa/Swa   本地处理      轮询方式      断开                10          NULL
    Zn          default   Zn        本地处理      轮询方式      断开                11          NULL
    AAAVALID    aaavalid  S6a/S6d   本地处理      轮询方式      断开                12          AAA
   (结果个数 = 13)
   ---    END
   ```
2. 显示Diameter路由组表中的一条路由组配置状态信息，“路由组名称”为“AAAVALID”：

   ```
   DSP DMRTS: RTSNAME="AAAVALID";
   ```

   ```
   %%DSP DMRTS: RTSNAME="AAAVALID";%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
           路由组名称  =  AAAVALID
             目标域名  =  aaavalid
             应用类型  =  S6a/S6d
         消息路由方式  =  本地处理
         路由选择模式  =  轮询方式
   Diameter路由组状态  =  断开
           路由组标识  =  11
         本端实体名称  =  AAA
   (结果个数 = 1)
   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见

**ADD DMRTS**

命令的参数说明。表1列出的是未包含在

**ADD DMRTS**

参数说明中的输出项。

| 输出项名称         | 输出项解释                                                                                                                                                                      |
|:--------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Diameter路由组状态 | 用于标识Diameter路由组的工作状态。正常：本端与对端Diameter路由组处于正常状态。断开：本端与对端Diameter路由组处于断开状态。当本端出现故障、对端故障或网络通信故障时，会造成Diameter路由组断开。拥塞：Diameter路由组处于拥塞状态。当本端出现业务量过大或者网络通信质量差时，会造成Diameter路由组拥塞。 |
| 路由组标识         | 用于标识Diameter路由组的ID。                                                                                                                                                        |
| 本端实体名称        | 用于标识Diameter路由组关联的本端实体名称。                                                                                                                                                  |