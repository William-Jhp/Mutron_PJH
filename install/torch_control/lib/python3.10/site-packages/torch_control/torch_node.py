import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import serial

class TorchSerialBridge(Node):
    def __init__(self):
        super().__init__('torch_serial_bridge')
        
        # 아두이노 포트 설정 (환경에 따라 /dev/ttyUSB0 등으로 변경)
        self.port = '/dev/ttyUSB0'
        self.baud = 9600
        
        try:
            self.ser = serial.Serial(self.port, self.baud, timeout=0.1)
            self.get_logger().info(f'아두이노 연결 성공: {self.port}')
        except Exception as e:
            self.get_logger().error(f'아두이노 연결 실패: {e}')

        # /torch_light 토픽 구독
        self.subscription = self.create_subscription(
            Bool,
            '/torch_light',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        if msg.data is True:
            self.ser.write(b'1')  # 아두이노 ledState = true 유도
            self.get_logger().info('명령 수신: ON -> 아두이노로 1 전송')
        else:
            self.ser.write(b'0')  # 아두이노 ledState = false 유도
            self.get_logger().info('명령 수신: OFF -> 아두이노로 0 전송')

def main(args=None):
    rclpy.init(args=args)
    node = TorchSerialBridge()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if hasattr(node, 'ser'):
            node.ser.write(b'0') # 종료 시 안전을 위해 끄기
            node.ser.close()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
