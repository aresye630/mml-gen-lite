# 查询Diameter局向统计对象(LST STATDIAMHOST)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询Diameter局向统计对象。

- 若需要查询全部Diameter局向统计对象数据信息，请不要输入任何参数。
- 若需要查询某条Diameter局向统计对象数据信息，请输入“统计对象名称”或其他参数或这些参数的组合。

## 注意事项

无。

## 参数说明

| 参数标识       | 参数名称   | 参数说明                                                   |
|:-----------|:-------|:-------------------------------------------------------|
| OBJECTNAME | 统计对象名称 | 用于指示系统需要按照哪个统计对象名称来查询Diameter局向统计对象；若不输入，则表示所有的统计对象。   |
| MSGAPP     | 消息应用类型 | 用于指示系统需要按照哪个消息应用类型来查询Diameter局向统计对象；若不输入，则表示所有的消息应用类型。 |
| HN         | 主机名    | 用于指示系统需要按照哪个主机名来查询Diameter局向统计对象；若不输入，则表示所有的主机。        |

## 使用实例

1. 查询全部Diameter局向统计对象信息：

   ```
   LST STATDIAMHOST:;
   ```

   ```
   %%LST STATDIAMHOST:;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
   统计对象ID       统计对象名称      消息应用类型         主机名
       0              mme_1              S6a           mme.huawei1.com
       1              mme_2              S6a           mme.huawei2.com
   (结果个数 = 2)

   ---    END
   ```
2. 查询“统计对象名称”为“mme\_1”，“消息应用类型”为“S6a”，“主机名”为“mme.huawei1.com”Diameter局向统计对象信息：

   ```
   LST STATDIAMHOST: OBJECTNAME="mme_1", MSGAPP=S6a, HN="mme.huawei1.com";
   ```

   ```
   %%LST STATDIAMHOST: OBJECTNAME="mme_1", MSGAPP=S6a, HN="mme.huawei1.com";%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
      统计对象ID  =  0
    统计对象名称  =  mme_1
    消息应用类型  =  S6a
          主机名  =  mme.huawei1.com
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD STATDIAMHOST**命令中的参数说明。