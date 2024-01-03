#采用xml中的ElementTree包进行解析
import xml.etree.ElementTree as ET

#定义函数进行文件的解析，file代表文件
def parse_opendrive(file):
    #创建解析的对象
    tree = ET.parse(file)
    #获取根对象，root指向所需要解析的对象
    root = tree.getroot()
    #获取header里面的信息，header包含图商、坐标等信息
    for header in root.findall('header'):
        revMajor = header.get('revMajor')
        print('revMajor:{}'.format(revMajor))
        for vectorScene in header.findall('userData/vectorScene'):
            program = vectorScene.get('program')
            print('program:{}'.format(program))

    # 遍历road
    for road in root.findall('road'):
        road_id = road.get('id')
        road_name = road.get('name', 'Unnamed Road')  # 默认值为 'Unnamed Road'
        road_length = road.get('length')
        print(f"Road ID: {road_id}, Name: {road_name}, Length: {road_length}")

        # 解析道路类型，road作为根对象
        for road_type in road.findall('type'):
            road_type_value = road_type.get('type')
            speed_limit = road_type.find('speed').get('max')
            print(f"  Road Type: {road_type_value}, Speed Limit: {speed_limit}")

        # 解析车道信息，road子对象
        for lane_section in road.findall('lanes/laneSection'):
            s = lane_section.get('s')
            print(f"  Lane Section Start: {s}")
            #//代表所有子对象
            for lane in lane_section.findall('.//lane'):
                lane_id = lane.get('id')
                lane_type = lane.get('type')
                print(f"    Lane ID: {lane_id}, Type: {lane_type}")

                # 解析车道宽度
                for width in lane.findall('width'):
                    width_value = width.get('a')  # 只获取 'a' 属性
                    print(f"      Width: {width_value}")

if __name__ == "__main__":
    opendrive_file = 'one road.xodr'
    parse_opendrive(opendrive_file)
