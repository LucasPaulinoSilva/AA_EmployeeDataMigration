import zipfile
import config


def fileExtraction() -> None:
    # Concatena caminho da pasta com o nome do arquivo e extensão
    path_file_zip = config.PATH_FILE + config.NAME_PROGRAM + '.zip'

    # Extrai o arquivo zip
    with zipfile.ZipFile(path_file_zip, 'r') as zip_ref:
        zip_ref.extractall(config.PATH_FILE)


if __name__ == '__main__':
    fileExtraction()
