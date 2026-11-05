# 查询DDN信令抑制参数(LST DDNTHROTPARA)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：MME**

该命令用于查询DDN（Downlink Data Notification）信令抑制参数。

#### 注意事项

无。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

1. 查询DDN信令抑制参数:

   `LST DDNTHROTPARA:;`

   ```
   %%LST DDNTHROTPARA:;%%
   RETCODE = 0  操作成功。

   输出结果如下
   --------------
     DDN信令抑制功能开关  =  关闭
           启动门限（%）  =  80
   DDN信令抑制时长（秒）  =  60
      策略发送时长（秒）  =  2
   (结果个数 = 1)

   ---    END
   ```
2. 查询DDN信令抑制参数:

   `LST DDNTHROTPARA:;`

   ```
   %%LST DDNTHROTPARA:;%%
   RETCODE = 0  操作成功。

   输出结果如下
   --------------
     DDN信令抑制功能开关  =  开启
           启动门限（%）  =  80
   DDN信令抑制时长（秒）  =  60
      策略发送时长（秒）  =  2
   (结果个数 = 1)

   ---    END
   ```

#### 输出结果说明

参见**SET DDNTHROTPARA**的参数说明。