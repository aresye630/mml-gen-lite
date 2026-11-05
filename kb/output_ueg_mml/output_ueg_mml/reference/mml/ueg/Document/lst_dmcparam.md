# 查询DMC参数(LST DMCPARAM)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于在配置数据库中查询DMC参数记录。

- 若需要查询全部DMC参数记录，请不要输入任何参数。
- 若需要查询某个DMC参数的对应记录，请输入“参数名称”参数。

**说明** 

该命令仅在Full-stack虚机场景下支持。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                            |
|:-------|:-------|:------------------------------------------------|
| NAME   | 参数名称   | 用于指示系统按照哪个DMC参数名称来查询DMC参数记录；若不输入，则表示所有的DMC参数记录。 |

## 使用实例

1. 查询全部DMC参数记录。

   `LST DMCPARAM:;`

   ```
   %%LST DMCPARAM:;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
    参数名称  参数值   

    service1  carrier_name1
    service   carrier_name
   (结果个数 = 2)

   ---    END
   ```
2. 查询某一个DMC参数的对应记录，“参数名称”为“service”。

   `LST DMCPARAM: NAME="service";`

   ```
   %%LST DMCPARAM: NAME="service";%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------
   参数名称  =  service
     参数值  =  carrier_name
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

请参见**ADD DMCPARAM**命令的参数说明。