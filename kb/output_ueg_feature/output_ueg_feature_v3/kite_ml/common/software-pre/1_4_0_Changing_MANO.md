# 修改VNF LCM对接参数

* 操作场景
* 必备事项
* 操作步骤
* 任务实例

#### 操作场景

场景一：VNF采用VNF LCM安装，然后安装VNFM Agent。此时要将VNF对接到VNFM Agent，参考本文操作。

场景二：已预安装VNF和VNFM Agent。当设备上电后，VNFM Agent和中心侧管理面 VNF LCM对接，VNF LCM会将VNF LCM的IP地址自动传递给VNFM Agent，VNFM Agent将VNF LCM的IP地址传递给VNF。此过程无需人工操作。仅当VNFM Agent自动传递给VNF的流程故障时，才需要参考本文将VNF对接到VNFM Agent。

#### 必备事项

**前提条件**

* 已经完成硬件设备安装和相关网络配置。
* 已经确认现场网络规划的网元对接MAE-VNF LCM/U2020 VNF LCM帐户信息与VNF生产预安装的预设参数值不同。
* 已经修改VNF LCM Agent的IP地址为局方的规划值。
* 已经完成配置调测PC与OMU操作维护IP互通，确保调测使用的PC与VNF OMU操作维护IP可以正常通信。
* 已通过MAE或UEG OMPortal登录华为操作维护系统。

**数据**

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| MAE-VNF LCM/U2020 VNF LCM对接参数 | 主节点IP（MASTERIP）  这是VNFM-Agent的浮动IP地址。 | 10.10.10.10 | 对端获取 | UEG上的命令：  **MOD VNFMINFO** |
|  | 备节点IP（SLAVEIP）  当前VNFM-Agent 备用VM的IP地址。 | 空白，不用填写。 | 对端获取 |  |
|  | 用户名（USER） | nerestuser | 对端获取 |  |
|  | 密码（PWD） | \*\*\*\*\*\* | 对端获取 |  |

nerestuser用户用于网元连接MAE-VNF LCM/U2020 VNF LCM，进行网元虚拟机复位、上电、下电和查询虚拟机状态操作。

#### 操作步骤

1. 登录UEG OMPortal，选择“应用管理 > MML”。
2. 进入“MML命令行-UEG”窗口。
3. 修改MAE-VNF LCM/U2020 VNF LCM对接信息。

   ```
   MOD VNFMINFO: MASTERIP="10.10.10.10",USER="nerestuser", PWD="******";
   ```

#### 任务实例

**任务描述**

修改MAE-VNF LCM/U2020 VNF LCM对接参数。

**脚本**

1. 登录UEG OMPortal，选择“应用管理 > MML”。
2. 修改MAE-VNF LCM/U2020 VNF LCM对接参数。

   ```
   MOD VNFMINFO: MASTERIP="10.10.10.10",USER="user", PWD="******";
   ```

版权所有 © 华为技术有限公司
