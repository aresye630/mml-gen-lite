# 查询用户数据统计扩展对象(LST STRNGEX)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询用户数据统计对象的配置信息：

- 若需要查询全部用户数据统计对象的配置信息，请不要输入任何参数。
- 若需要查询某条用户数据统计对象配置信息的详细信息，请输入“统计对象ID”或“统计类型”或这两个参数的组合。

## 注意事项

无。

## 参数说明

| 参数标识     | 参数名称   | 参数说明                                                |
|:---------|:-------|:----------------------------------------------------|
| OBJECTID | 统计对象ID | 用于指示系统按照哪个统计对象ID来查询用户数据统计对象的配置信息；若不输入，则表示所有的统计对象ID。 |
| TYPE     | 统计类型   | 用于指示系统按照哪个统计类型来查询用户数据统计对象的配置信息；若不输入，则表示所有的统计类型。     |

## 使用实例

1. 查询全部用户数据统计对象的配置信息：

   ```
   LST STRNGEX:;
   ```

   ```
   %%LST STRNGEX:;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    统计对象ID   统计类型            统计起始号码     统计结束号码     HLR序列号  路由码  源路由码  目的路由码  MME主机名   GUMMEI  PLMN    VLR号码  

    统计对象0    对所有用户进行统计  NULL             NULL             0          NULL    NULL      NULL        NULL        NULL    NULL    NULL     
    统计对象1    按HLRSN统计         NULL             NULL             22         NULL    NULL      NULL        NULL        NULL    NULL    NULL     
    统计对象3    按RN统计            NULL             NULL             0          1113    NULL      NULL        NULL        NULL    NULL    NULL     
    统计对象5    按HLRSN统计         NULL             NULL             240        NULL    NULL      NULL        NULL        NULL    NULL    NULL     
    统计对象6    按号段统计          8613821006006    8613821006010    0          NULL    NULL      NULL        NULL        NULL    NULL    NULL     
    统计对象32   按号段统计          460011310029001  460011310030001  0          NULL    NULL      NULL        NULL        NULL    NULL    NULL     
    统计对象227  按HLRSN统计         NULL             NULL             85         NULL    NULL      NULL        NULL        NULL    NULL    NULL     
    统计对象230  按MME主机名统计     NULL             NULL             0          NULL    NULL      NULL        huawei.com  NULL    646054  NULL     
    统计对象827  按VLRNUM前缀统计    NULL             NULL             0          NULL    NULL      NULL        NULL        NULL    NULL    861391000
   (结果个数 = 9)

   ---    END
   ```
2. 查询用户数据统计对象配置信息的详细信息，“统计对象ID”为“OBJECT230(统计对象230)”，“统计类型”为“STAT\_MMEHOST(按MME主机名统计)”：

   ```
   LST STRNGEX: OBJECTID=OBJECT230, TYPE=STAT_MMEHOST;
   ```

   ```
   %%LST STRNGEX: OBJECTID=OBJECT230, TYPE=STAT_MMEHOST;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
     统计对象ID  =  统计对象230
       统计类型  =  按MME主机名统计
   统计起始号码  =  NULL
   统计结束号码  =  NULL
      HLR序列号  =  0
         路由码  =  NULL
       源路由码  =  NULL
     目的路由码  =  NULL
      MME主机名  =  huawei.com
         GUMMEI  =  NULL
           PLMN  =  646054
        VLR号码  =  NULL
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

请参见**ADD STRNGEX**命令的参数说明。