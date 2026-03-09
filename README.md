# Mutron

ROS2 기반 torch control 프로젝트입니다.
bool type으로 true / false --- topic메세지 publish하면 led on/off됩니다.
## 구성
- torch_control 노드(subscribe)
- ROS2 패키지 구조

#topic msg name
/torch_light

## 실행 방법
```bash
colcon build
source install/setup.bash
ros2 run torch_control torch_node
```

#추가
##아두이노 코드(pwm_serial_code)
시리얼 subscribe코드한테서 받아 랜덤하게 pwm조절해 led 플래쉬되는 코드
