if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()
    try:
        from nsuda_client.main import start_nsuda, configure_nsuda
    except Exception as e:
        print(e)
        print("Нажмите любую кнопку для продолжения")
        input()
    configure_nsuda()
    start_nsuda()