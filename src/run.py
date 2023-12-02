import multiprocessing

if __name__ == "__main__":
    try:
        from nsuda_client.main import start_nsuda, configure_nsuda
    except Exception as e:
        print(e)
        print("Нажмите любую кнопку для продолжения")
        input()
    multiprocessing.freeze_support()
    configure_nsuda()
    start_nsuda()