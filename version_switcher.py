import json
import sys


def main():
    replace_from = "master" if sys.argv[1] == "test" else "test"
    replace_to = "test" if sys.argv[1] == "test" else "test"
    with open('config.json', 'r+') as config_file:
        config_data = json.load(config_file)
        config_new_urls = []
        for version_file_url in config_data["updates"]["versions_files"]:
            replace_from = "master"
            replace_to = "test"
            new_url = version_file_url.replace(replace_from, replace_to)
            config_new_urls.append(new_url)

        config_data["updates"]["versions_files"] = config_new_urls
        config_file.truncate(0)
        json.dump(config_file, config_data)

    with open('versions.json', 'r+') as versions_file:
        versions_data = json.load(versions_file)
        for file_name, file_data in versions_data.items():
            for url in file_data["urls"]:
                new_url = url.replace(replace_from, replace_to)
