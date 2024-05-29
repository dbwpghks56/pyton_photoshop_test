"""Export every layer as a .png file."""
# Import built-in modules
import os

# Import third-party modules
import photoshop.api as ps
# Import local modules
from photoshop import Session


def hide_all_layers(layers):
    for layer in layers:
        layer.visible = False


def main():
    psd_file_path = 'C:\\Users\\wpghk\\Desktop\\pyton_photoshop_test\\images.psd'
    base_path = 'C:\\Users\\wpghk\\Desktop\\pyton_photoshop_test'
    with Session(psd_file_path, action="open") as ps:
        doc = ps.active_document
        options = ps.PNGSaveOptions()
        options.compression = 1
        layers = doc.artLayers
        print("shoot")
        for layer in layers:
            print("what")
            hide_all_layers(layers)
            layer.visible = True
            layer_path = os.path.join(base_path, layer.name)
            print(layer_path)
            if not os.path.exists(layer_path):
                os.makedirs(layer_path)
            image_path = os.path.join(layer_path, f"{layer.name}.png")
            print(image_path)
            doc.saveAs(image_path, options=options, asCopy=True)
        ps.alert("Task done!")
        ps.echo(doc.activeLayer)


if __name__ == "__main__":
    main()
