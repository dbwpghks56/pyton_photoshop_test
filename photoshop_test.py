import os
import re

from PIL import Image
from psd_tools import PSDImage
from psd_tools.constants import BlendMode


def save_layer_add_background(layer, path):
    background = Image.new("RGBA", (1920, 1080), (255, 255, 255, 0))
    image: Image
    
    if layer.is_group():
        image = layer.composite()
        
    else:
        image = layer.topil()

    offset = layer.bbox[0:2]
    background.paste(image, offset, image)
    background.save(f"{path}/{layer.name}.png", format='PNG', optimize=True)

def sanitize_directory_name(name):
    return re.sub(r'[<>:"/\\|?*]', '_', name)


def save_layer_as_png(layer, path):
    # 레이어 이름을 안전하게 치환
    layer_name_sanitized = sanitize_directory_name(layer.name)
    layer_path = os.path.join(path, layer_name_sanitized)
    # layer 변수 타입
    # print(type(layer))
    # 레이어가 그룹인 경우 재귀적으로 하위 레이어 탐색
    if layer.is_group():
        if not os.path.exists(layer_path):
            os.makedirs(layer_path)
            
        layer.visible = True
        for child_layer in layer:
            
            try:
                save_layer_add_background(child_layer, layer_path)
                    
            except Exception as e:
                print(f"Failed to save layer: {layer.name}")
                print(e)
                pass


def main():
    # currPage = input("시작할 파일 이름 : ")
    psd_file_path = f'C:\\Users\\wpghk\\Desktop\\pyton_photoshop_test\\[인하대]SDGs_02.psd'
    base_path = 'C:\\Users\\wpghk\\Desktop\\pyton_photoshop_test\\layers'
    
    psd = PSDImage.open(psd_file_path)
    for layer in psd:
        save_layer_as_png(layer, base_path)

if __name__ == "__main__":
    main()
