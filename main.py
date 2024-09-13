from service.files_service import create_files_if_not_exist
from service.mission_service import pilots


def main():
    create_files_if_not_exist()
    pilots()



if __name__ == '__main__':
    main()

