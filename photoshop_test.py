import os
import re

from psd_tools import PSDImage


def sanitize_directory_name(name):
    return re.sub(r'[<>:"/\\|?*]', '_', name)

def save_layer_as_png(layer, path):
    # 레이어 이름을 안전하게 치환
    layer_name_sanitized = sanitize_directory_name(layer.name)
    layer_path = os.path.join(path, layer_name_sanitized)

    # 레이어가 그룹인 경우 재귀적으로 하위 레이어 탐색
    if layer.is_group():
        if not os.path.exists(layer_path):
            os.makedirs(layer_path)
        for child_layer in layer:
            save_layer_as_png(child_layer, layer_path)
    else:
        try:
            # 레이어를 PNG로 저장
            if not os.path.exists(path):
                os.makedirs(path)
            image = layer.topil()
            image_path = f"{layer_path}.png"
            image.save(image_path)
            print(f"Saved layer: {layer.name} as {image_path}")
        except Exception as e:
            print(f"Failed to save layer: {layer.name}")
            print(e)
            pass

def main():
    currPage = input("시작할 파일 이름 : ")
    psd_file_path = 'C:\\Users\\wpghk\\Desktop\\pyton_photoshop_test\\' + currPage + '.psd'
    base_path = 'C:\\Users\\wpghk\\Desktop\\pyton_photoshop_test\\layers'
    
    psd = PSDImage.open(psd_file_path)
    for layer in psd:
        save_layer_as_png(layer, base_path)

if __name__ == "__main__":
    main()
