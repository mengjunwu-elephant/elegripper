# 1 串口库安装
```bash
pip install pyserial
```

# 2 案例运行

```python
python demo.py
```
# 3 接口介绍

## 1. 夹爪信息查询

### get_firmware_version()

- **功能:** 获取夹爪固件主版本号
- **参数:** 无
- **返回:** `(int)`固件主版本号

### get_modified_version()

- **功能:** 获取夹爪固件次版本号
- **参数:** 无
- **返回:** `(int)`固件次版本号

### get_gripper_Id()

- **功能:** 获取夹爪ID
- **参数:** 无
- **返回:** `(int)`夹爪ID


### get_gripper_baud()

- **功能:** 获取夹爪波特率
- **参数:** 无
- **返回:**`(int)` 0-5
    - `0`: 115200
    - `1`: 1000000
    - `2`: 57600
    - `3`: 19200
    - `4`: 9600
    - `5`: 4800

### get_gripper_value()

- **功能:** 获取夹爪的当前位置数据信息
- **参数:** 无
- **返回:** `(int)`夹爪的当前位置数据

### get_gripper_status()

- **功能:** 获取夹爪的当前状态
- **参数:** 无
- **返回:**`(int)` 0-3
    - `0`:  正在运动
    - `1`: 停止运动，未检测到夹到物体
    - `2`: 停止运动，检测到夹到了物体
    - `3`: 检测到夹到物体以后，物体掉落

### get_gripper_speed()

- **功能:** 获取夹爪的当前速度
- **参数:** 无
- **返回:** `(int)`夹爪的当前速度

### get_gripper_P()

- **功能:** 获取夹爪PID的P值
- **参数:** 无
- **返回:** `(int)`夹爪PID的P值

### get_gripper_I()

- **功能:** 获取夹爪PID的I值
- **参数:** 无
- **返回:** `(int)`夹爪PID的I值

### get_gripper_D()

- **功能:** 获取夹爪PID的D值
- **参数:** 无
- **返回:** `(int)`夹爪PID的D值

### get_gripper_cw()

- **功能:** 获取夹爪顺时针可运行误差
- **参数:** 无
- **返回:** `(int)`夹爪顺时针可运行误差

### get_gripper_cww()

- **功能:** 获取夹爪逆时针可运行误差
- **参数:** 无
- **返回:** `(int)`夹爪逆时针可运行误差

### get_gripper_mini_pressure()

- **功能:** 获取夹爪最小启动力
- **参数:** 无
- **返回:** `(int)`夹爪最小启动力

### get_gripper_io_open_value()

- **功能:** 获取夹爪Io张开角度
- **参数:** 无
- **返回:** `(int)`夹爪Io张开角度

### get_gripper_io_close_value()

- **功能:** 获取夹爪Io闭合角度
- **参数:** 无
- **返回:** `(int)`获取夹爪Io闭合角度

### get_gripper_queue_count()

- **功能:** 获取夹爪当前队列的数据量
- **参数:** 无
- **返回:** `(int)`夹爪当前队列的数据量

### get_gripper_vir_pos()

- **功能:** 获取夹爪舵机虚位数值
- **参数:** 无
- **返回:** `(int)`夹爪舵机虚位数值
  
### get_gripper_protection_current()

- **功能:** 获取夹爪夹持电流
- **参数:** 无
- **返回:** `(int)`夹爪夹持电流

## 2 夹爪设置

### set_gripper_Id(value)

- **功能:** 设置夹爪ID号
- **参数:** 
  - `value`: `(int)` 夹爪ID，取值范围 `1-254`
- **返回:**`(int)` 0-1
  - `0`: 失败
  - `1`: 成功

### set_gripper_baud(value)

- **功能:** 设置夹爪波特率
- **参数:** 
  - `value`: `(int)` 夹爪波特率，取值范围 `0-5`
    - `0`: 115200
    - `1`: 1000000
    - `2`: 57600
    - `3`: 19200
    - `4`: 9600
    - `5`: 4800
- **返回:**`(int)` 0-1
  - `0`: 失败
  - `1`: 成功
  
### set_gripper_enable(value)

- **功能:** 设置夹爪使能状态
- **参数:** 
  - `value`: `(int)` 使能状态，取值范围 `0-1`
    - `0`: 掉使能
    - `1`: 上使能
- **返回:**`(int)` 0-1
  - `0`: 失败
  - `1`: 成功

### set_gripper_value(value,speed)

- **功能:** 设置夹爪以指定的速度转动到指定的位置
- **参数:** 
  - `value`: `(int)` 位置，取值范围 `0-100`
  - `speed`: `(int)` 速度，取值范围 `1-100` 
- **返回:**`(int)` 0-1
  - `0`: 失败
  - `1`: 成功

### set_gripper_calibration()

- **功能:** 设置夹爪零位校准
- **参数:** 无
- **返回:**`(int)` 0-1
  - `0`: 失败
  - `1`: 成功

### set_gripper_P(value)

- **功能:** 设置夹爪PID的P值
- **参数:** 
  - `value`: `(int)` P值，取值范围 `0-254`
- **返回:**`(int)` 0-1
  - `0`: 失败
  - `1`: 成功

### set_gripper_I(value)

- **功能:** 设置夹爪PID的I值
- **参数:** 
  - `value`: `(int)` I值，取值范围 `0-254`
- **返回:**`(int)` 0-1
  - `0`: 失败
  - `1`: 成功

### set_gripper_D(value)

- **功能:** 设置夹爪PID的D值
- **参数:** 
  - `value`: `(int)` D值，取值范围 `0-254`
- **返回:**`(int)` 0-1
  - `0`: 失败
  - `1`: 成功

### set_gripper_cw(value)

- **功能:** 设置夹爪顺时针可运行误差
- **参数:** 
  - `value`: `(int)` 误差，取值范围 `0-254`
- **返回:**`(int)` 0-1
  - `0`: 失败
  - `1`: 成功

### set_gripper_cww(value)

- **功能:** 设置夹爪逆时针可运行误差
- **参数:** 
  - `value`: `(int)` 误差，取值范围 `0-254`
- **返回:**`(int)` 0-1
  - `0`: 失败
  - `1`: 成功

### set_gripper_mini_pressure(value)

- **功能:** 设置夹爪最小启动力
- **参数:** 
  - `value`: `(int)` 最小启动力，取值范围 `0-254`
- **返回:**`(int)` 0-1
  - `0`: 失败
  - `1`: 成功

### set_gripper_torque(value)

- **功能:** 设置夹爪扭矩
- **参数:** 
  - `value`: `(int)` 扭矩，取值范围 `0-300`
- **返回:**`(int)` 0-1
  - `0`: 失败
  - `1`: 成功

### set_gripper_output(value)

- **功能:** 设置夹爪IO
- **参数:** 
  - `value`: `(int)` 夹爪IO，取值范围 `0-3`
    - `0`: out1 off,out2 off
    - `1`: out1 on,out2 off
    - `2`: out1 off,out2 on
    - `3`: out1 on,out2 on
    
- **返回:**`(int)` 0-1
  - `0`: 失败
  - `1`: 成功

### set_gripper_io_open_value(value)

- **功能:** 设置夹爪Io张开位置
- **参数:** 
  - `value`: `(int)` 位置，取值范围 `0-100`
- **返回:**`(int)` 0-1
  - `0`: 失败
  - `1`: 成功

### set_gripper_io_close_value(value)

- **功能:** 设置夹爪Io闭合位置
- **参数:** 
  - `value`: `(int)` 位置，取值范围 `0-100`
- **返回:**`(int)` 0-1
  - `0`: 失败
  - `1`: 成功

### set_gripper_speed(speed)

- **功能:** 设置夹爪速度
- **参数:** 
  - `speed`: `(int)` 速度，取值范围 `1-100`
- **返回:**`(int)` 0-1
  - `0`: 失败
  - `1`: 成功

### set_abs_gripper_value(value,speed)

- **功能:** 设置夹爪以指定的速度转动到指定的绝对位置
- **参数:**
  - `value`: `(int)` 位置，取值范围 `1-100` 
  - `speed`: `(int)` 速度，取值范围 `1-100`
- **返回:**`(int)` 0-1
  - `0`: 失败
  - `1`: 成功

### set_gripper_vir_pos(value)

- **功能:** 设置夹爪舵机虚位数值
- **参数:** 
  - `value`: `(int)` 虚位，取值范围 `0-100`
- **返回:**`(int)` 0-1
  - `0`: 失败
  - `1`: 成功

### set_gripper_protection_current(value)

- **功能:** 设置夹爪夹持电流
- **参数:** 
  - `value`: `(int)` 虚位，取值范围 `1-254`
- **返回:**`(int)` 0-1
  - `0`: 失败
  - `1`: 成功

### set_gripper_pause()

- **功能:** 设置夹爪暂停运动
- **备注:** 只对set_abs_gripper_value()生效
- **参数:** 无
- **返回:**`(int)` 0-1
  - `0`: 失败
  - `1`: 成功

### set_gripper_resume()

- **功能:** 设置夹爪恢复运动
- **备注:** 只对set_abs_gripper_value()生效
- **参数:** 无
- **返回:**`(int)` 0-1
  - `0`: 失败
  - `1`: 成功

### set_gripper_stop()

- **功能:** 设置夹爪停止运动，并清空消息队列
- **备注:** 只对set_abs_gripper_value()生效
- **参数:** 无
- **返回:**`(int)` 0-1
  - `0`: 失败
  - `1`: 成功

