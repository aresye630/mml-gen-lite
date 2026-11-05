# 查询Diameter路由组(LST DMRTS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于在Diameter路由组表中查询路由组数据的记录。

- 若需要查询全部Diameter路由组数据记录的信息，请不要输入任何参数。
- 若需要查询某些Diameter路由组数据记录的信息，请输入“路由组名称”或其他参数或这些参数的组合。

## 注意事项

无。

## 参数说明

| 参数标识     | 参数名称   | 参数说明                                                              |
|:---------|:-------|:------------------------------------------------------------------|
| RTSNAME  | 路由组名称  | 用于指示系统按照哪个Diameter路由组名称来查询Diameter路由组信息；若不输入，则表示所有的Diameter路由组名称。 |
| RN       | 目标域名   | 用于指示系统按照哪个目标域名来查询Diameter路由组信息；若不输入，则表示所有的目标域名。                   |
| APPID    | 应用类型   | 用于指示系统按照哪种应用类型来查询Diameter路由组信息；若不输入，则表示所有的应用类型。                   |
| RTYPE    | 路由组类型  | 用于指示系统按照哪种路由组类型来查询Diameter路由组信息；若不输入，则表示所有的路由组类型。                 |
| ACTION   | 消息路由方式 | 用于指示系统按照哪种消息路由方式来查询Diameter路由组信息；若不输入，则表示所有的消息路由方式。               |
| SMODE    | 路由选择模式 | 用于指示系统按照哪种路由选择模式来查询Diameter路由组信息；若不输入，则表示所有的路由选择模式。               |
| LOCALNAM | 本端实体名称 | 用于指示系统按照哪个本端实体名称来查询Diameter路由组信息；若不输入，则表示所有的本端实体名称。               |

## 使用实例

1. 查询所有Diameter路由组表中的路由组配置信息。

   ```
   LST DMRTS:;
   ```

   ```
   %%LST DMRTS:;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    路由组名称  目标域名  应用类型  消息路由方式  路由选择模式  路由组标识  本端实体名称

    S6A/S6D     default   S6a/S6d   本地处理      轮询方式      0           NULL
    SWX         default   SWx       本地处理      轮询方式      1           NULL
    SLH         default   SLh       本地处理      轮询方式      2           NULL
    CX/DX       default   Cx/Dx     本地处理      轮询方式      3           NULL
    SH          default   Sh        本地处理      轮询方式      4           NULL
    ZH          default   Zh        本地处理      轮询方式      5           NULL
    S13         default   S13/S13'  本地处理      轮询方式      6           NULL
    Ml          default   Ml        本地处理      轮询方式      7           NULL
    S6b         default   S6b       本地处理      轮询方式      8           NULL
    SWm         default   SWm       本地处理      轮询方式      9           NULL
    STa/SWa     default   STa/Swa   本地处理      轮询方式      10          NULL
    Zn          default   Zn        本地处理      轮询方式      11          NULL             
    AAAVALID    aaavalid  S6a/S6d   本地处理      轮询方式      12          AAA
   (结果个数 = 13)
   ---    END
   ```
2. 查询Diameter路由组表中的一条路由组配置信息，“路由组名称”为“AAAVALID”。

   ```
   LST DMRTS: RTSNAME="AAAVALID";
   ```

   ```
   %%LST DMRTS: RTSNAME="AAAVALID";%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
     路由组名称  =  AAAVALID
       目标域名  =  aaavalid
       应用类型  =  S6a/S6d
   消息路由方式  =  本地处理
   路由选择模式  =  轮询方式
     路由组标识  =  11
   本端实体名称  =  AAA
   (结果个数 = 1)
   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见

**ADD DMRTS**

命令的参数说明，表1列出的是未包含在

**ADD DMRTS**

命令参数说明中的输出项。

| 输出项名称   | 输出项解释                     |
|:--------|:--------------------------|
| 路由组标识   | 用于返回一个Diameter路由组的数据记录索引。 |