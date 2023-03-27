def get_current_path():
    import pathlib
    return pathlib.Path(__file__).parent.resolve()


def get_settings_json(folder_separator):
    import files
    import json

    settings = files.read_file(str(get_current_path())+folder_separator+"settings.json")
    # print(type(settings))
    return json.loads(settings)
