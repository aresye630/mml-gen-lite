# 查询智能分流APN (LST SUBSMARTAPN)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：MME**

该命令用于查询匹配用户签约APN智能分流配置。

#### 注意事项

无

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无

#### 使用实例

1. 查询智能分流APNNI，可以用如下命令：

   LST SUBSMARTAPN:;

   ```
   %%LST SUBSMARTAPN:;%%
   RETCODE = 0  操作成功。

   操作结果如下
   ------------
   智能分流APNNI  =  APN1
   (结果个数 = 1)

   ---    END
   ```

#### 输出结果说明

参见ADD SUBSMARTAPN的参数标识。